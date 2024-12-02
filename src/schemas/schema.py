from pydantic import BaseModel, Field
from typing import Optional


class Usuario(BaseModel):
    nombre: str
    