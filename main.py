import hikari
import lightbulb
import social_ping

#tokenfile
tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

#guildfile
# guildFile = open('GUILDS', 'r')
# guilds  = guildFile.readline()
# guildFile.close()

#initialisation
bot = lightbulb.BotApp(token, default_enabled_guilds = (999584580019441728))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

# @bot.command
# @lightbulb.command('socials', 'Displays the socials')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx):
#     await ctx.respond(embed = discord.Embed(title="Socials", description="These are the socials", color= "Blue", )

bot.run()
