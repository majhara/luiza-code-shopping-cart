from src.server.database import connect_db, db, disconnect_db
from src.models.product import (create_product, get_product_by_code, delete_product)



async def products_crud():
    option = input("Entre com a opção de CRUD para produto: \n1-Inserir produto / 2-Buscar produto / 3-Deletar produto: ")
    await connect_db()
    product_collection = db.product_collection
    
    product = {}
    
    if option == '1':
        product["name"] = input("Nome do produto:  ")
        product["description"] = input("Descrição do produto: ")
        product["price"] = float(input("Preço: "))
        product["image"] = input("Imagem: ")
        product["code"] = input("Code: ")
        # create user
        new_product = await create_product(product_collection, product)
        print(new_product)
        
    elif option == '2':
        product["code"] = input("Digite o código do produto: ")        
        # get product
        product_found = await get_product_by_code(product_collection, product["code"])
        print(product_found)


    elif option == '3':
        # delete
        product["code"] = input("Digite o código do produto a ser deletado: ")
        product_found = await get_product_by_code(product_collection, product["code"])
        
        result = await delete_product(product_collection, product_found["_id"])
        
        if result:
            print("Produto deletado com sucesso!")
        else:
            print("Não foi possível realizar a operação!")





    await disconnect_db()