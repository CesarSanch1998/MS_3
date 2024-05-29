from db.connection import session
from models.get_plans import plans_db


data_plans =[]
def get_plans_send():
    data_plans.clear()
    request = session.query(plans_db).order_by(plans_db.plan_name).all()
    if request == None:
        return "Planes no existen en la db"
    else:
        for plans in request:
            print(plans.plan_name)
            data_plans.append({
            "plan_name": plans.plan_name,
            "plan_idx": plans.plan_idx,
            "srv_profile": plans.srv_profile,
            "line_profile": plans.line_profile,
            "gem_port": plans.gem_port,
            "provider": plans.provider,
            "vlan": plans.vlan})

    return data_plans