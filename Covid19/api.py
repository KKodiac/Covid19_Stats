from fastapi import FastAPI
from src.covid19_wd import CovidInfowd

app = FastAPI()

@app.get('/covid')
async def root():
    return {"message : test "}

worldCovid = CovidInfowd()
head, body = worldCovid.getData()

@app.get('/covid/world')
async def show_world_all():
    return body

@app.get('/covid/world/header')
async def show_world_header():

    return {i for i in head}

@app.get('/covid/world/{country_name}')
async def show_world_country(country_name: str):
    isFound = False
    country_name = " ".join(country_name.split('_'))

    for cnt, info in enumerate(body):
        if(info[1] == country_name):
            index = cnt
            isFound = True
            break
    if(isFound):
        return {i for i in body[cnt]}
    else:
        return {'message : Country Index not Found'}

