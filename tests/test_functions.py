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

import io, os, pathlib, subprocess, pytest, sys
from metashade.hlsl.sm5 import ps_5_0

class TestFunctions:
    @classmethod
    def setup_class(cls):
        parent_dir = pathlib.Path(sys.modules[cls.__module__].__file__).parent
        cls._out_dir = os.path.join(parent_dir, 'out')
        os.makedirs(cls._out_dir, exist_ok = True)

    def _test_function_call(self, func, file_name : str = None):
        entry_point_name = 'psMain'
        hlsl_path = ( os.path.join(self._out_dir, f'{file_name}.hlsl')
            if file_name is not None else None
        )

        def open_file():
            return ( open(hlsl_path, 'w')
                if hlsl_path is not None else io.StringIO()
            )

        with open_file() as ps_file:
            sh = ps_5_0.Generator(ps_file)
            with sh.function('add', sh.Float4)(a = sh.Float4, b = sh.Float4):
                sh.return_(sh.a + sh.b)

            with sh.ps_output('PsOut') as PsOut:
                PsOut.SV_Target('color', sh.Float4)

            with sh.uniform_buffer(register = 0, name = 'cb'):
                sh.uniform('g_f4A', sh.Float4)
                sh.uniform('g_f4B', sh.Float4)
                sh.uniform('g_f3C', sh.Float3)

            with sh.main(entry_point_name, sh.PsOut)():
                sh.result = sh.PsOut()
                if not func(sh):
                    return
                sh.return_(sh.result)

        if hlsl_path is not None:
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
            sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f4B)
            return True
        self._test_function_call(func, 'test_function_call')

    def test_missing_arg(self):
        def func(sh):
            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A)
            return False
        self._test_function_call(func)

    def test_extra_arg(self):
        def func(sh):
            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f4B, c = sh.g_f3C)
            return False
        self._test_function_call(func)

    def test_arg_type_mismatch(self):
        def func(sh):
            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f3C)
            return False
        self._test_function_call(func)