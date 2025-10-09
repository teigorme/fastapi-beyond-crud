from fastapi import APIRouter, Depends, HTTPException, status
from .service import UserService
from .schemas import UserCreateModel, UserModel
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession

auth_router = APIRouter()
user_service = UserService()


@auth_router.post(
    "/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data: UserCreateModel, session: AsyncSession = Depends(get_session)
):
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists"
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user
