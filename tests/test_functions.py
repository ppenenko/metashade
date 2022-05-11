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

import os, pathlib, sys
from metashade.hlsl.sm5 import ps_5_0

class TestFunctions:
    @classmethod
    def setup_class(cls):
        parent_dir = pathlib.Path(sys.modules[cls.__module__].__file__).parent
        cls._out_dir = os.path.join(parent_dir, 'out')
        os.makedirs(cls._out_dir, exist_ok = True)

    def test_define(self):
        with open(
            os.path.join(self._out_dir, 'test_define_dunction.hlsl'),
            'w'
        ) as ps_file:
            sh = ps_5_0.Generator(ps_file)
            with sh.function('add', sh.Float4)(a = sh.Float4, b = sh.Float4):
                sh.return_(sh.a + sh.b)
