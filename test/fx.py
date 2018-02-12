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

def test_simple():
    sh = profile.Target(sys.stderr)
    
    sh.VsIn = sh.VertexShaderIn(position = sh.Point3f)
    sh.VsOut = sh.VertexShaderOut()
    
    sh.VsMain = sh.VertexShaderMain(return_value = sh.VsOut, i = sh.VsIn)
    with sh.VsMain.body() as sh:
        sh.o = sh.VsOut()
        
        # TODO: multiply by MVP
        sh.o.position = sh.Vector4f(sh.i.position)
        sh.return_(sh.o)
        
    sh.PsOut = sh.PixelShaderOut(color = sh.Rgba)
    
    sh.PsMain = sh.PixelShaderMain(return_value = sh.PsOut)
    with sh.PsMain.body() as sh:
        sh.o = sh.PsOut()
        sh.o.color = sh.Rgba(1, 0, 1, 1)
        sh.return_(sh.o)
        
    sh.Technique('technique0',
        [sh.RenderPass('pass0',
                       vertex_shader = sh.VsMain,
                       pixel_shader = sh.PsMain)])
