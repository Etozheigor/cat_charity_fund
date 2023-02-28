from fastapi import APIRouter, Depends
from app.core.user import current_superuser, current_user
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.db import get_async_session
from app.schemas.donation import DonationCreate, DonationDB, UserDonation
from app.crud.donation import donation_crud
from app.models.user import User
from app.services.investing_process import investing_process

router = APIRouter()

@router.get(
    '/donation/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
    description='Получает список всех пожертвований.'
)
async def get_all_donations(session: AsyncSession = Depends(get_async_session)):
    """Только для суперюзеров."""
    all_donations = await donation_crud.get_multi(session)
    return all_donations

@router.post(
    '/donation/',
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
    await investing_process(new_donation, session)
    return new_donation

@router.get(
    '/donation/my/',
    response_model=List[UserDonation],
    response_model_exclude_none=True,
    description='Получить список моих пожертвований.'
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)):
    user_donations = await donation_crud.get_user_donations(session=session, user=user)
    return user_donations