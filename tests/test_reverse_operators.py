# Copyright 2025 Pavlo Penenko
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

"""
Tests demonstrating missing reverse operator implementations (__radd__, etc.)

These tests are expected to FAIL until reverse operators are implemented.
The issue is that Python tries `lhs.__add__(rhs)` first, and when lhs is a
primitive (like int or float), it returns NotImplemented. Python then tries
`rhs.__radd__(lhs)`, which doesn't exist in our types.

Currently, only __rmul__ is implemented in _RawVector for scalar-vector
multiplication.
"""

import pytest
from metashade.util.testing import ctx_cls_hg


class TestReverseOperators:
    """Tests for reverse operators (scalar OP shader_var)."""

    @ctx_cls_hg
    def test_radd_scalar_plus_float(self, ctx_cls):
        """
        Test: 1.0 + shader_float
        
        This should generate: float r = 1.0 + a;
        Currently fails with TypeError because Float lacks __radd__.
        """
        with ctx_cls(dummy_entry_point=True) as sh:
            with sh.function('test_radd', sh.Float)():
                sh.a = sh.Float(2.0)
                # This line will raise TypeError: unsupported operand type(s)
                sh.r = 1.0 + sh.a
                sh.return_(sh.r)

    @ctx_cls_hg
    def test_rsub_scalar_minus_float(self, ctx_cls):
        """
        Test: 1.0 - shader_float
        
        This should generate: float r = 1.0 - a;
        Currently fails with TypeError because Float lacks __rsub__.
        """
        with ctx_cls(dummy_entry_point=True) as sh:
            with sh.function('test_rsub', sh.Float)():
                sh.a = sh.Float(2.0)
                sh.r = 1.0 - sh.a
                sh.return_(sh.r)

    @ctx_cls_hg
    def test_rdiv_scalar_div_float(self, ctx_cls):
        """
        Test: 1.0 / shader_float
        
        This should generate: float r = 1.0 / a;
        Currently fails with TypeError because Float lacks __rtruediv__.
        """
        with ctx_cls(dummy_entry_point=True) as sh:
            with sh.function('test_rdiv', sh.Float)():
                sh.a = sh.Float(2.0)
                sh.r = 1.0 / sh.a
                sh.return_(sh.r)

    @ctx_cls_hg
    def test_radd_vector(self, ctx_cls):
        """
        Test: scalar + vector (addition, not multiplication)
        
        This should generate: float3 r = 1.0 + v;
        Currently fails with TypeError because Float3 lacks __radd__.
        
        Note: __rmul__ IS implemented for vectors (scalar * vector works).
        """
        with ctx_cls(dummy_entry_point=True) as sh:
            with sh.function('test_radd_vec', sh.Float3)():
                sh.v = sh.Float3((1.0, 2.0, 3.0))
                # This will fail - __radd__ not implemented
                sh.r = 1.0 + sh.v
                sh.return_(sh.r)

    @ctx_cls_hg
    def test_rmul_vector_works(self, ctx_cls):
        """
        Test: scalar * vector (this SHOULD work - __rmul__ is implemented)
        
        This is included to show the contrast - __rmul__ exists in _RawVector.
        """
        with ctx_cls(dummy_entry_point=True) as sh:
            with sh.function('test_rmul_vec', sh.Float3)():
                sh.v = sh.Float3((1.0, 2.0, 3.0))
                # This works because __rmul__ is implemented in _RawVector
                sh.r = 2.0 * sh.v
                sh.return_(sh.r)
