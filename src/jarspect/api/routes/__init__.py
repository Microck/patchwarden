"""API route exports."""

from jarspect.api.routes.health import router as health_router
from jarspect.api.routes.scan import router as scan_router
from jarspect.api.routes.scans import router as scans_router
from jarspect.api.routes.ui import router as ui_router
from jarspect.api.routes.upload import router as upload_router

__all__ = ["health_router", "upload_router", "scan_router", "scans_router", "ui_router"]
