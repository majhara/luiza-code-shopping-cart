

async def create_order(order_collection, order, order_item):
    try:
        order = await order_collection.insert_one(order)
        
        if order.inserted_id:
            order = await get_order_by_id(order_collection, order.inserted_id)
        return order
    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order_by_user_id(
    
    
)
# async def calculate_order_total_price():
#     order = await order_collection.find_one
    
async def get_order_by_id(order_collection, order_id):
    try:
        order = await order_collection.find_one({'_id': order_id})
        if order:
            return order
    except Exception as e:
        print(f'pedido não encontrado! {e}')
    