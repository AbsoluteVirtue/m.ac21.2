
async def get_user(db, username):
    return await db.users.find_one({
        '_id': username,
    })


async def insert_user(db, **kwobj):
    data = {}
    data.update(kwobj)
    return await db.users.insert_one(data)


async def update_user(db, **kwobj):
    data = {}
    data.update(kwobj)
    return await db.users.find_and_modify(
        {'_id': data.pop('username')},
        {'$set': data})
