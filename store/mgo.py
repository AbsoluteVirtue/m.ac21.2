from pymongo import errors


async def get_user(db, username):
    return await db.users.find_one({
        '_id': username,
    })


async def insert_user(db, **kwobj):
    data = {'_id': kwobj.pop('username')}
    data.update(kwobj)
    try:
        return await db.users.insert_one(data)
    except errors.DuplicateKeyError:
        return None


async def update_user(db, **kwobj):
    return await db.users.update_one(
        {'_id': kwobj.pop('username')},
        {'$set': kwobj})


async def remove_user(db, **kwobj):
    return await db.users.delete_one({'_id': kwobj.get('username', '')})
