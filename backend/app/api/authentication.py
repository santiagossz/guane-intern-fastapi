import jwt
from .schemas import User, user_pd
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


auth = APIRouter(prefix="/login")
oauth2schema = OAuth2PasswordBearer(tokenUrl='login')

ALGORITHM = "HS256"
SECRET_KEY = "437a92d34e8849acc4f7ff9d696ef87ecd8ac48e2665fa2a41cfc515afbb483b"



async def authenticate_user(name: str, password: str):
    user = await User.get(name=name)
    if user and user.verify_password(password):
        return user
    return False


@auth.post('',tags=["Login"])
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401, detail=f"Invalid name or password")
    user_obj = await user_pd.from_tortoise_orm(user)
    user_jwt = jwt.encode(
        {'id': user_obj.dict()['id']}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": user_jwt}


async def auth_user(token: str = Depends(oauth2schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('id')
    except:
        raise HTTPException(
            status_code=401, detail=f"Could not validate credentials")
    return user_id
