# import requests
# import hikari
# import lightbulb
# from apscheduler.triggers.cron import CronTrigger

# daily_plugin = lightbulb.Plugin("Daily")
# onlineList = []

# #Retrieving the channel ID
# channelFile = open('CHANNELS' , 'r')
# channel = channelFile.readline().strip()
# channelFile.close()


# async def twitchCheck() -> None:
#     streamFile = open('STREAMERS', 'r')
#     for x in range(5):
#         channelName = streamFile.readline().strip()
#         contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

#         #this means theyre streaming
#         if 'isLiveBroadcast' in contents: 
#             #checks if we already sent the message of them streaming
#             if channelName in onlineList:
#                 pass

#             else:
#                 onlineList.append(channelName)
#                 await daily_plugin.app.rest.create_message(channel, "Hello")

#         #theyre not streaming
#         else:
#             try:
#                 onlineList.remove(channelName)

#             except:
#                 pass

#     streamFile.close()

# @daily_plugin.listener(hikari.StartedEvent)
# async def on_started(_: hikari.StartedEvent) -> None:
#     # This event fires once, when the BotApp is fully started.
#     daily_plugin.app.d.sched.add_job(twitchCheck, CronTrigger(minute="*/1"))

# def load(bot: lightbulb.BotApp) -> None:
#     bot.add_plugin(daily_plugin)

