import argparse
import os.path
import yaml
from aiohttp import web
from controllers import base


def setup_routes(app):
    app.router.add_view(r'/', handler=base.Base)


async def close_session(app):
    app['http'].close()


def get_config(path):
    config_file = os.path.abspath(path)
    with open(config_file) as f:
        config = yaml.safe_load(f)

    return config


if __name__ == '__main__':
    app = web.Application()

    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('--config_file', dest='config_file', default='./config/local.yaml', help='config file path')

    path = parser.parse_args().config_file

    app['config'] = get_config(path)

    setup_routes(app)

    web.run_app(app, host=app['config']['host'], port=app['config']['port'],
                access_log_format='%t "%r" %s %Tf ms -ip:"%a" -ref:"%{Referer}i"')
