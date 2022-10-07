import lightbulb

@bot.command
@lightbulb.command('socials', 'Replies with pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

