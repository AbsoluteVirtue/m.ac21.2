import json
from aiohttp import web


class Base(web.View):

    async def get(self):
        return web.json_response({"success": True})
