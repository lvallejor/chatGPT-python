import openai
import config
from typing import Union


from fastapi import FastAPI

app = FastAPI()

openai.api_key = config.api_key

# Healtcheck smoke test


@app.get("/healthcheck", status_code=200)
def read_root():
    return {"healthcheck": "ok"}


# ChatBot ChatGPT
@app.post("/chatbot/", status_code=200)
async def create_chat(content: str):
    contenido = content
    print(contenido)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "user", "content": contenido}])
    response_chat = response.choices[0].message.content
    print(response_chat)
    return {"respuesta": response_chat}


# Dall-E
@app.post("/imagen/", status_code=201)
async def create_image(content: str):
    contenido = content
    print(contenido)
    response_dallE = openai.Image.create(
        prompt=contenido,
        n=1,
        size="512x512"
    )
    image_url = response_dallE['data'][0]['url']
    print(image_url)
    return {"Imagen": image_url}


# ChatBot & Dall-E
@app.post("/chat-image/", status_code=200)
async def create_chat_image(content: str):
    contenido = content
    print(contenido)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "user", "content": contenido}])
    response_chat = response.choices[0].message.content
    print(response_chat)
    response_dallE = openai.Image.create(
        prompt=contenido,
        n=1,
        size="512x512"
    )
    image_url = response_dallE['data'][0]['url']
    print(image_url)
    return {"Respuesta": response_chat, "Imagen": image_url}
