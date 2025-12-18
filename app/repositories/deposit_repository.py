from sqlalchemy.orm import Session
from app.models.deposit import Deposit


def get_deposit_by_id(db: Session, deposit_id: int):
    return db.query(Deposit).filter(Deposit.id == deposit_id).first()


def update_deposit_status(db: Session, deposit: Deposit, is_paid: bool):
    deposit.is_paid = is_paid
    db.commit()
    db.refresh(deposit)
    return deposit


def get_deposit_by_goal_and_number(
    db: Session,
    goal_id: int,
    number: int
):
    return (
        db.query(Deposit)
        .filter(
            Deposit.number == number,
            Deposit.goal_id == goal_id
        )
        .first()
    )
