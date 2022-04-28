import os
from aiohttp import web

from store import mgo as datastore
from utils import enc_cryptography as crypt, gen_hashlib as gen


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
                "authenticate_user": {
                    "methods": ["POST"],
                    "path": (
                        f"{self.request.scheme}://{self.request.host}{self.request.app.router['auth'].canonical}"),
                },
            },
        })


class User(web.View):

    async def get(self):
        username = self.request.match_info.get('username', None)
        if not username:
            raise web.HTTPBadRequest

        user = await datastore.get_user(self.request.app['db'], username)
        if user:
            user.update({"uid": username})

        return web.json_response({
            "success": True if user else False,
            "res": user or {
                "reason": "user not found",
            },
        })

    async def post(self):
        form = await self.request.json()
        if not (
            form.get('username')
            and form.get('email')
            and form.get('plaintext')
        ):
            return web.json_response({
                "success": False,
                "res": {"reason": "provided user data incomplete or incorrect"},
            })

        salt = os.urandom(16)
        form.update({
            "hash": gen.encrypt(form.pop('plaintext'), salt),
            "key": crypt.encrypt(salt)
        })
        res = await datastore.insert_user(self.request.app['db'], **form)

        return web.json_response({
            "success": True if res else False,
            "res": {
                "uid": form["username"],
                "hash": form["hash"],
            } if res else {
                "reason": "user already exists",
            },
        })

    async def patch(self):
        form = await self.request.json()
        if not (form and form.get('username')):
            return web.json_response({
                "success": False,
                "res": {"reason": "provided user data incomplete or incorrect"},
            })

        data = {
            'username': form['username'],
            'email': form['email'],
        }

        if form.get('plaintext'):
            salt = os.urandom(16)
            data.update({
                "hash": gen.encrypt(form.pop('plaintext'), salt),
                "key": crypt.encrypt(salt)
            })

        found, modified = await datastore.update_user(self.request.app['db'], **data)

        return web.json_response({
            "success": True if modified else False,
            "res": {
                "uid": form['username'],
                "hash": data.get("hash", ""),
            } if found else {
                "reason": "user not found",
            },
        })

    async def delete(self):
        form = await self.request.json()
        if not (form and form.get('username')):
            return web.json_response({
                "success": False,
                "res": {"reason": "provided user data incomplete or incorrect"},
            })

        res = await datastore.remove_user(self.request.app['db'], form['username'])

        return web.json_response({
            "success": True if res else False,
            "res": {
                "uid": form['username'],
            } if res else {
                "reason": "user not found",
            },
        })


class Auth(web.View):

    async def post(self):
        form = await self.request.json()
        if not (
            form and form.get('email')
            and form.get('plaintext')
        ):
            return web.json_response({
                "success": False,
                "res": {"reason": "provided user data incomplete or incorrect"},
            })

        user = await datastore.get_user(self.request.app['db'], email=form['email'], no_metadata=False)
        if not user:
            return web.json_response({
                "success": False,
                "res": {"reason": "user not found"},
            })

        return web.json_response({
            "success": gen.verify(form['plaintext'], crypt.decrypt(user['key']), user['hash']),
            "res": {
                "uid": user["_id"],
                "hash": user["hash"],
            },
        })
