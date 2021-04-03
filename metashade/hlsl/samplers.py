# Copyright 2020 Pavlo Penenko
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

class Texture2d:
    def __init__(self, sh, name, register):
        self._name = name
        self._sh = sh
        sh._emit(
            'Texture2D {name} : register(t{register});\n'.format(
                name = name,
                register = register
            )
        )

class Sampler:
    def __init__(self, sh, name, register, texture):
        self._name = name
        self._sh = sh
        self._texture = texture
        sh._emit(
            'SamplerState {name} : register(s{register});\n\n'.format(
                name = name,
                register = register
            )
        )

    def __call__(self, texCoord):
        pass

