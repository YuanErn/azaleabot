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

    categoryScores = response["results"][0]["category_scores"]


    return categoryScores