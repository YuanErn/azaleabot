import hikari
import lightbulb
import discord

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
    embed = hikari.Embed(title="Socials!", description="Here are the socials", color=0x0fff000)
    embed.add_field(name="Instagram", value="link")
    embed.add_field(name="Instagram", value="link")
    embed.add_field(name="Instagram", value="link")
    await ctx.respond(embed=embed)

bot.run()
