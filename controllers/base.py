from pickle import NONE
from aiohttp import web

from store import mgo as datastore


class Base(web.View):

    async def get(self):
        return web.json_response({
            "success": True,
            "res": {
                "modify_user": {
                    "methods": ["POST", "PATCH", "DELETE"],
                    "path": (
                        f"{self.request.scheme}://{self.request.host}{self.request.app.router['user'].canonical}"),
                },
                "get_user": {
                    "methods": ["GET"],
                    "path": (
                        f"{self.request.scheme}://{self.request.host}{self.request.app.router['user-id'].canonical}"),
                },
            },
        })


class User(web.View):

    async def get(self):
        username = self.request.match_info.get('username', None)
        if not username:
            raise web.HTTPBadRequest

        user = await datastore.get_user(self.request.app['db'], username)
        return web.json_response({
            "success": True if user else False,
            "res": user or {},
        })

    async def post(self):
        res = None
        form = await self.request.json()
        if (form.get('username')
            and form.get('email')
        ):
            res = await datastore.insert_user(self.request.app['db'], **{
                'username': form['username'],
                'email': form['email'],
            })

        return web.json_response({
            "success": True if res else False,
            "res": {
                "uid": res.inserted_id,
                "hpw": "123",
            } if res else {},
        })

    async def patch(self):
        res = None
        form = await self.request.json()
        if (form and form.get('username')):
            res = await datastore.update_user(self.request.app['db'], **{
                'username': form['username'],
                'email': form['email'],
            })

        return web.json_response({
            "success": True if res and res.modified_count else False,
            "res": {
                "uid": form['username'],
            } if res and res.matched_count else {},
        })

    async def delete(self):
        res = None
        form = await self.request.json()
        if (form.get('username')):
            res = await datastore.remove_user(self.request.app['db'], **form)

        return web.json_response({
            "success": True if res and res.deleted_count else False,
            "res": {
                "uid": form['username'],
            } if res and res.deleted_count else {},
        })
