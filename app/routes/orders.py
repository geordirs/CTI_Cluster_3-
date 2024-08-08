from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models import Notification

from ..database import get_db
from ..models import Order, OrderItem, Product, Coupon
from ..schemas import OrderCreate, Order as OrderSchema
from ..auth import get_current_active_user

router = APIRouter()

@router.post("/orders/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_order = Order(user_id=current_user.id)
    
    if order.coupon_code:
        coupon = db.query(Coupon).filter(Coupon.code == order.coupon_code, Coupon.is_active == True).first()
        if coupon:
            now = datetime.utcnow()
            if now >= coupon.valid_from and now <= coupon.valid_to:
                db_order.coupon_id = coupon.id
            else:
                raise HTTPException(status_code=400, detail="Coupon is not valid at this time")
        else:
            raise HTTPException(status_code=400, detail="Invalid coupon code")

    db.add(db_order)
    db.flush()  # This assigns an id to db_order

    total_amount = 0
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        
        if product.stock_quantity < item.quantity:
            raise HTTPException(status_code=400, detail=f"Not enough stock for product {product.name}")
        
        product.stock_quantity -= item.quantity
        
        order_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price
        )
        db.add(order_item)
        total_amount += product.price * item.quantity

    if db_order.coupon:
        total_amount *= (1 - db_order.coupon.discount_percent / 100)

    db_order.total_amount = total_amount

    notification = Notification(
        user_id=current_user.id,
        message=f"Su pedido #{db_order.id} ha sido creado y está siendo procesado."
    )
    db.add(notification)

    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/orders/", response_model=List[OrderSchema])
def get_orders(db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return db.query(Order).filter(Order.user_id == current_user.id).all()

@router.get("/orders/{order_id}", response_model=OrderSchema)
def get_order(order_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order