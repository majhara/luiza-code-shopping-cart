#Controller para criação de novo pedido

from src.schemas.order import OrderSchema
from src.server.database import connect_db, db, disconnect_db
from src.models.user import get_user_by_email
from src.models.address import get_address_by_user
from src.models.order import create_order
from src.models.product import get_product_by_code
import datetime


async def order_crud():
    option = input("Entre com a opção de CRUD para carrinho: ")
    await connect_db()
    
    users_collection = db.users_collection
    order_collection = db.order_collection
    order_items_collection = db.order_items_collection 
    product_collection = db.product_collection
    address_collection = db.address_collection
    
    user =  {}
    address = {}
    product  = {}

    if option == '1':
        user["email"] = input("Entre com email do usuário: ")
        
        user_searched = await get_user_by_email(users_collection, user["email"])
        
        if user_searched == None:
            return "Usuário não encontrado!"
        
        address_searched = await get_address_by_user(address_collection, user_searched["_id"])
        
        if address_searched == None:
            print("Usuário não possui endereço cadastrado!")
            return address_searched
    
    order = OrderSchema(address=address_searched, user=user_searched, price=0) 
    order = order.dict()
    order["user"] = user_searched
    order["address"] = address_searched 
    
    
    new_order = await create_order(order_collection, order)
    
    print("Created order: ", new_order)
    
    
        
    await disconnect_db()