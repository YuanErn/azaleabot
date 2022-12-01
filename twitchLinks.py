import requests
import hikari
import lightbulb
from apscheduler.triggers.cron import CronTrigger


daily_plugin = lightbulb.Plugin("Daily")
onlineList = []

async def twitchCheck() -> None:
    streamFile = open('STREAMERS.txt', 'r')
    for x in range(4):
        channelName = streamFile.readline()
        contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

        if 'isLiveBroadcast' in contents: 
            if channelName in onlineList:
                pass

            else:
                onlineList.append
                print(channelName + ' is live')
                print(onlineList)
                
        else:
            onlineList.remove(channelName)
            print(channelName + ' is not live')

    streamFile.close()

@daily_plugin.listener(hikari.StartedEvent)
async def on_started(_: hikari.StartedEvent) -> None:
    # This event fires once, when the BotApp is fully started.
    daily_plugin.app.d.sched.add_job(twitchCheck, CronTrigger(minute="*/1"))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)

