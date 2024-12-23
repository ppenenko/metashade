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

import metashade._rtsl.dtypes as rtsl

import numbers
from . import _auto_float_intrinsics, _auto_numeric_intrinsics

class _AnyLayoutMixin(
    _auto_float_intrinsics.AnyLayoutMixin,
    _auto_numeric_intrinsics.AnyLayoutMixin
):
    def _checkDdxDdy(self, name):
        if not self._sh.__class__._is_pixel_shader:
            raise RuntimeError(f'"{name}" is only supported in pixel shaders')

    def ddx(self):
        self._checkDdxDdy('ddx')
        return super().ddx()

    def ddy(self):
        self._checkDdxDdy('ddy')
        return super().ddy()

class _MulMixin:
    def mul(self, rhs, result_type):
        self._check_mul(rhs)
        return self._sh._instantiate_dtype(result_type, f'mul({self}, {rhs})')

class Float(rtsl.Float, _AnyLayoutMixin):
    pass

class Int(rtsl.Int, _AnyLayoutMixin):
    pass

class _RawVector(rtsl._RawVector, _MulMixin, _AnyLayoutMixin):
    def __init__(self, _ = None):
        element_ref = self.__class__._element_type._get_value_ref(_)
        super().__init__(
            '.'.join((str(element_ref), 'x' * self.__class__._dim))
                if element_ref is not None else _
        )

class _RawVectorF(_RawVector):
    _element_type = Float

    # TODO: auto-generate a mixin for the following methods:
    # https://github.com/metashade/metashade/issues/9

    def normalize(self):
        return self.__class__( f'normalize({self})' )

    def length(self):
        return self._sh._instantiate_dtype(
            self.__class__._element_type,
            f'length({self})'
        )
    
    def reflect(self, rhs):
        return self.__class__( f'reflect({self}, {rhs})' )
    
class _RawVectorI(_RawVector):
    _element_type = Int

class Float1(_RawVectorF, rtsl.RawVector1):
    _target_name = 'float1'

class Float2(_RawVectorF, rtsl.RawVector2):
    _target_name = 'float2'

class Float3(_RawVectorF, rtsl.RawVector3):
    _target_name = 'float3'

class Float4(_RawVectorF, rtsl.RawVector4):
    _target_name = 'float4'

    def __init__(self, _ = None, xyz = None, w = None):
        if xyz is None:
            if w is not None:
                raise RuntimeError('Conflicting arguments')

            super().__init__(_)
        else:
            if _ is not None:
                raise RuntimeError('Conflicting arguments')

            xyz = Float3._get_value_ref(xyz)
            if xyz is None:
                raise RuntimeError('"xyz" must be convertible to Float3')

            if not isinstance(w, numbers.Number):
                raise RuntimeError('"w" must be a scalar number')

            expression = '{dtype}({xyz}, {w})'.format(
                dtype = self.__class__._target_name,
                xyz = xyz,
                w = w
            )
            super().__init__(expression)

class Int1(_RawVectorI, rtsl.RawVector1):
    _target_name = 'int1'

class Int2(_RawVectorI, rtsl.RawVector2):
    _target_name = 'int2'

class Int3(_RawVectorI, rtsl.RawVector3):
    _target_name = 'int3'

class Int4(_RawVectorI, rtsl.RawVector4):
    _target_name = 'int4'

class _RawMatrixF(_MulMixin, _AnyLayoutMixin, rtsl._RawMatrixF):
    _element_type = Float

    @classmethod
    def _get_row_type_name(cls):
        return f'Float{cls._dims[1]}'

    def __init__(self, _ = None, rows = None):
        if rows is None:
            rtsl._RawMatrixF.__init__(self, _ = _)
        else:
            if _ is not None:
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
            
            rtsl._RawMatrixF.__init__(
                self,
                _ = '{dtype}({rows})'.format(
                    dtype = self.__class__._target_name,
                    rows = ', '.join(map(str, rows))
                )
            )

# Generate all concrete matrix types to avoid copy-and-paste
for rows in range(1, 5):
    for cols in range(1, 5):
        name = f'Float{rows}x{cols}'
        target_name = f'float{rows}x{cols}'
        globals()[name] = type(
            name,
            (getattr(rtsl, name), _RawMatrixF),
            {'_target_name' : target_name}
        )

class _MatrixF(rtsl._MatrixF, _RawMatrixF):
    @classmethod
    def _get_row_type_name(cls):
        return f'Vector{cls._dims[1]}f'
    
    def _xform(self, rhs, result_type):
        if self._sh._matrix_post_multiplication:
            return self.mul(rhs, result_type = result_type)
        else:
            return rhs.mul(self, result_type = result_type)

class Matrix3x3f(_MatrixF, Float3x3):
    def __init__(self, _ = None, rows = None):
        _MatrixF.__init__(self, _ = _, rows = rows)

    def xform(self, rhs):
        return self._xform(rhs, rhs.__class__)

class Matrix4x3f(_MatrixF, Float4x3):
    def xform(self, rhs):
        if rhs._dim != 3:
            raise RuntimeError(
                'Only 3-element inputs are supported by Matrix4x3f'
            )
        return self._xform(rhs.as_vector4(), rhs.__class__)
    
class Matrix3x4f(_MatrixF, Float3x4):
    def xform(self, rhs):
        if rhs._dim != 3:
            raise RuntimeError(
                'Only 3-element inputs are supported by Matrix3x4f'
            )
        return self._xform(rhs.as_vector4(), rhs.__class__)

class Matrix4x4f(_MatrixF, Float4x4):
    def xform(self, rhs):
        return self._xform(rhs.as_vector4(), Vector4f)

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
    _swizzle_str = 'rgb'

class RgbaF(rtsl.RgbaF, Float4):
    _swizzle_str = 'rgba'

    def __init__(self, _ = None, rgb = None, a = None):
        if ( isinstance(rgb, Float3) and not isinstance(rgb, RgbF) ):
            raise RuntimeError('"rgb" must be convertible to RgbF')

        super().__init__(_ = _, xyz = rgb, w = a)

    def __getattr__(self, name):
        if name == 'rgb':
            return self._sh._instantiate_dtype(
                RgbF,
                '.'.join((str(self), name))
            )
        else:
            return super().__getattr__(name)

    def __setattr__(self, name, value):
        if name == 'rgb':
            lvalue = self._sh._instantiate_dtype(
                RgbF,
                '.'.join((str(self), name))
            )
            lvalue._assign(value)
        else:
            super().__setattr__(name, value)
