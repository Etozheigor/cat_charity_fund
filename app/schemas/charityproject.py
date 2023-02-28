from pydantic import BaseModel, Field, validator, root_validator, Extra
from typing import Optional
from datetime import datetime
from pydantic import PositiveInt



class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str
    full_amount: PositiveInt

    class Config:
        extra = Extra.forbid


class CharityProjectUpdate(CharityProjectCreate):
    name: Optional[str] = Field(..., min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]




class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False
    create_date: Optional[datetime]
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
 



