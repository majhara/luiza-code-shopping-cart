from bson.decimal128 import Decimal128
from src.models.user import get_user_by_email
from src.models.product import get_product_by_code

async def create_order(order_collection, order):
    try:
        order["price"] = Decimal128(order["price"])
                                    
        order = await order_collection.insert_one(order)
        
        if order.inserted_id:
            order = await get_order_by_id(order_collection, order.inserted_id)
        return order
    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order_by_user_id(order_collection, user_id):
    data = await order_collection.find_one({'user._id': user_id})
    return data
    
async def get_order_by_id(order_collection, order_id):
    try:
        order = await order_collection.find_one({'_id': order_id})
        if order:
            return order
    except Exception as e:
        print(f'ainda não existe um pedido {e}')
    