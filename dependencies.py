from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
from auth import *
from database import get_db

db_dependency = Annotated[AsyncSession, Depends(get_db)]
token_dependency = Annotated[str, Depends(oauth2_scheme)]


async def get_current_user(
    token: token_dependency,
    db: db_dependency,
) -> models.User:
    user_id = verify_access_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        user_id_int = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    result = await db.execute(
        select(models.User).where(models.User.id == user_id_int),
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


current_user_dependency = Annotated[models.User, Depends(get_current_user)]
