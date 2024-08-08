from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import Product, OrderItem, Recommendation
from typing import List

def update_recommendations(db: Session):
    # Limpiar recomendaciones existentes
    db.query(Recommendation).delete()

    # Obtener todos los productos
    products = db.query(Product).all()

    for product in products:
        # Encontrar productos que se compraron juntos
        similar_products = db.query(
            Product.id,
            func.count(OrderItem.id).label('count')
        ).join(OrderItem).filter(
            OrderItem.order_id.in_(
                db.query(OrderItem.order_id).filter(OrderItem.product_id == product.id)
            ),
            Product.id != product.id
        ).group_by(Product.id).order_by(func.count(OrderItem.id).desc()).limit(5).all()

        # Crear recomendaciones
        for similar_product in similar_products:
            recommendation = Recommendation(
                product_id=product.id,
                recommended_product_id=similar_product.id,
                score=similar_product.count
            )
            db.add(recommendation)

    db.commit()

def get_recommendations(db: Session, product_id: int) -> List[Product]:
    recommendations = db.query(Recommendation).filter(
        Recommendation.product_id == product_id
    ).order_by(Recommendation.score.desc()).limit(5).all()

    recommended_products = [recommendation.recommended_product for recommendation in recommendations]
    return recommended_products