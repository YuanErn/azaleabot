import hikari

tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()
bot = hikari.GatewayBot(token)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot is online")

bot.run()
