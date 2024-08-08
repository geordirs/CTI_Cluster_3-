from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import RecommendationResponse, Product as ProductSchema
from ..services.recommendation import get_recommendations, update_recommendations

router = APIRouter()

@router.get("/products/{product_id}/recommendations", response_model=RecommendationResponse)
def get_product_recommendations(product_id: int, db: Session = Depends(get_db)):
    recommendations = get_recommendations(db, product_id)
    return RecommendationResponse(recommendations=recommendations)

@router.post("/recommendations/update", status_code=200)
def update_product_recommendations(db: Session = Depends(get_db)):
    update_recommendations(db)
    return {"message": "Recommendations updated successfully"}