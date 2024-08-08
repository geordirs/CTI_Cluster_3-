from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import CartItem, Product
from ..schemas import CartItemCreate, CartItem as CartItemSchema, CartItemUpdate, Cart
from ..auth import get_current_active_user

router = APIRouter()

@router.post("/cart/items/", response_model=CartItemSchema)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    cart_item = CartItem(user_id=current_user.id, product_id=item.product_id, quantity=item.quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/cart/", response_model=Cart)
def get_cart(db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return {"items": cart_items, "total": total}

@router.put("/cart/items/{item_id}", response_model=CartItemSchema)
def update_cart_item(item_id: int, item_update: CartItemUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == current_user.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db_item.quantity = item_update.quantity
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/cart/items/{item_id}", status_code=204)
def remove_from_cart(item_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == current_user.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(db_item)
    db.commit()
    return {"ok": True}