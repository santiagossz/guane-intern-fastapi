import requests
from passlib.hash import bcrypt
from fastapi import HTTPException


async def get_all(model, DB):
    return await model.from_queryset(DB.all())


async def get_is_adopted(model, DB):
    return await model.from_queryset(DB.filter(is_adopted=True))


async def get_entity(name, model, DB):
    return await model.from_queryset_single(DB.get(name=name))


async def new_entity(modelIn, model, DB, user_id=0, dogs=False):
    if dogs:
        pic = requests.get(
            'https://dog.ceo/api/breeds/image/random').json()['message']
        new_entity = await DB.create(**modelIn.dict(), picture=pic, user_id=user_id)
    else:
        new_entity = await DB.create(name=modelIn.name, age=modelIn.age,
                                     password_hash=bcrypt.hash(modelIn.password_hash))
    return await model.from_tortoise_orm(new_entity)


async def update_entity(name, modelUpd, model, DB, update_picture=False, dogs=False):
    if update_picture:
        pic = requests.get(
            'https://dog.ceo/api/breeds/image/random').json()['message']
        await DB.filter(name=name).update(**modelUpd.dict(), picture=pic)
    elif dogs:
        DB.filter(name=name).update(**modelUpd.dict())
    else:
        await DB.filter(name=name).update(name=modelUpd.name,age=modelUpd.age,
                                    password_hash=bcrypt.hash(modelUpd.password_hash))
    return await model.from_queryset_single(DB.get(name=modelUpd.name))


async def delete_entity(name, DB):
    deleted_entity = await DB.get(name=name).delete()
    if not deleted_entity:
        raise HTTPException(
            status_code=404, detail=f"Entity {name}: not found")
    return f"Deleted entity: {name}"
