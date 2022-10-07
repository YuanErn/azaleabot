import hikari

tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()
bot = hikari.GatewayBot(token)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


bot.run()
