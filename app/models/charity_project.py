from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.db import Base
from .abstract_model import AbstractModel


class CharityProject(AbstractModel, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
