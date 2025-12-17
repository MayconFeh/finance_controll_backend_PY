from sqlalchemy.orm import Session

from app.models.goal import Goal
from app.models.deposit import Deposit


def create_goal_service(db: Session, name: str, target_value: float):
    """
    Cria uma meta e gera os depósitos automaticamente
    Ex: target_value = 20000 -> gera depósitos 1..200
    """
    deposits = []
    total = 0
    number = 1

    while total < target_value:
        deposits.append(
            Deposit(
                number=number,
                value=number,
                is_paid=False
            )
        )
        total += number
        number += 1

    goal = Goal(
        name=name,
        target_value=target_value,
        total_deposits=len(deposits),
        final_value=total
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    for deposit in deposits:
        deposit.goal_id = goal.id
        db.add(deposit)

    db.commit()

    return goal


def list_goals_service(db: Session):
    return db.query(Goal).all()


def get_goal_with_deposits_service(db: Session, goal_id: int):
    return db.query(Goal).filter(Goal.id == goal_id).first()
