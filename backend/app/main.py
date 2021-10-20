import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


# from .api.endpoints.dogs import dogs
# from .api.endpoints.users import users
# from .api.authentication import auth


config=['PSQL_USER','PSQ_PSSW','PSQL_HOST','PSQL_DB']
user,pssw,host,db=[os.getenv(i) for i in config]


app = FastAPI(title='GUANE TEST',version='0.1')


# register_tortoise(
#     app,
#     db_url=f'postgres://{user}:{pssw}@{host}/{db}',
#     modules={"models": ["app.api.models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# ) 



@app.get("/")
async def read_root():
    return {"Status": "Working"}


# app.include_router(auth)
# app.include_router(users)
# app.include_router(dogs)
