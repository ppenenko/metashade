# Copyright 2026 Pavlo Penenko
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
Test demonstrating MaterialX default parameter extraction.

The generalized_schlick_bsdf node has 13+ parameters with defaults defined
in the MaterialX nodedef. This test shows how Metashade automatically
extracts those defaults, allowing you to call the node with only the
inputs you want to override.
"""

from __future__ import annotations
import io

import pytest

mx = pytest.importorskip("MaterialX")

from metashade.mtlx.mtlx_reflection import acquire_function
from metashade.mtlx.dtypes import register_mtlx_closure_structs
from metashade.mtlx.util.testing import GlslTestContext
from metashade.targets._clike.context import In
from metashade.targets.glsl import frag


class TestSchlickWithDefaults:
    """Tests for MaterialX default parameter extraction."""

    def test_acquire_with_defaults(self, stdlib_doc: mx.Document):
        """
        Verify that acquire_function extracts MaterialX defaults.
        
        The generalized_schlick_bsdf nodedef defines defaults like:
        - weight: 1.0
        - color0: (1.0, 1.0, 1.0)
        - exponent: 5.0
        - roughness: (0.05, 0.05)
        etc.
        
        These should be reflected in the acquired function's param_defs.
        """
        # Use a simple generator - no file output needed for reflection test
        sh = frag.Generator(io.StringIO(), glsl_version='')
        register_mtlx_closure_structs(sh)
        
        # Find and acquire the generalized_schlick_bsdf
        for impl in stdlib_doc.getImplementations():
            if (
                impl.getNodeDefString().endswith("generalized_schlick_bsdf")
                and impl.getTarget() == "genglsl"
            ):
                schlick = acquire_function(sh, impl)
                break
        else:
            pytest.fail("Could not find generalized_schlick_bsdf")
        
        # Verify defaults were extracted
        assert schlick is not None
        param_defs = schlick._param_defs
        
        # Check that inputs with defaults use In with default values
        assert isinstance(param_defs['weight'], In)
        assert param_defs['weight'].default == 1.0
        
        assert isinstance(param_defs['color0'], In)
        assert param_defs['color0'].default == (1.0, 1.0, 1.0)
        
        assert isinstance(param_defs['exponent'], In)
        assert param_defs['exponent'].default == 5.0
        
        assert isinstance(param_defs['roughness'], In)
        assert param_defs['roughness'].default == pytest.approx((0.05, 0.05))
        
        # normal/tangent have no default value (geometry-bound)
        assert not isinstance(param_defs['normal'], In) or \
               param_defs['normal'].default is None

    def test_call_with_partial_args(self, stdlib_doc: mx.Document):
        """
        Generate a wrapper that calls generalized_schlick_bsdf with
        only a subset of inputs connected - the rest use MaterialX defaults.
        
        This mimics how gltf_pbr.mtlx uses the node:
        - metal_bsdf only connects: color0, color90, roughness, normal, tangent
        - All other inputs use their MaterialX defaults
        """
        ctx = GlslTestContext(base_name="schlick_simplified")
        
        with ctx as test_ctx:
            sh = test_ctx._sh
            register_mtlx_closure_structs(sh)
            
            # Acquire the generalized_schlick_bsdf with defaults
            for impl in stdlib_doc.getImplementations():
                if (
                    impl.getNodeDefString().endswith("generalized_schlick_bsdf")
                    and impl.getTarget() == "genglsl"
                ):
                    file_attr = impl.getAttribute("file")
                    sh.include(file_attr)
                    schlick = acquire_function(sh, impl)
                    break
            else:
                pytest.fail("Could not find generalized_schlick_bsdf")
            
            # Define a simplified wrapper that only takes commonly-used inputs
            func_name = 'schlick_metal'
            
            with sh.function(func_name)(
                closureData=sh.ClosureData,
                color0=sh.RgbF,
                color90=sh.RgbF,
                roughness=sh.Float2,
                normal=sh.Float3,
                tangent=sh.Float3,
                out_=sh.Out(sh.BSDF)
            ):
                # Call schlick with only connected inputs - rest use defaults!
                schlick(
                    closureData=sh.closureData,
                    color0=sh.color0,
                    color90=sh.color90,
                    roughness=sh.roughness,
                    normal=sh.normal,
                    tangent=sh.tangent,
                    out_=sh.out_
                    # weight, color82, exponent, thinfilm_*, distribution,
                    # scatter_mode all use their MaterialX defaults
                )
            
            # Register as MaterialX node
            test_ctx.add_node_impl(
                func_name=func_name,
                mx_doc_string=(
                    'Simplified Schlick BSDF - calls generalized_schlick_bsdf '
                    'with MaterialX defaults for weight, color82, exponent, '
                    'thinfilm, distribution, and scatter_mode.'
                )
            )
