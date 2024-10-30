from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/habits/")
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.create_habit(db=db, habit=habit)
