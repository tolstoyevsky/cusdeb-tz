# Copyright (C) 2020 Vladislav Yarovoy. All Rights Reserved.
# Copyright (C) 2020 Denis Gavrilyuk. All Rights Reserved.
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

"""Bread and butter of the service. """

import os
import time

from cdtz import config


def list_time_zones():
    """Returns all available tzfile(5) files in the zoneinfo database. """

    time_zones = []
    excluded = [
        # There's not much information about it, but it seems the SystemV
        # time-zone IDs are old and deprecated.
        'SystemV',
        # The zoneinfo database might contain two separate databases called 'posix' and 'right'
        # (see https://mm.icann.org/pipermail/tz/2015-February/022024.html for details).
        'posix',
        'right',
    ]

    for dirpath, dirnames, filenames in os.walk(config.ZONEINFO_DATABASE):
        dirnames[:] = [dirname for dirname in dirnames if dirname not in excluded]
        if dirpath[len(config.ZONEINFO_DATABASE):] in excluded:
            continue

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if open(filepath, 'rb').read(4) == b'TZif':
                time_zone = filepath[len(config.ZONEINFO_DATABASE):]
                if time_zone not in ['Factory', 'Riyadh8'] and time_zone[0].isupper():
                    time_zones.append(time_zone)

    time_zones.sort()

    return time_zones


def set_time_zone(time_zone):
    """Sets the current time zone. """

    time_zones = list_time_zones()
    if time_zone not in time_zones:
        raise ValueError(f'Incorrect timezone setting: {time_zone}')

    os.environ['TZ'] = time_zone
    time.tzset()
