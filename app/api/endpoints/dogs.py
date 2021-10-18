from fastapi import APIRouter, Depends
from app.api.schemas import Dogs, dogs_pd, dogsIn_pd
from app.api.crud import get_all, get_is_adopted, get_entity, update_entity, new_entity, delete_entity

from ..authentication import auth_user

dogs = APIRouter(prefix="/api/dogs", tags=["Dogs"])


@dogs.get("/")
async def all_dogs():
    return await get_all(dogs_pd, Dogs)


@dogs.get("/is_adopted")
async def adopted_dogs():
    return await get_is_adopted(dogs_pd, Dogs)


@dogs.get("/{name}")
async def dog_by_name(name: str):
    return await get_entity(name, dogs_pd, Dogs)


@dogs.post("/{name}", response_model=dogs_pd)
async def new_dog(dog: dogsIn_pd, user_id: int = Depends(auth_user)):
    return await new_entity(dog, dogs_pd, Dogs, user_id, dogs=True)


@dogs.put("/{name}")
async def update_dog(name: str, update_picture: bool, dog: dogsIn_pd):
    return await update_entity(name, dog, dogs_pd, Dogs, update_picture, dogs=True)


@dogs.delete("/{name}")
async def delete_dog(name: str):
    return await delete_entity(name, Dogs)
