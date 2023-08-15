from fastapi import APIRouter

from models.common import Response
from models.user import User
from services.user_services import UserServices

router = APIRouter()
user_service = UserServices()


@router.post("", response_model=Response)
async def create_new_user(user: User):
    try:
        user = await user_service.create_user(user)
        return Response(success=True, message="user created successfully", data=user)
    except Exception as e:
        return Response(success=False, message=str(e))


@router.get("", response_model=Response)
async def get_all_users():
    try:
        users = await user_service.get_users()
        return Response(success=True, message="users retrieved successfully", data=users)
    except Exception as e:
        return Response(success=False, message=str(e))


@router.get("/{email}", response_model=Response)
async def get_user_by_email(email: str):
    try:
        user = await user_service.get_user_by_email(email=email)
        return Response(success=True, message="user retrieved successfully", data=user)
    except Exception as e:
        return Response(success=False, message=str(e))


@router.put("", response_model=Response)
async def update_user(user: User):
    try:
        user = await user_service.update_user(new_user=user)
        return Response(success=True, message="user updated successfully", data=user)
    except Exception as e:
        return Response(success=False, message=str(e))


@router.delete("/{email}", response_model=Response)
async def delete_user(email: str):
    try:
        user = await user_service.delete_user(email=email)
        return Response(success=True, message="user deleted successfully")
    except Exception as e:
        return Response(success=False, message=str(e))
