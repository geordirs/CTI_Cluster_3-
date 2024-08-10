from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from ..database import get_db
from ..models import Product, User
from ..schemas import ProductCreate, Product as ProductSchema, ProductUpdate, ProductInventory, ProductSearch, ProductSearchResults
from ..auth import get_current_active_user, get_current_admin_user
from datetime import datetime

router = APIRouter()

@router.post("/products/", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products/", response_model=List[ProductSchema])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.is_active == True).offset(skip).limit(limit).all()
    return products

@router.get("/products/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id, Product.is_active == True).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/products/{product_id}", response_model=ProductSchema)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.is_active = False
    db.commit()
    return db_product

@router.get("/inventory/", response_model=List[ProductInventory])
def get_inventory(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    inventory = db.query(Product).all()
    return inventory

@router.put("/inventory/{product_id}", response_model=ProductInventory)
def update_inventory(product_id: int, stock_quantity: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.stock_quantity = stock_quantity
    db.commit()
    db.refresh(product)
    return product

@router.get("/low-stock/", response_model=List[ProductInventory])
def get_low_stock_products(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    low_stock_products = db.query(Product).filter(Product.stock_quantity <= Product.low_stock_threshold).all()
    return low_stock_products

@router.post("/products/search", response_model=ProductSearchResults)
def search_products(search: ProductSearch, db: Session = Depends(get_db)):
    query = db.query(Product)

    if search.keyword:
        search_filter = f"%{search.keyword}%"
        query = query.filter(Product.name.ilike(search_filter) | Product.description.ilike(search_filter))
        search_query = func.to_tsquery('english', search.keyword)
        query = query.filter(
            func.to_tsvector('english', Product.name).match(search_query) |
            func.to_tsvector('english', Product.description).match(search_query)
        )

    if search.category:
        query = query.filter(Product.category == search.category)

    if search.min_price is not None:
        query = query.filter(Product.price >= search.min_price)

    if search.max_price is not None:
        query = query.filter(Product.price <= search.max_price)

    # Sorting
    if search.sort_by == "price":
        sort_column = Product.price
    else:
        sort_column = Product.name

    if search.sort_order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    # Pagination
    total = query.count()
    pages = (total + search.items_per_page - 1) // search.items_per_page
    query = query.offset((search.page - 1) * search.items_per_page).limit(search.items_per_page)

    products = query.all()

    return ProductSearchResults(
        items=products,
        total=total,
        page=search.page,
        pages=pages
    )