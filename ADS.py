import hikari 
import lightbulb
import json
import openai

secret_file = open("API.txt", "r")
openai.api_key = secret_file.readline()
secret_file.close()

def check_content(content):
    response = openai.Moderation.create(
    model = "text-moderation-stable",
    input = content
    )

    categoryScores = json.loads(response["results"][0]["category_scores"])



    return categoryScores[0][0]