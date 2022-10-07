import hikari
import lightbulb


tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

bot = lightbulb.BotApp(token, default_enabled_guilds = (999584580019441728))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.event
async def on_ready():
   await client.get_channel("enter channel id here").send("bot is online")

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
