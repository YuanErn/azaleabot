import asyncio
import genshin
import hikari
import lightbulb
from apscheduler.triggers.cron import CronTrigger

daily_plugin = lightbulb.Plugin("Daily")
onlineList = []

async def autoClaim():
    cookies = {"ltuid": 25089082, "ltoken": "4P3cU29tyXw2pVSS01MukdJhvSPF16GoGi7gQJxF"}
    client = genshin.Client(cookies, game=genshin.Game.GENSHIN)

    # claim daily reward
    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        print("Daily reward already claimed")
    else:
        print(f"Claimed {reward.amount}x {reward.name}")


@daily_plugin.listener(hikari.StartedEvent)
async def on_started(_: hikari.StartedEvent) -> None:
    # This event fires once, when the BotApp is fully started.
    daily_plugin.app.d.sched.add_job(autoClaim, CronTrigger(day="*/1"))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(daily_plugin)
