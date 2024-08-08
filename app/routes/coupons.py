from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from ..database import get_db
from ..models import Coupon, User
from ..schemas import CouponCreate, Coupon as CouponSchema
from ..auth import get_current_active_user, get_current_admin_user

router = APIRouter()

@router.post("/coupons/", response_model=CouponSchema)
def create_coupon(coupon: CouponCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_coupon = Coupon(**coupon.dict())
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

@router.get("/coupons/", response_model=List[CouponSchema])
def get_coupons(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return db.query(Coupon).all()

@router.get("/coupons/{coupon_id}", response_model=CouponSchema)
def get_coupon(coupon_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon

@router.put("/coupons/{coupon_id}/deactivate", response_model=CouponSchema)
def deactivate_coupon(coupon_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    coupon.is_active = False
    db.commit()
    db.refresh(coupon)
    return coupon

@router.post("/coupons/validate")
def validate_coupon(coupon_code: str, db: Session = Depends(get_db)):
    coupon = db.query(Coupon).filter(Coupon.code == coupon_code, Coupon.is_active == True).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found or not active")
    now = datetime.utcnow()
    if now < coupon.valid_from or now > coupon.valid_to:
        raise HTTPException(status_code=400, detail="Coupon is not valid at this time")
    return {"valid": True, "discount_percent": coupon.discount_percent}