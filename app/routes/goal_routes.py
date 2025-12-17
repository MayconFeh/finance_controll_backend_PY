from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.schemas.goal import GoalResponse
from app.services.goal_service import (
    create_goal_service,
    list_goals_service,
    get_goal_with_deposits_service
)

router = APIRouter(prefix="/goals", tags=["Goals"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_goal(name: str, target_value: float, db: Session = Depends(get_db)):
    goal = create_goal_service(db, name, target_value)
    return {
        "message": "Meta criada com sucesso",
        "goal_id": goal.id,
        "total_deposits": goal.total_deposits,
        "final_value": goal.final_value
    }


@router.get("/", response_model=List[GoalResponse])
def list_goals(db: Session = Depends(get_db)):
    return list_goals_service(db)


@router.get("/{goal_id}", response_model=GoalResponse)
def get_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = get_goal_with_deposits_service(db, goal_id)

    if not goal:
        raise HTTPException(status_code=404, detail="Meta não encontrada")

    return goal
