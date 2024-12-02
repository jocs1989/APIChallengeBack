from src.services.tiendas_jumbo_services import Scraper
from uuid import uuid4
import logging
from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    status,
    BackgroundTasks,
    Header,
    Request,
    FastAPI,
    UploadFile,
    File
)
from src.schemas.schema import ScraperIn
from fastapi.responses import JSONResponse
router = APIRouter()


@router.post("/tiendas_jumbo", status_code=status.HTTP_201_CREATED)
async def start(data:ScraperIn=Body(...)):
    try:

        bach_id=str(uuid4())
        result = await Scraper(url=str(data.url),bach_id=bach_id).start()
        
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")

