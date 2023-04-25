import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from twitchLinks import onlineList
from apscheduler.triggers.cron import CronTrigger
import openai
from ADS import check_content

# tokenfile
tokenFile = open('TOKEN', 'r')
token = tokenFile.readline()
tokenFile.close()

apiKey_file = open("API.txt", "r")
openai.api_key = apiKey_file.readline()
apiKey_file.close()

# initialisation
bot = lightbulb.BotApp(
    token,
    intents=hikari.Intents.ALL_UNPRIVILEGED 
    | hikari.Intents.MESSAGE_CONTENT,
    )

# Prints the text to terminal for easy debugging
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

daily_plugin = lightbulb.Plugin("Daily")

# Could improve the CPU usage by using push methods instead of pulling from the Twitch API every min, too lazy to change the code since it works now
# Twitch implementation
@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    # This event fires once, while the BotApp is starting.
    bot.d.sched = AsyncIOScheduler()
    bot.d.sched.start()
    bot.load_extensions("twitchLinks", "autoClaim","ADS")
    print("Bot Online!")

# logs the server's chats
@bot.listen(hikari.GuildMessageCreateEvent)
async def handle_message(event):
    logfile = open("chatlogging.txt", "a")
    if event.guild_id == 1020319387678425108:
        if event.content == None:
            mediaLink = event.message.attachments[0].url
            logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), (mediaLink), str(event.channel_id)))

        else:
            try:
                mediaLink = event.message.attachments[0].url
                logfile.write("{0} said| {1} |in channel:{2}, mediaAttached:{3}\n".format(str(event.author), str(event.content), str(event.channel_id), (mediaLink)))

            except IndexError:
                    logfile.write("{0} said| {1} |in channel:{2}\n".format(str(event.author), str(event.content), str(event.channel_id)))


    else:
        pass
    
    logfile.close()

# Content Filtering
@bot.listen(hikari.GuildMessageCreateEvent)
async def handle_message(event):
    if event.guild_id == 999584580019441728 and check_content(event.content) == True:
        await event.message.delete()
        await event.message.respond("@"+ str(event.author) + " Your message was deleted because it was flagged by the system.")

    else:
        pass


# /nowStreaming
@bot.command
@lightbulb.command("nowstreaming", "Checks for the streamers currently streaming")
@lightbulb.implements(lightbulb.SlashCommand)
async def nowStreaming(ctx):
    currentlyOnline = ['<:offlinestatus:1055690090770337842>','<:offlinestatus:1055690090770337842>','<:offlinestatus:1055690090770337842>','<:offlinestatus:1055690090770337842>', '<:offlinestatus:1055690090770337842>']
    streamerFile = open('STREAMERS', 'r')
    for streamers in range(5):
        streamCheck = streamerFile.readline().strip()   
        # we know this streamer is now online
        if streamCheck in onlineList:
            currentlyOnline[streamers] = '<:onlinestatus:1055690106377343066>'

        else:
            pass    

    # embed for the command
    embed = hikari.Embed(title="Now Streaming! :movie_camera:", description="Here's the list of the streamers", color=0x9b59b6)
    embed.add_field(name="{0} [baglikesbags] (https://www.twitch.tv/baglikesbags)".format(currentlyOnline[0]), value="Hi, I am Gabriel, a content creator for Adrenaline and mainly enjoy playing horror, fps, and adventure. If you enjoy these genres come along and enjoy my streams in your free time!")
    embed.add_field(name="{0} [fin3sss] (https://www.twitch.tv/fin3sss)".format(currentlyOnline[1]), value="My name is Brandon also known as 'Fin3Ss' (Finesse). In the year of 2022 I am 16. I am just an ordinary cool guy that plays every game and its good at it :)")
    embed.add_field(name="{0} [pr0phet46] (https://www.twitch.tv/pr0phet46)".format(currentlyOnline[2]), value="Yo my ADL peepers, come and hope on to the stream and enjoy the fun (Assuming Im not already angry from rank  heh T_T)")
    embed.add_field(name="{0} [crustycorgi] (https://www.twitch.tv/cru3tycorgi)".format(currentlyOnline[3]), value="A competitive gamer that plays too much and has a dream of one day being a successful content creator , feel free to drop by and chat.")
    embed.add_field(name="{0} [Adrenaline Official] (https://www.twitch.tv/adrenaline_esports_apac)".format(currentlyOnline[4]), value="Main channel for Adrenaline livestreams")

    await ctx.respond(embed=embed)

# /socials
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

bot.run()
