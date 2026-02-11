from __future__ import annotations

from fastapi import FastAPI

from mod_sentinel.api.routes.health import router as health_router


app = FastAPI(title="Mod Sentinel")
app.include_router(health_router)
