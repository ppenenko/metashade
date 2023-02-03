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

import _base
from metashade.hlsl.sm6 import ps_6_0

class TestAugmentedAssignments(_base.Base):
    def test_augmented_add(self):
        hlsl_path = self._get_hlsl_path('test_augmented_add')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)

            with sh.function('assign_add', sh.Float4)(a = sh.Float4, b = sh.Float4):
                sh.a += sh.b
                sh.return_(sh.a)

        self._compile(hlsl_path, as_lib = True)
