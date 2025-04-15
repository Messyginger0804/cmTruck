from app.routes.estimate import router as estimate_router
from app.routes.feedback import router as feedback_router
from app.routes.admin import router as admin_router

all_routes = [
    estimate_router,
    feedback_router,
    admin_router,
]
