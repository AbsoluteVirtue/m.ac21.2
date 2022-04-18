from aiohttp import web

from store import mgo as datastore

class Base(web.View):

    async def get(self):
        return web.json_response({
            "success": True,
            "routes": {
                "user": {
                    "methods": ["GET"],
                    "path": (
                        f"{self.request.scheme}://{self.request.host}{self.request.app.router['user'].canonical}"),
                },
                "modify": {
                    "methods": ["POST", "PATCH", "DELETE"],
                    "path": (
                        f"{self.request.scheme}://{self.request.host}{self.request.app.router['user.id'].canonical}"),
                },
            },
        })


class User(web.View):

    async def get(self):
        user = await datastore.get_user(self.request.app['db'], self.request.match_info['username'])
        return web.json_response({
            "success": True if user else False,
            "res": user or {},
        })

    async def post(self):
        res = None
        form = await self.request.post()
        if (form.get('username')
            and form.get('email')
        ):
            res = await datastore.insert_user(self.request.app['db'], **{
                'username': form['username'],
                'email': form['email'],
            })

        return web.json_response({
            "success": True if res else False,
            "res": res or {},
        })

    async def patch(self):
        res = None
        form = await self.request.post()
        if (form and form.get('username')):
            res = await datastore.update_user(self.request.app['db'], **{
                'username': form['username'],
                'email': form['email'],
            })

        return web.json_response({
            "success": True if res else False,
            "res": res or {},
        })

    async def delete(self):
        res = None
        form = await self.request.post()
        if (form.get('username')):
            res = await datastore.update_user(self.request.app['db'], **{
                'username': form['username'],
                '_inactive_': True,
            })

        return web.json_response({
            "success": True if res else False,
            "res": res or {},
        })
