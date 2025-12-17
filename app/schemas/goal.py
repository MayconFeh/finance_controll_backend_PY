from pydantic import BaseModel
from typing import List
from app.schemas.deposit import DepositResponse


class GoalResponse(BaseModel):
    id: int
    name: str
    target_value: float
    total_deposits: int
    final_value: float
    deposits: List[DepositResponse]

    class Config:
        from_attributes = True
