from fastapi import APIRouter
from ..schemas import User, user_pd, userIn_pd
from ..crud import get_all, get_entity, new_entity, update_entity, delete_entity


users = APIRouter(prefix="/api/users", tags=["Users"])


@users.get("/")
async def all_users():
    return await get_all(user_pd, User)


@users.get("/{name}")
async def user_by_name(name: str):
    return await get_entity(name, user_pd, User)


@users.post("/{name}", response_model=user_pd)
async def new_user(user: userIn_pd):
    return await new_entity(user, user_pd, User)


@users.put("/{name}")
async def update_user(name: str, user: userIn_pd):
    return await update_entity(name, user, user_pd, User)


@users.delete("/{name}")
async def delete_user(name: str):
    return await delete_entity(name, User)
