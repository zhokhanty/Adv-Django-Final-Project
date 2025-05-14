import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_openai(messages, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
