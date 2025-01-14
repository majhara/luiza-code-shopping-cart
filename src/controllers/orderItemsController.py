#Controller para adição de produtos ao carrinho

from src.server.database import connect_db, db, disconnect_db
from src.models.user import get_user_by_email
from src.models.product import get_product_by_code
from src.models.order_items import insert_cart, get_cart_by_user, add_product_to_cart, update_cart, delete_cart


async def order_item_crud():
    option = input("Entre com a opção de CRUD para carrinho: ")
    
    await connect_db()
    
    users_collection = db.users_collection
    order_items_collection = db.order_items_collection 
    product_collection = db.product_collection
    
    user =  {}
    product  = {}

    if option == '1':
        user["email"] = input("Entre com email do usuário: ")
        
        user_searched = await get_user_by_email(users_collection, user("email"))
        
        if user_searched == None:
            return "Usuário não encontrado!"
        
        
        order_items_searched = await get_cart_by_user(order_items_collection, user_searched["_id"] )
        
        if order_items_searched == None:
            new_cart = insert_cart(order_items_collection, order_items_searched, user_searched["_id"])
            return new_cart
        print("O carrinho está vazio")
        
        
        product["code"] = input("Digite o código do produto a ser adicionado no carrinho: ")
        
        product_searched = await get_product_by_code(product_collection, product["code"])
        
        if product_searched == None:
            return "Produto não encontrado!"
        data = add_product_to_cart( product_searched)
    
    order: OrderSchema
    product: ProductSchema

        
        
   
    # elif option == '2':
    #     user["email"] = input("Entre com o email do usuario: ")        
    #     # get address
    #     user_searched = await get_user_by_email(users_collection, user["email"])
    #     user_addresses = await get_address_by_user(address_collection, user_searched["_id"])
    #     print(user_addresses)
        
    
    
    # elif option == '3':
    #     # update
    #     user["email"] = input("Entre com o email do usuario: ")        
    #     user_found = await get_user_by_email(users_collection,user["email"])
    #     user_modified = {}
    #     user_modified["password"] = input("Entre com a nova senha do usuario: ")              

    #     is_updated, numbers_updated = await update_user(users_collection, user_found["_id"], user_modified)
        
    #     if is_updated:
    #         print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
    #     else:
    #         print("Atualização falhou!")
    # elif option == '4':
    #     # delete
    #     user["email"] = input("Entre com o email do usuario a ser deletado: ")
    #     user_found = await get_user_by_email(users_collection, user["email"])
        
    #     is_deleted, user_found = await delete_user(users_collection, user_found["_id"])
        
    #     if is_deleted:
    #         print("Usuário deletado com sucesso!")
    #     else:
    #         print("Não foi possível realizar a operação!")

    #     # print(result)
    # elif option == '5':
    #     # pagination
    #     users = await get_users(
    #         users_collection,
    #         skip=0,
    #         limit=2
    #     )
    #     print(users)

    await disconnect_db()
