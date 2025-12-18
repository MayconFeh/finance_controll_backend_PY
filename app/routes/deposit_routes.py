from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.deposit import DepositUpdate
from app.services.deposit_service import toggle_deposit_service

router = APIRouter(prefix="/goals", tags=["Deposits"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.patch("/{goal_id}/deposits/{deposit_number}")
def update_deposit(
    goal_id: int,
    deposit_number: int,
    data: DepositUpdate,
    db: Session = Depends(get_db)
):
    deposit = toggle_deposit_service(
        db=db,
        goal_id=goal_id,
        deposit_number=deposit_number,
        is_paid=data.is_paid
    )

    if not deposit:
        raise HTTPException(
            status_code=404,
            detail="Depósito não encontrado"
        )

    return {
        "message": "Depósito pago com sucesso",
        "goal_id": goal_id,
        "deposit_number": deposit_number,
        "is_paid": deposit.is_paid
    }
