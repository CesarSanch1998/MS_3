from fastapi import APIRouter
from fastapi import HTTPException
from schema.model_plans import first_structure_get_all_plans
#/////////////Scripts//////////////////////////////////////////
from scripts.get_all_plans import get_plans_send
import os
from dotenv import load_dotenv

load_dotenv()
get_all_plans = APIRouter()

@get_all_plans.post("/get-all-plans-db")
def get_all_plans_db(data: first_structure_get_all_plans):
    # Api key smartolt ----------------------
    if data.api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    # response = "aceptado"
    response = get_plans_send()
    return HTTPException(status_code=202, detail=response)
