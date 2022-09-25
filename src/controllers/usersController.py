from os import environ
from unittest import result

from src.models.user import (
    create_user,
    get_user_by_email,
    update_user,
    delete_user,
    get_users
)
from src.server.database import connect_db, db, disconnect_db


async def users_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    users_collection = db.users_collection

    user =  {}

    if option == '1':
        user["email"] = input("Entre com o email do usuario: ")
        user["password"] = input("Entre com o password do usuario: ")
        user["is_active"] = True
        user["is_admin"] = False
        # create user
        user = await create_user(users_collection, user)
        print(user)
    elif option == '2':
        user["email"] = input("Entre com o email do usuario: ")        
        # get user
        user = await get_user_by_email(users_collection,user["email"])
        print(user)
    elif option == '3':
        # update
        user["email"] = input("Entre com o email do usuario: ")        
        user_found = await get_user_by_email(users_collection,user["email"])
        user_modified = {}
        user_modified["password"] = input("Entre com a nova senha do usuario: ")              

        is_updated, numbers_updated = await update_user(users_collection, user_found["_id"], user_modified)
        
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        user["email"] = input("Entre com o email do usuario a ser deletado: ")
        user_found = await get_user_by_email(users_collection, user["email"])
        
        result = await delete_user(users_collection, user_found["_id"])
        
        if result:
            print("Usuário deletado com sucesso!")
        else:
            print("Não foi possível realizar a operação!")

    elif option == '5':
        # pagination
        users = await get_users(
            users_collection,
            skip=0,
            limit=2
        )
        print(users)

    await disconnect_db()
