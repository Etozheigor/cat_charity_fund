from app.crud.base import CRUDBase
from app.models import Donation, User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from datetime import datetime


class DonationCrud(CRUDBase):
    
    async def get_user_donations(self, session: AsyncSession, user: User):
        user_donations = await session.execute(select(Donation).where(Donation.user_id == user.id))
        return user_donations.scalars().all()


donation_crud = DonationCrud(Donation) 