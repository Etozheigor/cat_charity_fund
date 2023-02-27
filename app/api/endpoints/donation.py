from fastapi import APIRouter, Depends
from app.core.user import current_superuser, current_user
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.db import get_async_session
from app.schemas.donation import DonationCreate, DonationDB, UserDonation
from app.crud.donation import donation_crud
from app.models.user import User

router = APIRouter()

@router.get(
    '/donation',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    description='Получает список всех пожертвований.'
)
async def get_all_donations(session: AsyncSession = Depends(get_async_session)):
    all_donations = await donation_crud.get_multi(session)
    return all_donations

@router.post(
    '/donation',
    response_model=UserDonation,
    response_model_exclude_none=True,
    description='Сделать пожертвование.'
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(donation, session, user)
    return new_donation

@router.get(
    '/donation/my',
    response_model=List[UserDonation],
    response_model_exclude_none=True,
    description='Получить список моих пожертвований.'
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)):
    user_donations = await donation_crud.get_user_donations(session=session, user=user)
    return user_donations