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

import metashade.slang.profile as slang
import metashade.clike.struct as struct
import data_types

class Generator(slang.Generator):
    vs_input = slang.Generator.struct
    
    def vs_output(self, identifier):
        def impl(**kwargs):
            position_name = 'position'
            position_type = data_types.Vector4f
            
            for name, data_type in kwargs.iteritems():
                if name == position_name or data_type == position_type:
                    raise RuntimeError(
                        'Homogenous position output already defined')
            
            kwargs[position_name] = position_type
        
            struct_def = struct.StructDef(self, identifier, kwargs)
            setattr(self, identifier, struct_def)
            return struct_def
                
        return impl
    
    pixel_shader_input = slang.Generator.struct
    ps_output = slang.Generator.struct
