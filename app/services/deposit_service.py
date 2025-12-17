from sqlalchemy.orm import Session
from app.repositories.deposit_repository import (
    get_deposit_by_id,
    update_deposit_status
)


def toggle_deposit_service(db: Session, deposit_id: int, is_paid: bool):
    deposit = get_deposit_by_id(db, deposit_id)

    if not deposit:
        return None

    return update_deposit_status(db, deposit, is_paid)
