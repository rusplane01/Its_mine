from sqlalchemy import Boolean, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from fastapi.security import OAuth2PasswordBearer
from db.engine import Base


class DBCompany(Base):
    __tablename__ = "company"
    
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    # sec_name = Column(String(255), nullable=False)
    # img_path = Column(String, nullable="False")