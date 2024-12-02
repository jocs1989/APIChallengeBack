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
from fastapi.responses import JSONResponse
router = APIRouter()


@router.post("/tiendas_jumbo", status_code=status.HTTP_201_CREATED)
async def start():
    try:
        bach_id=str(uuid4())
        result = await Scraper(url="https://www.tiendasjumbo.co/televisores-y-audio",bach_id=bach_id).start()
        
        return f'{result}'

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")

