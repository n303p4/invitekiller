# invitekiller
A brutally simple, self-hostable Discord bot that deletes invite links and bans repeat
offenders. Designed for myself, but released publicly in hopes that someone else will
find it useful, too.

# How to use
`invitekiller` is intended to be self-hosted, and restricted to servers that you control
specifically. You could make a public bot out of it, but this is not recommended since
it isn't designed or optimized for that use case, and might experience slowdowns.

As part of the setup process, make sure you give `invitekiller` the necessary permissions
to do what it's designed for, as it will fail silently otherwise. You are expected to have
working knowlege of Discord's permissions system, as well as working knowledge of how to
set up a bot account on Discord. If you do not have knowledge of either, simply refer to
the official Discord help articles and documentation. A quick Google search will turn up
the results you seek.

To run `invitekiller`, you will need Python 3.5 or higher as well as `discord.py`
`rewrite`. Create a file named `oauth.txt` that contains the bot's Discord token. Then in
a terminal, run the following:

```bash
python3 -m pip install --user -U git+https://github.com/Rapptz/discord.py@rewrite
python3 invitekiller.py
```

As this bot is meant to be hosted on your server specifically, there is no additional
configuration involved, and it will indiscriminately attempt to delete any messages
that contain valid Discord invite links, as well as ban repeat offenders. If this
behavior is not to your liking, you can take a look at the code and modify it as you
see fit for your own uses.