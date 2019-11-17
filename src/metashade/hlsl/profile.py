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
from . import data_types
from . import stage_interface

class Generator(slang.Generator):
    def __init__(self, file_):
        super(Generator, self).__init__(file_)
        self._uniforms_by_semantic = dict()
        
    def uniform(self, name, dtype, semantic = None):
        # TODO: registers        
        if name.startswith('_'):
            raise RuntimeError("'{name}': names starting with an underscore"
                               "can't be Metashade symbols")
            
        if semantic is not None:
            existing = self._uniforms_by_semantic.get(semantic)
            if existing is not None:
                raise RuntimeError(
                    "Can't define uniform '{name}' with semantic '{semantic}' "
                    "because uniform '{existing_name}' already uses that "
                    "semantic.".format(name = name,
                                       semantic = semantic,
                                       existing_name = existing._name))
                
            
        value = dtype() #TODO: make it immutable
        self._set_global(name, value)
        self._emit_indent()
        value._define(self, name, semantic)
        self._emit(';\n')
        
    def vs_input(self, name):
        return stage_interface.VsInputDef(self, name)
    
    def vs_output(self, name):
        return stage_interface.VsOutputDef(self, name)

    ps_output = slang.Generator.struct
