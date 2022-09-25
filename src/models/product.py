



async def create_product(product_collection, product):
    try:
        product = await product_collection.insert_one(product)

        if product.inserted_id:
            product = await get_product_by_code(product_collection, product.inserted_id)
            return product

    except Exception as e:
        print(f'create_user.error: {e}')

async def get_product_by_code(product_collection, product_code):
    try:
        data = await product_collection.find_one({'code': product_code})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')

# async def get_users(users_collection, skip, limit):
#     try:
#         user_cursor = users_collection.find().skip(int(skip)).limit(int(limit))
#         users = await user_cursor.to_list(length=int(limit))
#         return users

    # except Exception as e:
    #     print(f'get_users.error: {e}')


async def update_product(product_collection, product_id, product_data):
    try:
        data = {k: v for k, v in product_data.items() if v is not None}

        product = await product_collection.update_one(
            {'_code': product_id},
            {'$set': data}
        )
        
        if product.modified_count:
            return True, product.modified_count

        return False, 0
    except Exception as e:
        print(f'update_user.error: {e}')

async def delete_product(product_collection, product_id):
    try:
        product = await product_collection.delete_one({'_id': product_id})
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_user.error: {e}')
