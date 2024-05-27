from pydantic import BaseModel
from typing import Optional
from typing import ClassVar

# ----------------------------------------------------------------------
# Clases Obtener usuario en DB
# ----------------------------------------------------------------------
class get_client(BaseModel):
    """Datos necesarios para actualizar el usuario en la db  ."""
    contract : str

class first_structure_get(BaseModel):
    """Estructura superior de la consulta ."""
    api_key:str
    data:get_client

# ----------------------------------------------------------------------
# Clases Obtener usuarios en DB TODOS
# ----------------------------------------------------------------------
