from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import Tortoise

from .models import Dogs,User

Tortoise.init_models(['backend.app.api.models'], 'models') 


## serialized model for Dogs
dogs_pd = pydantic_model_creator(Dogs,name='Dogs') 
dogsIn_pd = pydantic_model_creator(Dogs,name='DogsIn',exclude=('picture','user_id'),exclude_readonly=True) 

## serialized model for User
user_pd = pydantic_model_creator(User,name='User') 
userIn_pd = pydantic_model_creator(User,name='UserIn',exclude_readonly=True) 


