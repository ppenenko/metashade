# Copyright 2018 Pavlo Penenko
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

import metashade.clike.data_types as clike
from metashade.clike.data_types import Float

class RawVector(clike.ArithmeticType):
    def _check_dims(self, rhs):
        if rhs.__class__._dim != self.__class__._dim:
            raise ArithmeticError(
                'Operands must have the same dimensions.'
            )

    def _binary_operator(self, rhs, op):
        self._check_dims(rhs)
        super()._binary_operator(self, rhs, op)

    def dot(self, rhs):
        self._check_dims(rhs)
        return self.__class__._element_type(
            'dot({this}, {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref()
            )
        )

    def mul(self, matrix):
        if matrix.__class__._dims[0] != self.__class__._dim:
            raise ArithmeticError(
                'The number of rows in the matrix must be equal to the size of'
                ' the vector'
            )
        # Derived classes must implement code generation.

class Float1(RawVector):
    _dim = 1
    _element_type = clike.Float

class Float2(RawVector):
    _dim = 2
    _element_type = clike.Float

class Float3(RawVector):
    _dim = 3
    _element_type = clike.Float

    def cross(self, rhs):
        if rhs.__class__ != self.__class__:
            raise ArithmeticError(
                'Cross product operands must have the same type (3D vector)'
            )
        return self.__class__(
            'cross({this}, {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref()
            )
        )

class Float4(RawVector):
    _dim = 4
    _element_type = clike.Float

class RawMatrix(clike.ArithmeticType):
    pass

for rows in range(5):
    for cols in range(5):
        type(
            'Float{rows}x{cols}'.format(rows = rows, cols = cols),
            (RawMatrix,),
            {'_dims' : (rows, cols), '_element_type' : clike.Float}
        )

class Point3f:
    def asVector4(self):
        raw_vector4_type = self.__class__._raw_vector4_type
        return raw_vector4_type(
            '{dtype}({this}, 1.0f)'.format(
                dtype = raw_vector4_type.get_target_type_name(),
                this = self.get_ref
            )
        )

Vector4f = Float4
RgbaF = Float4
