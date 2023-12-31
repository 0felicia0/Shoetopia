from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.api import shop, carts, users, search

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
        "name1": "Felicia Patel",
        "email1": "frpatel@calpoly.edu",
        "name2": "Hallie Christopherson",
        "email2": "halliec6@gmail.com",
        "name3": "Xander Specht",
        "email3": "afspecht@calpoly.edu",
        "name4": "Mio Nakagawa",
        "email4": "manakaga@calpoly.edu",
    },
)

# TODO: add routers for each endpoint
app.include_router(shop.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(search.router)


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