from sqlalchemy import Column, Integer, Boolean, Float, ForeignKey
from app.core.database import Base


class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    is_paid = Column(Boolean, default=False)
    goal_id = Column(Integer, ForeignKey("goals.id"))
