from fastapi import FastAPI
from app.routes import all_routes

app = FastAPI()

# Auto-load all routes
for route in all_routes:
    app.include_router(route)
