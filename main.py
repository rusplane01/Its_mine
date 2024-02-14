from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from typing import Annotated
import sqlite3
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from datetime import datetime, timedelta

app = FastAPI()

template = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

def get_db():
    db = sesion_local()
    try:
        yield db
    finally:
        db.close()

conect = sqlite3.connect('toolsmith.db')

@app.get("/")
def read_root(request: Request):
    # Дані, які будуть передані в шаблон
    data = {"message": "Hello, World!"} 
    return template.TemplateResponse('index.html', {'request': request, "data": data})


@app.post("/company/")
def create_company(name:str, db: Session = Depends(get_db)):
    return crud.create_company(db=db, name=name)
