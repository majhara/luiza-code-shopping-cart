#Controller para criação de novo pedido

from src.server.database import connect_db, db, disconnect_db
from src.models.user import get_user_by_email
from src.models.address import (insert_address, get_address_by_user, get_address)
from src.models.product import get_product_by_code

async def order_item_crud():
    
    await connect_db()
    
    users_collection = db.users_collection
    order_collection = db.order_collection
    order_items_collection = db.order_items_collection 
    product_collection = db.product_collection
    
    user =  {}
    address = {}
    product  = {}

    
    price: Decimal = Field(max_digits=10, decimal_places=2)
    paid: bool = Field(default=False)
    create: datetime.datetime = Field(default=datetime.datetime.now())
    address: Address
    authority: Optional[str] = Field(max_length=100)