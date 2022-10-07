import lightbulb

tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()
bot = lightbulb.BotApp(token)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print ('Bot has started')
    
bot.run()
