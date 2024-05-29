from pydantic import BaseModel
from typing import Optional
from typing import ClassVar

# ----------------------------------------------------------------------
# Clases Obtener planes en DB
# ----------------------------------------------------------------------

class first_structure_get_all_plans(BaseModel):
    """Estructura superior de la consulta ."""
    api_key:str

