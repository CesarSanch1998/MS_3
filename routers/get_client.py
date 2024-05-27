from fastapi import APIRouter
from fastapi import HTTPException
from schema.model_client import first_structure_get
#/////////////Scripts//////////////////////////////////////////
from scripts.get_client_db_request import get_client_send
import os
from dotenv import load_dotenv

load_dotenv()
get_client = APIRouter()

@get_client.post("/get-client-db")
def get_client_db(data: first_structure_get):
    # Api key smartolt ----------------------
    if data.api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    # response = "aceptado"
    response = get_client_send(data.data)
    return HTTPException(status_code=202, detail=response)
