from db.connection import session
from models.get_client import client_db


def get_client_send(data):
    
    request = session.query(client_db).filter(client_db.contract == data.contract).first()
    if request == None:
        return "Cliente no encontrado en la db agregando en la db"
    else:
        return {"data":{
            "contract": request.contract,
            "frame": request.frame,
            "slot": request.slot,
            "port": request.port,
            "olt": request.olt,
            "name_1": request.name_1,
            "name_2": request.name_2,
            "sn": request.sn,
            "sn": request.sn,
            "plan_name": request.plan_name,
            "spid": request.spid,
        }}