import hikari
import lightbulb

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
    await ctx.respond("hello")

bot.run()
