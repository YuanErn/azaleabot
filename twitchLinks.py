import requests
import hikari
import lightbulb
from apscheduler.triggers.cron import CronTrigger


daily_plugin = lightbulb.Plugin("Daily")

async def twitchCheck() -> None:
    channelName = '39daph'

    contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

    if 'isLiveBroadcast' in contents: 
        print(channelName + ' is live')
    else:
        print(channelName + ' is not live')

@daily_plugin.listener(hikari.StartedEvent)
async def on_started(_: hikari.StartedEvent) -> None:
    # This event fires once, when the BotApp is fully started.
    daily_plugin.app.d.sched.add_job(twitchCheck, CronTrigger(minute="*/1"))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)
