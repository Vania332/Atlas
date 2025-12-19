from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user  
from app.routers import client
from app.routers import deal
# импорт моделей чтобы Base.metadata видел их (если create_all)
import app.models.user

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API is running. Go to /static to see frontend."}

Base.metadata.create_all(bind=engine)  # потому что не юзаю Alembic


app.include_router(user.router)
app.include_router(client.router)
app.include_router(deal.router)

#http://127.0.0.1:8000/static/index.html 