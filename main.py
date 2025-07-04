import dotenv
import os
import discord
from discord.ext import commands

description = """
A simple discord bot that provides archive.is links for urls
"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", description=description, intents=intents)

prefix = "https://archive.is/newest/"


@bot.command()
async def archive(ctx, url: str):
    await ctx.send(prefix + url)


def main():
    dotenv.load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
