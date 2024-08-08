from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db, engine, Base
from .routes import products, auth, cart, orders, reviews, recommendations, coupons, notifications

app = FastAPI(
    title="Ecommerce API",
    description="API for an e-commerce platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configuración de CORS
origins = [
    "http://localhost:3000",  # Asume que tu frontend está corriendo en el puerto 3000
    "http://localhost:8080",
    "http://localhost:7000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Inicializar la base de datos
init_db()

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

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