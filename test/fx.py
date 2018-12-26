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
import metashade.hlsl.stage_interface as si
import metashade.hlsl.data_types as t

def test_simple():
    sh = profile.Target(sys.stderr)
    
    sh.VsIn = si.VertexShaderIn(position = t.Point3f)
    sh.VsOut = si.VertexShaderOut()
    
    with sh.VertexShaderMain('VsMain',
                             return_type = sh.VsOut,
                             i = sh.VsIn):
        sh.o = sh.VsOut()
        
        # TODO: multiply by MVP
        o = t.Vector4f(sh.i.position)
        sh.o.position = o   #TODO: doesn't generate code
        sh.return_(sh.o)
    
    sh.PsOut = si.PixelShaderOut(color = t.RGBA)
    
    with sh.PixelShaderMain('PsMain',
                            return_type = sh.PsOut):
        sh.o = sh.PsOut()
        sh.o.color = t.RGBA(1, 0, 1, 1)
        sh.return_(sh.o)
        
#     sh.Technique('technique0',
#         [sh.RenderPass('pass0',
#                        vertex_shader = sh.VsMain,
#                        pixel_shader = sh.PsMain)])
