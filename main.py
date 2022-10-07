import lightbulb
import hikari

tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

bot = lightbulb.BotApp(token, default_enabled_guilds = (999584580019441728))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print ('Bot has started')

@bot.command
@lightbulb.command('Ping', 'Replies with pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


bot.run()
