from sqlalchemy.orm import Session
from app.repositories.deposit_repository import (
    get_deposit_by_goal_and_number,
    update_deposit_status
)


def toggle_deposit_service(
    db: Session,
    goal_id: int,
    deposit_number: int
):
    deposit = get_deposit_by_goal_and_number(
        db=db,
        goal_id=goal_id,
        number=deposit_number,
    )

    if not deposit:
        return None

    new_status = not deposit.is_paid

    return update_deposit_status(
        db=db,
        deposit=deposit,
        is_paid=new_status
    )
