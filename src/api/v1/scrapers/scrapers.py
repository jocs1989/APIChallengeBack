from src.services.tiendas_jumbo_services import Scraper

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
        await Scraper(url="https://www.tiendasjumbo.co/televisores-y-audio").start()
        
        return f"Hola"

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")

