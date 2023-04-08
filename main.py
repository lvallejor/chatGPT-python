import openai
import config
from typing import Union


from fastapi import FastAPI

app = FastAPI()

openai.api_key = config.api_key


@app.get("/healthcheck", status_code=200)
def read_root():
    return {"healthcheck": "ok"}


@app.post("/chatbot/", status_code=200)
async def create_chat(content: str):
    contenido = content
    print(contenido)
    response_chat = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                 messages=[{"role": "user", "content": contenido}])
    print(response_chat.choices[0].message.content)
    return {"respuesta": response_chat.choices[0].message.content}


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
