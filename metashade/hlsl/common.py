# Copyright 2022 Pavlo Penenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess

def compile(
    path : str,
    entry_point_name : str,
    profile : str,
    includes = None
) -> int:
    args = [
        'dxc',
        '-T', profile,
        '-E', entry_point_name,
        path
    ]

    if includes:
        for include in includes:
            args.append('-I')
            args.append(include)

    dxc_result = subprocess.run( args, capture_output = True )
    print(f'DXC stderr: {dxc_result.stderr.decode()}')
    return dxc_result.returncode
