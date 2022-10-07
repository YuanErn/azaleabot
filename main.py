import hikari

#hiding token
tokenFile = open('TOKEN', r)
token = tokenFile.readline()
tokenFile.close()

bot = hikari.GatewayBot(token)
bot.run()
