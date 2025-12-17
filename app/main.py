from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.goal_routes import router as goal_router
from app.routes.deposit_routes import router as deposit_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Control API",
    version="1.0.0"
)


app.include_router(goal_router)
app.include_router(deposit_router)
