from db.connection import session
from models.get_client import client_db


data_user =[]
def get_clients_send(data):
    data_user.clear()
    request = session.query(client_db).order_by(client_db.frame,client_db.slot,client_db.port,client_db.onu_id).all()
    if request == None:
        return "Cliente no encontrado en la db agregando en la db"
    else:
        for user in request:
            print(user.contract)
            data_user.append({
            "contract": user.contract,
            "frame": user.frame,
            "slot": user.slot,
            "port": user.port,
            "onu_id": user.onu_id,
            "olt": user.olt,
            "name_1": user.name_1,
            "name_2": user.name_2,
            "sn": user.sn,
            "plan_name": user.plan_name,
            "device": user.device,
            "spid": user.spid})

    return data_user