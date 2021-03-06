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

import numbers

class _MulBase:
    def mul(self, rhs, result_type):
        self._check_mul(rhs)
        return result_type(
            'mul({this}, {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref()
            )
        ) 

class Float(rtsl.Float):
    pass

class _RawVector(_MulBase):
    _element_type = Float
    def normalize(self):
        return self.__class__(
            'normalize({this})'.format(this = self.get_ref())
        )

class Float1(rtsl.Float1, _RawVector):
    _target_name = 'float1'

class Float2(rtsl.Float2, _RawVector):
    _target_name = 'float2'

class Float3(rtsl.Float3, _RawVector):
    _target_name = 'float3'

class Float4(rtsl.Float4, _RawVector):
    _target_name = 'float4'

    def __init__(self, xyzw = None, xyz = None, w = None):
        if xyz is None:
            if w is not None:
                raise RuntimeError('Conflicting arguments')

            rtsl.Float4.__init__(self, initializer = xyzw)
        else:
            if xyzw is not None:
                raise RuntimeError('Conflicting arguments')

            if not (isinstance(xyz, Float3) \
                or Float3._is_compatible_tuple(xyz)
            ):
                raise RuntimeError('"xyz" must be convertible to Float3')

            if not isinstance(w, numbers.Number):
                raise RuntimeError('"w" must be a scalar number')

            def get_ref(value):
                if hasattr(value, 'get_ref'):
                    return value.get_ref()
                elif Float3._is_compatible_tuple(value):
                    return ', '.join(map(str, value))
                else:
                    return value

            initializer = '{dtype}({xyz}, {w})'.format(
                dtype = __class__._target_name,
                xyz = get_ref(xyz),
                w = get_ref(w)
            )
            rtsl.Float4.__init__(self, initializer)

class _Matrix(_MulBase):
    # This is the HLSL default but should ideally be configurable
    _row_major = False
    _element_type = Float

# Generate all concrete matrix types to avoid copy-and-paste
for rows in range(1, 5):
    for cols in range(1, 5):
        name = 'Float{rows}x{cols}'.format(rows = rows, cols = cols)
        target_name = 'float{rows}x{cols}'.format(rows = rows, cols = cols)
        globals()[name] = type(
            name,
            (getattr(rtsl, name), _Matrix),
            {'_target_name' : target_name}
        )

class Matrix3x3f(Float3x3):
    def xform(self, vector):
        if self.__class__._row_major:
            return vector.mul(self, result_type = vector.__class__)
        else:
            return self.mul(vector, result_type = vector.__class__)

class Matrix4x4f(Float4x4):
    def xform(self, vector):
        vector = vector.as_vector4()
        if self.__class__._row_major:
            return vector.mul(self, result_type = Vector4f)
        else:
            return self.mul(vector, result_type = Vector4f)

class Vector4f(rtsl.Vector4f, Float4):
    pass

class Vector2f(rtsl.Vector2f, Float2):
    pass

class Vector3f(rtsl.Vector3f, Float3):
    _vector4_type = Vector4f

class Point2f(rtsl.Point2f, Float2):
    pass

class Point3f(rtsl.Point3f, Float3):
    _vector4_type = Vector4f

class RgbF(rtsl.RgbF, Float3):
    pass

class RgbaF(rtsl.RgbaF, Float4):
    def __init__(self, rgb = None, a = None):
        if rgb is not None \
            and not (isinstance(rgb, RgbF) \
                or RgbF._is_compatible_tuple(rgb)
            ):
            raise RuntimeError('"rgb" must be convertible to RgbF')

        Float4.__init__(self, xyz = rgb, w = a)
