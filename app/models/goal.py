from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.core.database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    target_value = Column(Float, nullable=False)
    total_deposits = Column(Integer, nullable=False)
    final_value = Column(Float, nullable=False)

    deposits = relationship("Deposit", backref="goal")
