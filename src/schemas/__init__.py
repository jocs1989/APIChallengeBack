from pydantic import BaseModel, Field, ConfigDict

from typing import Optional, Union

import uuid


class BaseConfig(BaseModel):
    entityId: Optional[Union[str, int]] = Field(None, description="""
    Identificador unico de cada usuario a consultar, el entityId ayuda a diferenciar un usuario de otro.
    
    En el caso que no se proveea un entityId, se generará uno automaticamente basado en un UUID v4.
    """)
    entityType: Optional[str] = Field("externalUser", description="""Describe el origen del usuario, por defecto es externalUser.""")
    model_config = ConfigDict(populate_by_name=True)
    