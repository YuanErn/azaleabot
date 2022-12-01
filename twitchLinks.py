import requests
import hikari
import lightbulb
from apscheduler.triggers.cron import CronTrigger


daily_plugin = lightbulb.Plugin("Daily")
onlineList = []

async def twitchCheck() -> None:
    global onlineList 
    streamerFile = open('STREAMERS', 'r')
    for streamer in streamerFile:
        #streamer = streamerFile.readline()
        contents = requests.get('https://www.twitch.tv/' +streamer).content.decode('utf-8')

        if 'isLiveBroadcast' in contents: 
            if streamer in onlineList:
                pass

            else:
                onlineList.append(streamer)
                print(streamer + ' is live')
                print(onlineList)
        else:
            onlineList.remove(streamer)
            print(streamer + ' is not live')
    
    streamerFile.close()

@daily_plugin.listener(hikari.StartedEvent)
async def on_started(_: hikari.StartedEvent) -> None:
    # This event fires once, when the BotApp is fully started.
    daily_plugin.app.d.sched.add_job(twitchCheck, CronTrigger(minute="*/1"))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)

