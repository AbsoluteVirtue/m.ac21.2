import argparse
import asyncio
import os.path

import motor.motor_asyncio as aiomotor

import yaml
from aiohttp import web
from controllers import base


async def setup_mongo(app, loop):
    mgo = aiomotor.AsyncIOMotorClient(
        io_loop=loop, **app['config']['mongo']['kwargs'])[app['config']['mongo']['db']]

    async def close_mongo():
        mgo.client.close()

    app.on_cleanup.append(close_mongo)

    return mgo


def setup_routes(app):
    app.router.add_view(r'/', name='home', handler=base.Base)
    app.router.add_view(r'/user/{username}', name='user-id', handler=base.User)
    app.router.add_view(r'/user', name='user', handler=base.User)
    app.router.add_view(r'/auth', name='auth', handler=base.Auth)


async def close_session(app):
    app['http'].close()


def get_config(path):
    config_file = os.path.abspath(path)
    with open(config_file) as f:
        return yaml.safe_load(f)


async def make_app(config):
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app['config'] = config
    app['db'] = await setup_mongo(app, loop)

    setup_routes(app)

    return app


def init_func(argv):
    # python -m aiohttp.web discr:init_func
    return make_app(get_config('./config/local.yaml'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('--config_file', dest='config_file', default='./config/local.yaml', help='config file path')

    config = get_config(parser.parse_args().config_file)

    web.run_app(make_app(config), host=config['host'], port=config['port'],
                access_log_format='%t "%r" %s %Tf ms -ip:"%a" -ref:"%{Referer}i"')
