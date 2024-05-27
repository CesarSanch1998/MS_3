from fastapi import APIRouter
from fastapi import HTTPException
from schema.model_client import first_structure_get
#/////////////Scripts//////////////////////////////////////////
from scripts.get_all_clients_db_request import get_clients_send
import os
from dotenv import load_dotenv

load_dotenv()
get_all_clients = APIRouter()

@get_all_clients.post("/get-all-clients-db")
def get_all_clients_db(data: first_structure_get):
    # Api key smartolt ----------------------
    if data.api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    # response = "aceptado"
    response = get_clients_send(data.data)
    return HTTPException(status_code=202, detail=response)
