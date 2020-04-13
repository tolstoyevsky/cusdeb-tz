# Copyright (C) 2020 Vladislav Yarovoy. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Server-side of CusDeb Tz. """

from aiohttp import web

from cdtz import config, list_time_zones

TIME_ZONES = []


async def get_list_tz(_request):
    """Returns a comprehensive list of time zones. """

    return web.json_response(TIME_ZONES)


async def main():
    """The main entry point. """

    app = web.Application()
    app.router.add_get('/tz/list_time_zones', get_list_tz)
    return app


if __name__ == '__main__':
    TIME_ZONES = list_time_zones()
    web.run_app(main(), host=config.HOST, port=config.PORT)
