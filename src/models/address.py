

#Insere endereço

async def insert_address(address_collection, address):
    try:
        address = await address_collection.insert_one(address)

        if address.inserted_id:
            address = await get_address(address_collection, address.inserted_id)
            return address
    except Exception as e:
        print(f'create_user.error: {e}')
 
# Buscar endereço passando id do usuário
async def get_address_by_user(address_collection, user_id):
    data = await address_collection.find_one({"id_usuario": user_id}) 
    return data
 
# Busca se já existe endereço   
async def get_address(address_collection, address):
    address = await address_collection.find_one(address)
    return address
 


# Atualiza adicionando mais um endereço   
async def add_new_address(address_collection, address_id, address_data):
    data = {k: v for k, v in address_data.items() if v is not None}
    
    data = await address_collection.update_one(
        {"_id": address_id},
        {
            "$addToSet": {
             "address": data
            }
        }
    )
    
    return data
                                                
def delete_adress():
    ...

# Passos para criar novo endereço:
 
# * Verificar se existe algum endereço para um user, pelo model dentro de address.py, ADDRESS_USER = (address.find({"user._id": USER["_id"})),
# * Se caso não existir ainda, ADDRESS_USER = None:
# 	- chamar o método dentro do model address.insert_one({"user": {objeto_user_dicionario, "address": [{"objeto_address_dicionario"}]}});
# * Se caso já existir, ADDRESS_USER = {documento_endereco_user}
# 	- chamar o método dentro do model address.update_one(
#     {"_id": "{ADDRESS_USER._id}"},
#     {
#         "$addToSet": {
#             "address": 'novo_endereco_que_passar'
#         }
#     }
# );