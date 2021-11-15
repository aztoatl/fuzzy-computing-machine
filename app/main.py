#!/usr/bin/python3
from typing import Optional

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/api/v1/")
def read_root():
    return {"msg": "Hello!! this is a small api which will give you dog facts."}


@app.get("/api/v1/dogs/all")
def get_all_dog_facts():
    response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
    print(response.text)
    return {"response": response.json()}


@app.get("/api/v1/dogs/{dog_number}")
def get_dog_facts(dog_number: int):
    response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number="+str(dog_number)+"")
    print(response.text)
    return {"response": response.json()}
