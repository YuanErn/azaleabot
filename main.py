import hikari
import lightbulb
import discord
import asyncio

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

PLATFORMS = {
    "Instagram": "ig",
    "Facebook": "🐱",
    "Twitter": "🐼",
    "Twitch": "🦊",
}

@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def social_group(ctx):
    pass

@social_group.child
@lightbulb.command("socials", "Get the link to the socials")
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def platform_subcommand(ctx: lightbulb.Context) -> None:
    select_menu = (
        ctx.bot.rest.build_action_row()
        .add_select_menu("platform_select")
        .set_placeholder("Pick a platform")
    )

    for name, emoji in PLATFORMS.items():
        select_menu.add_option(
            name,  # the label, which users see
            name.lower().replace(" ", "_"),  # the value, which is used by us later
        ).set_emoji(emoji).add_to_menu()

    resp = await ctx.respond(
        "Pick a platform from the dropdown :3",
        component=select_menu.add_to_container(),
    )
    msg = await resp.message()

    try:
        event = await ctx.bot.wait_for(
            hikari.InteractionCreateEvent,
            timeout=60,
            predicate=lambda e: isinstance(e.interaction, hikari.ComponentInteraction)
            and e.interaction.user.id == ctx.author.id
            and e.interaction.message.id == msg.id
            and e.interaction.component_type == hikari.ComponentType.SELECT_MENU,
        )
    except asyncio.TimeoutError:
        await msg.edit("The menu timed out :c", components=[])
    else:
        platform = event.interaction.values[0]
        await msg.edit(
            f"Here's the link to our {platform} page for you! :3", embed=embed, components=[]
        )

bot.run()
