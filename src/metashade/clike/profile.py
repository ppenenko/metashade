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

import metashade.base.profile as base
import context
import struct

class Generator(base.Generator):
    def function(self, name, return_type):
        function = context.Function(self, name, return_type)
        self._set_global(name, function)
        self._push_context(function)
        return function
    
    def struct(self, name):
        def impl(**kwargs):
            struct_def = struct.StructDef(self, name, kwargs)
            self._set_global(name, struct_def)
            return struct_def
                
        return impl
    
        
        
    