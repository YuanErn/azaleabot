import lightbulb

@bot.command
@lightbulb.command('socials', 'Displays the social media accounts')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

