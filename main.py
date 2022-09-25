import asyncio

from src.controllers.usersController import users_crud
from src.controllers.addressController import address_crud
from src.controllers.productsController import products_crud
from src.controllers.cartController import cart_crud


loop = asyncio.new_event_loop()
#loop.run_until_complete(users_crud())
#loop.run_until_complete(address_crud())
#loop.run_until_complete(products_crud())
loop.run_until_complete(cart_crud())