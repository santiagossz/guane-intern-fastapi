import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


from app.api.endpoints.dogs import dogs
from app.api.endpoints.users import users
from app.api.authentication import auth


config=['APP_NAME','APP_VERSION','PSQL_USER','PSQ_PSSW','PSQL_HOST','PSQL_DB']
app_name , app_version,user,pssw,host,db=[os.getenv(i) for i in config]


app = FastAPI(title=app_name,version=app_version)


register_tortoise(
    app,
    db_url=f'postgres://{user}:{pssw}@{host}/{db}',
    modules={"models": ["app.api.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
) 



@app.get("/")
async def read_root():
    return {"Status": "Working"}


app.include_router(auth)
app.include_router(users)
app.include_router(dogs)
