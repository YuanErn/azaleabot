import hikari 
import lightbulb
import openai

secret_file = open("API.txt", "r")
openai.api_key = secret_file.readline()
secret_file.close()

def check_content(content):
    response = openai.Moderation.create(
    model = "text-moderation-stable",
    input = content
    )

    categories = response["results"][0]["category_scores"]
    for category in categories:
        if category > 0.1:
            flagged = True

    return categories, flagged