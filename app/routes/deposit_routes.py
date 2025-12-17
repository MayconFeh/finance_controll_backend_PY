from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.deposit import DepositUpdate
from app.services.deposit_service import toggle_deposit_service

router = APIRouter(prefix="/deposits", tags=["Deposits"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.patch("/{deposit_id}")
def update_deposit(
    deposit_id: int,
    data: DepositUpdate,
    db: Session = Depends(get_db)
):
    deposit = toggle_deposit_service(db, deposit_id, data.is_paid)

    if not deposit:
        raise HTTPException(status_code=404, detail="Depósito não encontrado")

    return {
        "message": "Depósito atualizado com sucesso",
        "deposit_id": deposit.id,
        "is_paid": deposit.is_paid
    }
