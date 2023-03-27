import openai
import config


openai.api_key = config.api_key

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                            messages=[{"role": "user", "content":"Que es el Banco BCI"}])

print(response.choices[0].message.content)