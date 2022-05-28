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

import os, pathlib, subprocess, pytest, sys
from metashade.hlsl.sm5 import ps_5_0

class TestFunctions:
    @classmethod
    def setup_class(cls):
        parent_dir = pathlib.Path(sys.modules[cls.__module__].__file__).parent
        cls._out_dir = os.path.join(parent_dir, 'out')
        os.makedirs(cls._out_dir, exist_ok = True)

    def _test_function_call(self, test_name :  str, func):
        hlsl_path = os.path.join(self._out_dir, f'{test_name}.hlsl')
        entry_point_name = 'psMain'
        with open(hlsl_path, 'w') as ps_file:
            sh = ps_5_0.Generator(ps_file)
            with sh.function('add', sh.Float4)(a = sh.Float4, b = sh.Float4):
                sh.return_(sh.a + sh.b)

            with sh.ps_output('PsOut') as PsOut:
                PsOut.SV_Target('color', sh.Float4)

            with sh.uniform_buffer(register = 0, name = 'cb'):
                sh.uniform('gA', sh.Float4)
                sh.uniform('gB', sh.Float4)

            with sh.main(entry_point_name, sh.PsOut)():
                sh.result = sh.PsOut()
                if not func(sh):
                    return
                sh.return_(sh.result)

        dxc_result = subprocess.run(
            [
                'dxc',
                '-T', 'ps_6_0', # the lowest supported by DXC
                '-E', entry_point_name,
                hlsl_path
            ],
            capture_output = True
        )
        print(f'DXC stderr: {dxc_result.stderr.decode()}')
        assert dxc_result.returncode == 0

    def test_function_call(self):
        def func(sh):
            sh.result.color = sh.add(a = sh.gA, b = sh.gB)
            return True
        self._test_function_call('test_function_call', func)

    def test_missing_arg(self):
        def func(sh):
            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.gA)
            return False

        self._test_function_call('test_missing_arg', func)