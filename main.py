import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from twitchLinks import onlineList

#tokenfile
tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

#guildfile
guildFile = open('GUILDS', 'r')
guilds  = guildFile.readline()
guildFile.close()

#initialisation
bot = lightbulb.BotApp(
    token,
    guilds
    )

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

/socials
@bot.command
@lightbulb.command('socials', 'Displays the socials')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    embed = hikari.Embed(title="Socials!", description="Here are the socials :)", color=0x9b59b6)
    embed.add_field(name="Tiktok", value="[Here is the link!](https://www.tiktok.com/@adrenaline_esports)")
    embed.add_field(name="Instagram", value="[Here is the link!](https://www.instagram.com/adll.esports)")
    embed.add_field(name="Twitter", value="[Here is the link!](https://twitter.com/ADL_Esports)")
    embed.add_field(name="Twitch", value="[Here is the link!](https://www.twitch.tv/adrenaline_esports_apac)")
    embed.add_field(name="Facebook", value="[Here is the link!](https://www.facebook.com/profile.php?id=100086242737895)")
    await ctx.respond(embed=embed)

#logs the server's chats
# @bot.listen(hikari.GuildMessageCreateEvent)
# async def handle_message(event):
#     logfile = open("chatlogging.txt", "a")
#     if event.content == None:
#         mediaLink = event.message.attachments[0].url
#         logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), (mediaLink), str(event.channel_id)))

#     else:
#         try:
#             mediaLink = event.message.attachments[0].url
#             logfile.write("{0} said| {1} |in channel:{2}, mediaAttached:{3}\n".format(str(event.author), str(event.content), str(event.channel_id), (mediaLink)))

#         except IndexError:       
#                 logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), str(event.content), str(event.channel_id)))

#     logfile.close()

# #Twitch implementation
# @bot.listen(hikari.StartingEvent)
# async def on_starting(_: hikari.StartingEvent) -> None:
#     # This event fires once, while the BotApp is starting.
#     bot.d.sched = AsyncIOScheduler()
#     bot.d.sched.start()
#     bot.load_extensions("twitchLinks")

#/nowStreaming
# @bot.command
# @lightbulb.command('nowStreaming', 'Shows the streamers currently online')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx):
#     #this means there are streamers oin
#     if len(onlineList) != 0:

    
#     await ctx.respond(embed=embed)



bot.run()
