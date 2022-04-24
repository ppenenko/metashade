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
import metashade.clike.struct as struct

import numbers

class _UnaryMixin:
    def _checkDdxDdy(self, name):
        if not self._sh.__class__._is_pixel_shader:
            raise RuntimeError(
                '"{}" is only supported in pixel shaders'.format(name)
            )

    def saturate(self):
        return self.__class__('saturate({})'.format(self))

    def ddx(self):
        self._checkDdxDdy('ddx')
        return self.__class__('ddx({})'.format(self))

    def ddy(self):
        self._checkDdxDdy('ddy')
        return self.__class__('ddy({})'.format(self))

class _MulMixin:
    def mul(self, rhs, result_type):
        self._check_mul(rhs)
        return result_type(
            'mul({this}, {rhs})'.format(
                this = self, rhs = rhs
            )
        ) 

class Float(rtsl.Float, _UnaryMixin):
    pass

class _RawVector(_MulMixin, _UnaryMixin):
    _element_type = Float
    def normalize(self):
        return self.__class__('normalize({})'.format(self))

class Float1(rtsl.Float1, _RawVector):
    _target_name = 'float1'

class Float2(rtsl.Float2, _RawVector):
    _target_name = 'float2'

class Float3(rtsl.Float3, _RawVector):
    _target_name = 'float3'

class Float4(rtsl.Float4, _RawVector):
    _target_name = 'float4'

    def __init__(self, _ : str = None, xyz = None, w = None):
        if xyz is None:
            if w is not None:
                raise RuntimeError('Conflicting arguments')

            rtsl.Float4.__init__(self, initializer = _)
        else:
            if _ is not None:
                raise RuntimeError('Conflicting arguments')

            xyz = Float3._get_value_ref(xyz)
            if xyz is None:
                raise RuntimeError('"xyz" must be convertible to Float3')

            if not isinstance(w, numbers.Number):
                raise RuntimeError('"w" must be a scalar number')

            initializer = '{dtype}({xyz}, {w})'.format(
                dtype = self.__class__._target_name,
                xyz = xyz,
                w = w
            )
            rtsl.Float4.__init__(self, initializer)

class _RawMatrixF(_MulMixin, _UnaryMixin, rtsl._RawMatrix):
    # This is the HLSL default but should ideally be configurable
    _row_major = False
    _element_type = Float

    @classmethod
    def _get_row_type_name(cls):
        return 'Float{}'.format(cls._dims[1])

    def __init__(self, initializer : str = None, rows = None):
        if rows is not None:
            if initializer is not None:
                raise RuntimeError(
                    'Conflicting constructor arguments'
                )

            if len(rows) != self.__class__._dims[0]:
                raise RuntimeError(
                    'Unexpected number of rows in matrix constructor'
                )

            row_type = globals()[self.__class__._get_row_type_name()]
            if any(row.__class__ !=  row_type for row in rows):
                raise RuntimeError(
                    'Unexpected row type in matrix constructor'
                )
            
            rtsl._RawMatrix.__init__(
                self,
                initializer = '{dtype}({rows})'.format(
                    dtype = self.__class__._target_name,
                    rows = ', '.join(map(str, rows))
                )
            )
        else:
            rtsl._RawMatrix.__init__(self, initializer = initializer)

# Generate all concrete matrix types to avoid copy-and-paste
for rows in range(1, 5):
    for cols in range(1, 5):
        name = 'Float{rows}x{cols}'.format(rows = rows, cols = cols)
        target_name = 'float{rows}x{cols}'.format(rows = rows, cols = cols)
        globals()[name] = type(
            name,
            (getattr(rtsl, name), _RawMatrixF),
            {'_target_name' : target_name}
        )

class _MatrixF(rtsl._Matrix, _RawMatrixF):
    @classmethod
    def _get_row_type_name(cls):
        return 'Vector{}f'.format(cls._dims[1])

class Matrix3x3f(_MatrixF, Float3x3):
    def __init__(self, initializer : str = None, rows = None):
        _MatrixF.__init__(self, initializer = initializer, rows = rows)

    def xform(self, vector):
        if self.__class__._row_major:
            return vector.mul(self, result_type = vector.__class__)
        else:
            return self.mul(vector, result_type = vector.__class__)

class Matrix4x4f(_MatrixF, Float4x4):
    def xform(self, vector):
        vector = vector.as_vector4()
        if self.__class__._row_major:
            return vector.mul(self, result_type = Vector4f)
        else:
            return self.mul(vector, result_type = Vector4f)

class Vector4f(rtsl.Vector4, Float4):
    pass

class Vector2f(rtsl.Vector2, Float2):
    pass

class Vector3f(rtsl.Vector3, Float3):
    pass

class Point2f(rtsl.Point2, Float2):
    pass

class Point3f(rtsl.Point3, Float3):
    pass

class RgbF(rtsl.RgbF, Float3):
    pass

class RgbaF(rtsl.RgbaF, Float4, struct.StructBase):
    _member_defs = {
        'rgb' : struct.StructMemberDef(RgbF),
        'a' : struct.StructMemberDef(Float)
    }

    def __init__(self, _ = None, rgb = None, a = None):
        if ( isinstance(rgb, Float3) and not isinstance(rgb, RgbF) ):
            raise RuntimeError('"rgb" must be convertible to RgbF')

        Float4.__init__(self, _ = _, xyz = rgb, w = a)
        struct.StructBase.__init__(self, self._expression)

    def _bind(self, sh, identifier, allow_init):
        super()._bind(sh, identifier, allow_init)
        self._bind_members(sh, identifier)

    def __setattr__(self, name, value):
        if not self._set_member(name, value):
            super().__setattr__(name, value)

