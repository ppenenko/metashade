# Copyright 2017 Pavlo Penenko
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

import metashade.base.data_types as base
import metashade.rtsl.data_types as rtsl
import metashade.clike.data_types as clike

class RawVector:
    def mul(self, matrix):
        self._check_mul(matrix)
        return self.__class__(
            'mul({this}, {matrix})'.format(
                this = self.get_ref(), matrix = matrix.get_ref()
            )
        )

class Float(rtsl.Float):
    _target_name = 'float'

class Float1(rtsl.Float1, RawVector):
    _target_name = 'float1'

class Float2(rtsl.Float2, RawVector):
    _target_name = 'float2'

class Float3(rtsl.Float3, RawVector):
    _target_name = 'float3'

class Float4(rtsl.Float4, RawVector):
    _target_name = 'float4'

    def __init__(self, initializer = None):
        if isinstance(initializer, tuple):
            initializer = 'float4({0}, {1}, {2}, {3})'.format(*xyzw)
        super().__init__(initializer)

for rows in range(1, 5):
    for cols in range(1, 5):
        name = 'Float{rows}x{cols}'.format(rows = rows, cols = cols)
        target_name = 'float{rows}x{cols}'.format(rows = rows, cols = cols)
        globals()[name] = type(
            name,
            (getattr(rtsl, name),),
            {'_target_name' : target_name}
        )

class Matrix4x4f(Float4x4):
    def xform(self, rhs):
        return rhs.as_vector4().mul(self)

class Vector4f(rtsl.Vector4f, Float4):
    pass

class Point3f(rtsl.Point3f, Float3):
    _vector4_type = Vector4f

class RgbaF(rtsl.RgbaF, Float4):
    pass
