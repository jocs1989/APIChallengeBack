from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class ScraperIn(BaseModel):
    url: HttpUrl = Field(
        "https://www.tiendasjumbo.co/televisores-y-audio",  # Valor por defecto
        example="https://www.tiendasjumbo.co/televisores-y-audio"  # Ejemplo para la documentación
    )

    class Config:
        # Configuración para asegurar que las URLs sean tratadas correctamente
        json_encoders = {
            HttpUrl: lambda v: str(v)
        }