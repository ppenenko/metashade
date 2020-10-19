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

"""
An example of generating an HLSL effect with a trivial VS/PS pair.
"""

import sys

import metashade.hlsl.profile as profile
import metashade.hlsl.data_types as t
import metashade.hlsl.fx as fx

def test_simple():
    with open("test_simple.fx", "w+") as f:
        # Create an HLSL FX generator writing to file f
        sh = profile.Generator(f)
        
        # Define an RGB color uniform, in single floating-point precision
        sh.uniform('diffuse_color', t.RgbF)

        # Transform uniforms. Semantics are HLSL-specific and can be ignored
        # when generating GLSL from this meta code. The semantic string
        # constants are specific to to the app (in this case FX Composer 2.5)
        # and are for CPU-side bindings only.
        sh.uniform('WorldXf', t.Matrix3x3f, semantic = 'World')
        sh.uniform('WvpXf', t.Matrix4x4f, semantic = 'WorldViewProjection')
        sh.uniform('WorldITXf', t.Matrix3x3f, semantic = 'WorldInverseTranspose')

        # The position of a light source. Similar to semantics, HLSL
        # annotations are app-specific, so we just pass them through as strings
        sh.uniform(
            'Lamp0Pos',
            t.Point3f,
            semantic = 'Position',
            annotations = [
                'string Object = "PointLight0"',
                'string UIName =  "Lamp 0 Position"',
                'string Space = "World"'
            ]
        )

        # The color of the light source
        sh.uniform(
            'Lamp0Color',
            t.RgbF,
            semantic = 'Specular',
            annotations = [
                'string UIName =  "Lamp 0"',
                'string Object = "Pointlight0"',
                'string UIWidget = "Color"'
            ]
        )

        # This scope defines an HLSL struct that serves as an input to the
        # vertex shader. In GLSL, the same meta code could generate in and out
        # blocks, ignoring HLSL semantics.
        with sh.vs_input('VsIn') as VsIn:
            # Each of these calls adds a struct member with the HLSL semantic
            # based on the function name
            VsIn.position('Po', t.Point3f)
            VsIn.normal('No', t.Vector3f)

        # The vertex shader output struct
        with sh.vs_output('VsOut') as VsOut:
            VsOut.position('Pclip', t.Vector4f)
            VsOut.texCoord('Nw', t.Vector3f)
            VsOut.texCoord('Lw', t.Vector3f)

        # Definition of the vertex shader entry point (main function). The
        # first set of parentheses specifies the function name and the return
        # type and the second set of parentheses lists the function arguments
        # with their types.
        with sh.vs_main('VsMain', sh.VsOut)(vsIn = sh.VsIn):
            # This generates a local variable of the specified type at the
            # function scope
            sh.vsOut = sh.VsOut()

            # _ is a special member denoting assignment by value
            sh.vsOut.Pclip._ = sh.WvpXf.xform(sh.vsIn.Po)
            sh.vsOut.Nw._ = sh.WorldITXf.xform(sh.vsIn.No)
            sh.vsOut.Lw._ = sh.Lamp0Pos - sh.WorldITXf.xform(sh.vsIn.Po)

            # Returning from the generated function
            sh.return_(sh.vsOut)
        
        # The pixel shader output struct
        with sh.ps_output('PsOut') as PsOut:
            PsOut.color('color', t.RgbaF)
        
        # Definition of the pixel shader entry point (main function).
        with sh.ps_main('PsMain', sh.PsOut)(psIn = sh.VsOut):
            sh.Nw = sh.psIn.Nw.normalize()
            sh.Lw = sh.psIn.Lw.normalize()

            # This generates a local variable of the specified type at the
            # function scope. Note that its type is deduced from the expression
            # it's initialized with, similar to the auto keyword in C++
            sh.lambert = sh.Lw.dot(sh.Nw) * sh.diffuse_color

            sh.psOut = sh.PsOut()
            sh.psOut.color._ = t.RgbaF(rgb = sh.lambert, a = 1.0)
            sh.return_(sh.psOut)

        # Generating a trivial HLSL FX technique. It's for testing in FX
        # Composer only, so it's not worth much investment.
        fx.simple_vs_ps_technique(sh, 'VsMain', 'PsMain')
