import hikari
import lightbulb


tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

bot = lightbulb.BotApp(token, default_enabled_guilds = (999584580019441728))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    await event.respond('Bot has started!')

@bot.command
@lightbulb.command('ping', 'Replies with pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

bot.run()
