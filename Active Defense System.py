import hikari 
import lightbulb
import openai

secret_file = open("API.txt", "r")
openai.api_key = secret_file.readline()
secret_file.close()

def check_content(content):
    response = openai.Moderation.create(
    input = content
    )

    categories = response["results"][0]["categories"]
    flagged = response["results"][0]["flagged"]

    return categories, flagged

@bot.listen(hikari.GuildMessageCreateEvent)
async def handle_message(event):
    if event.guild_id == 999584580019441728:
        if check_content(event.content).flagged == True:
            await event.message.delete()
            await event.message.respond("@" + event.author + "Your message was deleted because it was flagged by the system.")

    else:
        pass