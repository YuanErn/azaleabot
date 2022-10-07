from turtle import color
import hikari
import lightbulb
import discord
import turtle

#tokenfile
tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

#guildfile
guildFile = open('GUILDS', 'r')
guilds  = guildFile.readline()
guildFile.close()

#initialisation
bot = lightbulb.BotApp(
    token, 
    guilds
    )

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.command
@lightbulb.command('socials', 'Displays the socials')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    embed = discord.Embed(title="Socials!", description="Here are the socials", color= turtle.color( (0x60, 7d, 8b) ))
    embed.add_field(name="Instagram", value="Ig link here")
    embed.add_field(name="Facebook", value="Fb link here")
    embed.add_field(name="Twitter", value="Tw link here")

    await ctx.respond(embed = embed)

bot.run()
