import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from twitchLinks import onlineList

#tokenfile
tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

#initialisation
bot = lightbulb.BotApp(
    token,
    intents=hikari.Intents.ALL_UNPRIVILEGED 
    | hikari.Intents.MESSAGE_CONTENT,
    )

#Prints the text to terminal for easy debugging
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

#/socials
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
@bot.listen(hikari.GuildMessageCreateEvent)
async def handle_message(event):
    logfile = open("chatlogging.txt", "a")
    if event.content == None:
        mediaLink = event.message.attachments[0].url
        logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), (mediaLink), str(event.channel_id)))

    else:
        try:
            mediaLink = event.message.attachments[0].url
            logfile.write("{0} said| {1} |in channel:{2}, mediaAttached:{3}\n".format(str(event.author), str(event.content), str(event.channel_id), (mediaLink)))

        except IndexError:
                logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), str(event.content), str(event.channel_id)))

    logfile.close()

#Could improve the CPU usage by using push methods instead of pulling from the Twitch API every min, too lazy to change the code since it works now
#Twitch implementation
@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    # This event fires once, while the BotApp is starting.
    bot.d.sched = AsyncIOScheduler()
    bot.d.sched.start()
    bot.load_extensions("twitchLinks")

#/nowStreaming
@bot.command
@lightbulb.command("nowstreaming", "Checks for the streamers currently streaming")
@lightbulb.implements(lightbulb.SlashCommand)
async def nowStreaming(ctx):
    currentlyOnline = [':red_circle:',':red_circle:',':red_circle:',':red_circle:', ':red_circle:']
    streamerFile = open('STREAMERS', 'r')
    for streamers in range(5):
        streamCheck = streamerFile.readline().strip()   
        #we know this streamer is now online
        if streamCheck in onlineList:
            currentlyOnline[streamers] = ':green_circle:'
            print(currentlyOnline)

        else:
            pass    

    #embed for the command
    embed = hikari.Embed(title="Currently Streaming! :movie_camera:", description="Here's the list of the streamers", color=0x9b59b6)
    embed.add_field(name="{0} [baglikesbags](https://www.twitch.tv/baglikesbags)".format(currentlyOnline[0]), value="Hi, I am Gabriel, a content creator for Adrenaline and mainly enjoy playing horror, fps, and adventure. If you enjoy these genres come along and enjoy my streams in your free time!")
    embed.add_field(name="{0} [fin3sss](https://www.twitch.tv/fin3sss)".format(currentlyOnline[1]), value="desc")
    embed.add_field(name="{0} [pr0phet46](https://www.twitch.tv/pr0phet46)".format(currentlyOnline[2]), value="desc")
    embed.add_field(name="{0} [crustycorgi](https://www.twitch.tv/cru3tycorgi)".format(currentlyOnline[3]), value="desc")
    embed.add_field(name="{0} [Adrenaline Official](https://www.twitch.tv/adrenaline_esports_apac)".format(currentlyOnline[4]), value="desc")

    await ctx.respond(embed=embed)



bot.run()
