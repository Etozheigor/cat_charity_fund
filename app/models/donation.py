from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base
from .abstract_model import AbstractModel


class Donation(AbstractModel, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)