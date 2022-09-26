#Controller para adição de produtos ao carrinho


from src.schemas.order_item import OrderItemSchema
from src.server.database import connect_db, db, disconnect_db
from src.models.user import get_user_by_email
from src.models.product import get_product_by_code
from src.models.order_items import insert_cart, get_cart_by_user
from src.models.order import get_order_by_user_id

async def cart_crud():
    option = input("Entre com a opção de CRUD para carrinho: ")
    
    await connect_db()
    
    users_collection = db.users_collection
    order_items_collection = db.order_items_collection 
    product_collection = db.product_collection
    order_collection = db.order_collection
    
    user =  {}
    product  = {}
    order_items = {}
    
    if option == '1':
        user["email"] = input("Entre com email do usuário: ")
        
        user_searched = await get_user_by_email(users_collection, user["email"])
        
        if user_searched == None:
            print("Usuário não encontrado!")
            user_searched = user_searched.dict()
        
    order_items = await get_cart_by_user(order_items_collection, user_searched["_id"] )
        
    if order_items == None:
        order_items = await insert_cart(order_items_collection, user_searched["_id"])
        return order_items
    print("O carrinho foi criado, mas está vazio")  
    
    order_searched = await get_order_by_user_id(order_collection, user_searched["_id"])
    
    if order_searched == None:
        print("Ainda não existe um pedido associado a esse usuário")
    
    product["code"] = input("Digite o código do produto a ser adicionado no carrinho: ")
        
    product_searched = await get_product_by_code(product_collection, product["code"])
           
    if product_searched == None:
        return "Produto não encontrado!"
    
    if order_searched is not None:
        order_item = OrderItemSchema(order=order_searched, product=product_searched)
        order_item = order_item.dict()
        order_item["order"] = order_searched
        order_item["product"] = product_searched
    
        new_order = await insert_cart(order_items_collection, order_item)
    
        print("Produto inserido com sucesso: ", new_order)
    else:
        print("Erro ao inserir o produto")


    await disconnect_db()
