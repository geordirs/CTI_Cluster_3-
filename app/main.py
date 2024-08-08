from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .database import init_db, engine, Base
from .routes import products, auth, cart, orders, reviews, recommendations, coupons, notifications
import os


app = FastAPI(
    title="Ecommerce API",
    description="API for an e-commerce platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Inicializar la base de datos
@app.on_event("startup")
async def startup_event():
    init_db()

# Crear tablas en la base de datos
#Base.metadata.create_all(bind=engine)


# Incluir las rutas de productos
app.include_router(auth.router, tags=["authentication"])
app.include_router(products.router, tags=["products"])
app.include_router(cart.router, tags=["cart"])
app.include_router(orders.router, tags=["orders"])
app.include_router(reviews.router, tags=["reviews"])
app.include_router(recommendations.router, tags=["recommendations"])
app.include_router(coupons.router, tags=["coupons"])
app.include_router(notifications.router, tags=["notifications"])

@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API "}

#Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ecommerce API",
        version="1.0.0",
        description="This is an API for an e-commerce platform",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

