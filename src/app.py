# app
from src.api.v1.routes import router

# fastapi
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

# python
import os


load_dotenv(".env")


def get_app():
    return FastAPI(
        title="Challenge Back End Developer Scrappers",
        version="0.0.1",
        docs_url=None,
        openapi_url=None,
        redoc_url=None,
    )


app = get_app()


@app.get(path="/api/doc-json", include_in_schema=False)
def openapi_json():
    return JSONResponse(
        get_openapi(
            title=DOCS_TITLE,
            version="0.0.1",
            openapi_version="3.0.0",
            routes=app.routes,
        )
    )


@app.get(path="/api/doc", include_in_schema=False)
def docs():
    return get_swagger_ui_html(openapi_url="/api/doc-json", title=DOCS_TITLE)


VERSION_API = "/v1"
app.include_router(router, prefix=VERSION_API)


DOCS_TITLE = "Challenge Back End Developer Scrappers"
