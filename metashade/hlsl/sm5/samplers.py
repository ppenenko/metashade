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

from . import data_types

class Texture2d:
    _tex_coord_type = data_types.Point2f

    def __init__(self, sh, name : str, register : int, texel_type = None):
        self._name = name
        self._sh = sh
        self._texel_type = texel_type if texel_type is not None else sh.Float4
        sh._emit(
            'Texture2D {name} : register(t{register});\n'.format(
                name = name,
                register = register
            )
        )

    def sample(self, sampler, tex_coord):
        if tex_coord.__class__ != self.__class__._tex_coord_type:
            raise RuntimeError(
                'Expected texture coordinate type ' \
                    + str(self.__class__._tex_coord_type)
            )
        return self._texel_type(
            _ = '{name}.Sample({sampler_name}, {tex_coord})'.format(
                name = self._name,
                sampler_name = sampler._name,
                tex_coord = tex_coord.get_ref()
            )
        )

class Sampler:
    def __init__(self, sh, name : str, register : int, texture):
        self._name = name
        self._sh = sh
        self._texture = texture
        sh._emit(
            'SamplerState {name} : register(s{register});\n\n'.format(
                name = name,
                register = register
            )
        )

    def __call__(self, tex_coord):
        if self._texture is None:
            raise RuntimeError("Sampler hasn't been combined with any texture")
        return self._texture.sample(self, tex_coord)
