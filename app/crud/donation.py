from app.crud.base import CRUDBase
from app.models.donation import Donation
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.models.user import User
from datetime import datetime


class DonationCrud(CRUDBase):
    async def create(self, obj_in, session: AsyncSession, user: Optional[User] = None):
        obj_in_data = obj_in.dict()
        obj_in_data['create_date'] = datetime.now()
        if user is not None:
            obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
    
    async def get_user_donations(self, session: AsyncSession, user: User):
        user_donations = await session.execute(select(Donation).where(Donation.user_id == user.id))
        return user_donations.scalars().all()


donation_crud = DonationCrud(Donation) 