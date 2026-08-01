from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth import oauth2_scheme, get_current_user
from models import User
from database import get_db

db_dependency = Annotated[AsyncSession, Depends(get_db)]
token_dependency = Annotated[str, Depends(oauth2_scheme)]
current_user_dependency = Annotated[User, Depends(get_current_user)]
