#!/usr/bin/env python3

"""A simple Discord bot that deletes invite links and bans repeat offenders."""

import re

import discord

REGEX_URL = r'https?://[^\s<>"]+|www\.[^\s<>"]+'

client = discord.Client()
repeat_offenders = []  # This list keeps track of repeat offenders.


@client.event
async def on_message(message):
    """When people post invite links, deal with them accordingly."""
    message_urls = re.findall(REGEX_URL, message.content)
    for url in message_urls:
        if await client.get_invite(url):
            await message.delete()
            # Give the offender a warning first.
            # If they're a repeat offender, then ban them.
            if message.author.id in repeat_offenders:
                response = ("{0}, you were warned. See you later."
                            "").format(message.author.mention)
                await message.channel.send(response)
                await message.channel.guild.ban(message.author)
            else:
                response = ("{0}, please do not post invite links."
                            "").format(message.author.mention)
                await message.channel.send(response)
                repeat_offenders.append(message.author.id)
            break

if __name__ == "__main__":
    # Read token from oauth.txt.
    with open("oauth.txt") as file_object:
        TOKEN = file_object.read().strip("\n")
    client.run(TOKEN)
