from db.models import Customer

def save_customer(db, customer_data):

    # Convertir Df a dict
    data_dict = customer_data.iloc[0].to_dict()

    # Instancia del Modelo

    customer = Customer(**data_dict)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer