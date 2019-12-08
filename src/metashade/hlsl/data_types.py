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

import metashade.base.data_types as base
import metashade.slang.data_types as slang
import metashade.clike.data_types as clike

class Float(slang.Float):
    _target_name = 'float'
    
class Point3f(slang.Point3f):
    _target_name = 'float3'
    
class Vector4f(slang.Vector4f):
    def __init__(self, xyzw = None):
        initializer = None if xyzw is None \
            else 'float4({0}, {1}, {2}, {3})'.format(*xyzw)
        super(Vector4f, self).__init__(initializer)
                
    _target_name = 'float4'

class Matrix4x4f(clike.BaseType):
    _target_name = 'float4x4'

    def xform(self, v):
        pass

class RgbaF(slang.RgbaF):
    def __init__(self, rgba = None):
        initializer = None if rgba is None \
            else 'float4({0}, {1}, {2}, {3})'.format(*rgba)
        super(RgbaF, self).__init__(initializer)
    
    _target_name = 'float4'
