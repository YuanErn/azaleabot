import requests
import hikari
import lightbulb
from apscheduler.triggers.cron import CronTrigger


daily_plugin = lightbulb.Plugin("Daily")
streamerList = ['prxd4v41', '39daph', 'bunniejin', 'sinatraa']
onlineList = []

async def twitchCheck() -> None:
    global onlineList 
    for index in range(4):
        streamer = streamerList[index]
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
    

@daily_plugin.listener(hikari.StartedEvent)
async def on_started(_: hikari.StartedEvent) -> None:
    # This event fires once, when the BotApp is fully started.
    daily_plugin.app.d.sched.add_job(twitchCheck, CronTrigger(minute="*/1"))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)

