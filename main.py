import openai
import config
from typing import Union

from fastapi import FastAPI

app = FastAPI()

openai.api_key = config.api_key


@app.get("/healthcheck", status_code=200)
def read_root():
    return {"healthcheck": "ok"}


@app.post("/chatbot/", status_code=201)
async def create_chat(content: str):
    contenido = content
    print(contenido)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "user", "content": contenido}])
    print(response.choices[0].message.content)
    return {"respuesta": response.choices[0].message.content}


# response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
 #                                       messages=[{"role": "user", "content": "Que es el Banco BCI"}])

# print(response.choices[0].message.content)
