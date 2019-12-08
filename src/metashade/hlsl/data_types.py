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
import metashade.rtsl.data_types as rtsl
import metashade.clike.data_types as clike

class Float(rtsl.Float):
    _target_name = 'float'

class Float1(rtsl.Float1):
    _target_name = 'float1'

class Float2(rtsl.Float2):
    _target_name = 'float2'

class Float3(rtsl.Float3):
    _target_name = 'float3'

class Float4(rtsl.Float4):
    _target_name = 'float4'

class Point3f(rtsl.Point3f, Float3):
    _raw_vector4_type = Float4
    
class Vector4f(rtsl.Vector4f):
    def __init__(self, xyzw = None):
        initializer = None if xyzw is None \
            else 'float4({0}, {1}, {2}, {3})'.format(*xyzw)
        super().__init__(initializer)

    _target_name = 'float4'

class Matrix4x4f(clike.BaseType):
    _target_name = 'float4x4'

    def xform(self, v):
        pass

class RgbaF(rtsl.RgbaF):
    def __init__(self, rgba = None):
        initializer = None if rgba is None \
            else 'float4({0}, {1}, {2}, {3})'.format(*rgba)
        super().__init__(initializer)
    
    _target_name = 'float4'
