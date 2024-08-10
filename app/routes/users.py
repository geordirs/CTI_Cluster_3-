from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserCreate, UserResponse
from typing import List
from ..auth import get_current_admin_user, get_password_hash

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def read_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    users = db.query(User).all()
    return users

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    # Verificar si el usuario ya existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Crear un nuevo usuario
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        is_active=True,
        is_admin=False  # Por defecto, los nuevos usuarios no son administradores
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user