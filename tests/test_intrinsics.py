# Copyright 2023 Pavlo Penenko
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

import _base, _auto_float_intrinsics, _auto_numeric_intrinsics
from metashade.hlsl.sm6 import ps_6_0

class TestIntrinsics(_base.Base):
    def _test(self, hlsl_file_name, auto_package):
        hlsl_path = self._get_hlsl_path(hlsl_file_name)
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)

            with sh.uniform_buffer(register = 0, name = 'cb'):
                sh.uniform('g_f', sh.Float)
                for dim in range(1, 5):
                    sh.uniform(
                        f'g_f{dim}',
                        getattr(sh, f'Float{dim}')
                    )

                for row in range(1, 5):
                    for col in range(1, 5):
                        sh.uniform(
                            f'g_f{row}x{col}',
                            getattr(sh, f'Float{row}x{col}')
                        )

            auto_package.test(sh)

        self._compile(hlsl_path, as_lib = True)

    def test_float_intrinsics(self):
        self._test('test_float_intrinsics', _auto_float_intrinsics)

    def test_numeric_intrinsics(self):
        self._test('test_numeric_intrinsics', _auto_numeric_intrinsics)
