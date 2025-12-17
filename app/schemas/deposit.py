from pydantic import BaseModel


class DepositResponse(BaseModel):
    id: int
    number: int
    value: float
    is_paid: bool

    class Config:
        from_attributes = True


class DepositUpdate(BaseModel):
    is_paid: bool
