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
        value._define(self, name, semantic)
        self._write(';\n')
        
    vs_input = slang.Generator.struct
    
    def vs_output(self, name):
        class VSOutputDef(struct.StructDef):
            def __call__(self, **kwargs):
                position_name = 'position'
                position_type = data_types.Vector4f
                
                for member_name, dtype in kwargs.items():
                    if member_name == position_name or dtype == position_type:
                        raise RuntimeError(
                            'Homogenous position output already defined')
                
                kwargs[position_name] = position_type
                struct.StructDef.__call__(self, **kwargs)
                
        return VSOutputDef(self, name)

    ps_output = slang.Generator.struct
