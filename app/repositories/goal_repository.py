from sqlalchemy.orm import Session
from app.models.goal import Goal


def get_all_goals(db: Session):
    return db.query(Goal).all()


def get_goal_by_id(db: Session, goal_id: int):
    return db.query(Goal).filter(Goal.id == goal_id).first()
