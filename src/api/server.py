from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.api import shop
from src.api import carts
from src.api import shop, carts

import json
import logging
import sys
# from starlette.middleware.cors import CORSMiddleware

description = """
Shoetopia description
"""

app = FastAPI(
    title="Shoetopia",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "testName",
        "email": "testEmail",
    },
)

# TODO: add routers for each endpoint
app.include_router(shop.router)
app.include_router(carts.router)
<<<<<<< HEAD
=======

>>>>>>> 37494bac9a513dd9ae8f4f189994bdbd325e2573
# app.include_router(catalog.router)
# app.include_router(bottler.router)
# app.include_router(barrels.router)
# app.include_router(admin.router)

@app.exception_handler(exceptions.RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    logging.error(f"The client sent invalid data!: {exc}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}
    for error in exc_json:
        response['message'].append(f"{error['loc']}: {error['msg']}")

    return JSONResponse(response, status_code=422)

@app.get("/")
async def root():
    return {"message": "Welcome to Shoetopia."}