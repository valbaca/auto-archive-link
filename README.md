# Auto Archive Link

A simple discord bot that provides archive.is links for urls

If a link is posted that matches the [specified domains](), then prepends `https://archive.is/newest/` to the URL and posts it: `https://archive.is/newest/{original_url}` like https://archive.is/newest/http://www.example.com/

OR the bot can be manually invoked with !archive

## TODO

- [ ] Provide a way for people to react / reply and have a domain be added to the *specified domains*

## Deploying

`fly deploy --ha=false`

- `--ha=false` ensures only ONE machine is running (so you don't get multiple bot replies!) (ha = high availability)

It pulls DISCORD_TOKEN from Fly.io Secrets