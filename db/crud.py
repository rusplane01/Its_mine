from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import os


# def get_author_books(db: Session, author_id: int):
    # return db.query(models.DBBook).filter(models.DBBook.author_id == author_id).all()
