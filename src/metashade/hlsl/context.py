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

import metashade.clike.context as clike

class ShaderMain(clike.Function):
    """
    Possible base class for main functions for each shading stage.
    
    For HLSL, it would probably need to enforce that all arguments
    and return values define semantics.
    """
    pass

class VertexShaderMain(ShaderMain):
    pass

class PixelShaderMain(ShaderMain):
    pass