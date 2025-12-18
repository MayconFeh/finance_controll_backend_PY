from sqlalchemy.orm import Session
from app.repositories.deposit_repository import (
    get_deposit_by_goal_and_number,
    update_deposit_status
)


def toggle_deposit_service(
    db: Session,
    goal_id: int,
    deposit_number: int,
    is_paid: bool
):
    deposit = get_deposit_by_goal_and_number(
        db=db,
        goal_id=goal_id,
        number=deposit_number
    )

    if not deposit:
        return None

    return update_deposit_status(db, deposit, is_paid)
