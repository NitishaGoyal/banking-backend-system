from fastapi import FastAPI
from app.models.user import User
from app.database import SessionLocal, engine , Base
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
@app.get("/")
def read_root():
    return {"message":"Banking API is running!"}

