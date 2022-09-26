from src.schemas.address import AddressSchema
from src.server.database import connect_db, db, disconnect_db
from src.models.user import get_user_by_email
from src.models.address import (
    insert_address, get_address_by_user, add_new_address, get_address)

async def address_crud():
    option = input("Entre com a opção de CRUD para endereço: ")
    
    await connect_db()
    
    address_collection = db.address_collection
    users_collection = db.users_collection
    
    user =  {}
    address = {}


    if option == '1':
        user["email"] = input("Entre com email do usuário: ")
        print("\nDigite o endereço do usuário:")
        
        user_searched = await get_user_by_email(users_collection, user["email"])
        
        if user_searched == None:
            return "Usuário não encontrado"
        
        address["street"] = input("Rua: ")
        address["cep"] = input("CEP: ")
        address["district"] = input("Bairro:")
        address["city"] = input("Cidade:")
        address["state"] = input("Estado: ")
        address["is_delivery"] = True   
    
        result = await get_address_by_user(address_collection, user_searched["_id"]) 
        
        if result is None:
            address_schema = AddressSchema(user=user_searched )
            address_schema.address.append(address)
            new_address = await insert_address(address_collection, address_schema.dict())
            print("Added address: ", new_address)
        else:
            is_updated = await add_new_address(address_collection, result["_id"], address)
            if is_updated:
                print( "Endereço atualizado com sucesso!")
   
    elif option == '2':
        user["email"] = input("Entre com o email do usuario: ")        
        # get address
        user_searched = await get_user_by_email(users_collection, user["email"])
        user_addresses = await get_address_by_user(address_collection, user_searched["_id"])
        print(user_addresses)
        
    
    
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
