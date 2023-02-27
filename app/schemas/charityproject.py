from pydantic import BaseModel, Field, validator, root_validator, Extra
from typing import Optional
from datetime import datetime



class CharityProjectCreateUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str
    full_amount: int = Field(..., gt=0)

    class Config:
        extra = Extra.forbid

    # @validator('full_amount')
    # def validate_full_amount(cls, value: int):
    #     if value < 1:
    #         raise ValueError('Сумма сбора не может быть меньше 1')
    #     return value


class CharityProjectDB(CharityProjectCreateUpdate):
    id: int
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False
    create_date: Optional[datetime]
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
 



