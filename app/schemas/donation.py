from pydantic import BaseModel, Field, validator, root_validator, Extra
from typing import Optional
from datetime import datetime



class DonationCreate(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class UserDonation(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationCreate):
    id: int
    create_date: datetime = datetime.now()
    user_id: int
    invested_amount : Optional[int]
    fully_invested : Optional[bool]
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
 