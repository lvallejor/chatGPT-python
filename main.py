from fastapi import FastAPI
import requests
from fastapi.exceptions import HTTPException
import openai
import config
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app = FastAPI()
# Agregar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
openai.api_key = config.api_key


# Healtcheck smoke test
@app.get("/healthcheck/", status_code=200)
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


# Llamada a indicadores financieros
@app.get("/indicadores/dolar", status_code=200)
async def get_dolar_observado():
    try:
        response = requests.get("https://mindicador.cl/api/")
        data = response.json()
        print(data)
        return {"value": data}
    except requests.exceptions.HTTPError as error:
        if response.status_code == 500:
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
        else:
            raise HTTPException(status_code=response.status_code, detail=error)

# Llamada a clima


@app.get("/clima/", status_code=200)
async def get_clima():
    try:
        response = requests.get(
            "https://climatologia.meteochile.gob.cl/application/productos/boletinClimatologicoDiario")
        data = response.json()
        print(data)
        return {"value": data}
    except requests.exceptions.HTTPError as error:
        if response.status_code == 500:
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
        else:
            raise HTTPException(status_code=response.status_code, detail=error)
