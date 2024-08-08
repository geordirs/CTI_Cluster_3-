from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Notification
from ..schemas import NotificationCreate, Notification as NotificationSchema
from ..auth import get_current_active_user

router = APIRouter()

@router.post("/notifications/", response_model=NotificationSchema)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/notifications/", response_model=List[NotificationSchema])
def get_user_notifications(db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    notifications = db.query(Notification).filter(Notification.user_id == current_user.id).all()
    return notifications

@router.put("/notifications/{notification_id}/read")
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    notification = db.query(Notification).filter(Notification.id == notification_id, Notification.user_id == current_user.id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    notification.is_read = True
    db.commit()
    return {"status": "success"}