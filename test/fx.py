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
Just a sketch of generating an HLSL effect with a trivial VS/PS pair.
Currently fails.
"""

import sys

import metashade.hlsl.fx.profile as profile
import metashade.hlsl.io as io
import metashade.hlsl.fx.context as context
import metashade.hlsl.data_types as t

def test_simple():
    sh = profile.Target(sys.stderr)
    
    sh.VsIn = io.VertexShaderIn(position = t.Point3f)
    sh.VsOut = io.VertexShaderOut()
    
    sh.VsMain = context.VertexShaderMain(return_value = sh.VsOut, i = sh.VsIn)
    with sh.VsMain.body() as sh:
        sh.o = sh.VsOut()
        
        # TODO: multiply by MVP
        sh.o.position = Vector4f(sh.i.position)
        sh.return_(sh.o)
        
    sh.PsOut = io.PixelShaderOut(color = RGBA)
    
    sh.PsMain = context.PixelShaderMain(return_value = sh.PsOut)
    with sh.PsMain.body() as sh:
        sh.o = sh.PsOut()
        sh.o.color = RGBA(1, 0, 1, 1)
        sh.return_(sh.o)
        
    sh.Technique('technique0',
        [sh.RenderPass('pass0',
                       vertex_shader = sh.VsMain,
                       pixel_shader = sh.PsMain)])
