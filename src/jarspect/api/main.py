from __future__ import annotations

from fastapi import FastAPI

from jarspect.api.routes.health import router as health_router
from jarspect.api.routes.scan import router as scan_router
from jarspect.api.routes.scans import router as scans_router
from jarspect.api.routes.ui import router as ui_router
from jarspect.api.routes.ui import static_app as ui_static_app
from jarspect.api.routes.upload import router as upload_router
from jarspect.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.service_name,
        version=settings.service_version,
    )
    application.include_router(health_router)
    application.include_router(upload_router)
    application.include_router(scan_router)
    application.include_router(scans_router)
    application.include_router(ui_router)
    application.mount("/static", ui_static_app, name="ui-static")
    return application


app = create_app()
