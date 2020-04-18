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

"""Module allowing configuration of the service via the environment variables. """

import os

HOST = os.getenv('HOST', 'localhost')

PORT = os.getenv('PORT', '8006')

ZONEINFO_DATABASE = os.path.join(os.getenv('ZONEINFO_DATABASE', '/usr/share/zoneinfo/'), '')
