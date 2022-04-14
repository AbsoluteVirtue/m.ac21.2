import json
from aiohttp import web


class Base(web.View):

    async def get(self):
        return json.dumps({"success": True})
