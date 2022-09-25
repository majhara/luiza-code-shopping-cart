# from src.models.product import get_product_by_code
from src.models.user import get_user_by_email
from src.models.product import get_product_by_code
import bson


#Criando carrinho
async def insert_cart(order_items_collection, user_id):
    order_item = await order_items_collection.insert_one({'_id': user_id})
    
    if order_item.inserted_id:
        order_item = await get_cart_by_user(order_items_collection, user_id)
        return order_item         
    
# Verifica se existe carrinho vinculado ao usuário
# Se sim, me retorne o carrinho existente
async def get_cart_by_user(order_items_collection, user_id):
    data = await order_items_collection.find_one({'_id': user_id}) 
    return data
    
async def add_product_to_cart(order_items_collection, order_item, product_id):
    data = await get_product_by_code.insert_one(
        {'_id': product_id}
        
        )
    
async def update_cart(order_items_collection, product_code, order_items_data):
    data = {k: v for k, v in order_items_data.items() if v is not None}
    
    data = await order_items_collection.update_one(
        {"code": product_code},
        {
            "$addToSet": {
             "address": data
            }
        }
    )
    
    return data
                                                
async def delete_cart(order_items_collection, order_items, user_id):
    try:
        order_item = await order_items_collection.delete_one(order_items_collection, order_items)

        if order_item.inserted_id:
            order_item = await get_cart_by_user(order_items_collection, user_id)
            return order_item
    except Exception as e:
        print(f'create_cart.error: {e}')

