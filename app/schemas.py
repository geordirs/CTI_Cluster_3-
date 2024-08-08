from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from .models import OrderStatus

class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    product_id: int

class Review(ReviewBase):
    id: int
    user_id: int
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int
    low_stock_threshold: int
    category: str
    image_url: str
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    low_stock_threshold: Optional[int] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None

class Product(ProductBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    reviews: List[Review] = []

    class Config:
        orm_mode = True

class ProductInventory(BaseModel):
    id: int
    name: str
    stock_quantity: int
    low_stock_threshold: int
    is_active: bool
    
class ProductSearch(BaseModel):
    keyword: Optional[str] = None
    search: Optional[str] = None
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    sort_by: Optional[str] = "name"
    sort_order: Optional[str] = "asc"
    page: int = 1
    items_per_page: int = 10

class ProductSearchResults(BaseModel):
    items: List[Product]
    total: int
    page: int
    size: int
    pages: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

class Config:
    from_attributes = True

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int

class CartItem(CartItemCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class CartItemUpdate(BaseModel):
    quantity: int

class Cart(BaseModel):
    items: List[CartItem]
    total: float

class CouponBase(BaseModel):
    code: str
    discount_percent: float
    valid_from: datetime
    valid_to: datetime

class CouponCreate(CouponBase):
    pass

class Coupon(CouponBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class CouponApply(BaseModel):
    code: str

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItem(OrderItemCreate):
    id: int
    price: float

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

    coupon_code: Optional[str] = None

class Order(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total_amount: float
    items: List[OrderItem]

    class Config:
        from_attributes = True

class RecommendationBase(BaseModel):
    recommended_product_id: int
    score: float

class Recommendation(RecommendationBase):
    id: int
    product_id: int

    class Config:
        from_attributes = True

class RecommendationResponse(BaseModel):
    recommendations: List[Product]

class NotificationBase(BaseModel):
    message: str

class NotificationCreate(NotificationBase):
    user_id: int

class Notification(NotificationBase):
    id: int
    user_id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True

