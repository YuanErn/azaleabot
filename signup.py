from http import client
import discord

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = "Here are the required signup documents!"
    embed = discord.Embed(title=message)
    await user.send(ember=embed)


