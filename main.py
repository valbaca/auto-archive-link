import re
import dotenv
import os
import discord
from discord.ext import commands
import tldextract
from domains import domains_to_archive

description = """
A simple discord bot that provides archive.is links for urls
"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", description=description, intents=intents)

prefix = "https://archive.is/newest/"


def to_archive_link(url: str) -> str:
    return prefix + url


url_pattern = r"https?://(?:www\.)?\S+|www\.\S+"


def should_archive_link(url: str) -> bool:
    """Returns whether the given url should get an archive link (to avoid spam)"""
    try:
        extracted = tldextract.extract(url)
        if not extracted:
            return False
    except:
        return False
    domain = f"{extracted.domain}.{extracted.suffix}"
    if domain in domains_to_archive:
        # matched!
        return True
    return False


@bot.command()
async def archive(ctx, url: str):
    """Allows manual invocation: !archive url"""
    await ctx.send(to_archive_link(url))


@bot.event
async def on_message(message: discord.Message):
    """Checks the message for a link with a specified domain and if matches, replies with archive url"""
    if message.author == bot.user:
        # avoid infinite loop!
        return
    urls = re.findall(url_pattern, message.content.lower())
    if not urls:
        return
    for url in urls:
        if should_archive_link(url):
            reply_content = to_archive_link(url)
            await message.reply(reply_content, silent=True, mention_author=None)
    return


def main():
    dotenv.load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
