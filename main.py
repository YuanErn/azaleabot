import hikari
import lightbulb
import discord

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

@bot.command
@lightbulb.command('signup', 'Sends the signup form straight to your dms')
@lightbulb.implements(lightbulb.SlashCommand)
async def signup(ctx: lightbulb.Context):
    async def signupembed(ctx: lightbulb.Context):
        embed = hikari.Embed(title="Here is the signup!", description="empty for now", color=0x9b59b6)
        embed.add_field(name="Tiktok", value="[Here is the link!](https://www.tiktok.com/@adrenaline_esports)")
        embed.add_field(name="Instagram", value="[Here is the link!](https://www.instagram.com/adll.esports)")
        embed.add_field(name="Twitter", value="[Here is the link!](https://twitter.com/ADL_Esports)")
        embed.add_field(name="Twitch", value="[Here is the link!](https://www.twitch.tv/adrenaline_esports_apac)")
        embed.add_field(name="Facebook", value="[Here is the link!](https://www.facebook.com/profile.php?id=100086242737895)")
        await user.send(embed=embed)
    await ctx.respond(f"The necessary details have been sent into your DMs, good luck!")
    

bot.run()
