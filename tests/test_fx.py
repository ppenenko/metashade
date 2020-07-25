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
        sh = profile.Generator(f)
        
        sh.uniform('diffuse_color', t.RgbaF)

        # Transforms
        sh.uniform('WorldXf', t.Matrix3x3f, semantic = 'World')
        sh.uniform('WvpXf', t.Matrix4x4f, semantic = 'WorldViewProjection')
        sh.uniform('WorldITXf', t.Matrix3x3f, semantic = 'WorldInverseTranspose')

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

        with sh.vs_input('VsIn') as vs_in:
            vs_in.position('Po', t.Point3f)
            vs_in.normal('No', t.Vector3f)

        with sh.vs_output('VsOut') as vs_out:
            vs_out.position('Pclip', t.Vector4f)
            vs_out.texCoord('Nw', t.Vector3f)
            vs_out.texCoord('Lw', t.Vector3f)

        with sh.vs_main('VsMain', sh.VsOut)(i = sh.VsIn):
            sh.o = sh.VsOut()

            sh.o.Pclip._ = sh.WvpXf.xform(sh.i.Po)
            sh.o.Nw._ = sh.WorldITXf.xform(sh.i.No)
            sh.o.Lw._ = sh.Lamp0Pos - sh.WorldITXf.xform(sh.i.Po)

            sh.return_(sh.o)
        
        with sh.ps_output('PsOut') as ps_out:
            ps_out.color('color', t.RgbaF)
        
        with sh.ps_main('PsMain', sh.PsOut)():
            sh.o = sh.PsOut()
            sh.o.color._ = sh.diffuse_color
            sh.return_(sh.o)
            
        fx.simple_vs_ps_technique(sh, 'VsMain', 'PsMain')
