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

import metashade.base.context
import metashade.clike.data_types

class Struct(metashade.clike.data_types.BaseType):
    def __init__(self):
        super().__init__()
        
        for name, member_def in self.__class__._member_defs.items():
            setattr(self, name, member_def.dtype())
        
        self._constructed = True
        
    def _define(
        self,
        sh,
        identifier,
        semantic = None,
        allow_init = True,
        annotations = None
    ):
        super()._define(sh, identifier, semantic, allow_init, annotations)
        
        for member_name, member in vars(self).items():
            if not member_name.startswith('_'):
                nested_name = '{struct_name}.{member_name}'.format(
                    struct_name=identifier, member_name=member_name
                )

                member._bind(sh, nested_name, allow_init=False)
    
    def __setattr__(self, name, value):
        if not name.startswith('_') and hasattr(self, '_constructed'):
            raise RuntimeError(
                "Metashade struct member can't be bound after construction")
            
        super().__setattr__(name, value)

class StructMemberDef:
    def __init__(self, dtype, semantic = None):
        self.dtype = dtype
        self.semantic = semantic

def define_struct(sh, name, member_defs):
    struct_type = type(
        name,
        (Struct,),
        {'_member_defs' : member_defs}
    )
    sh._set_global(name, struct_type)

    sh._emit('struct {name}\n{{\n'.format(name = name))
    sh._push_indent()

    for member_name, member_def in member_defs.items():
        sh._emit_indent()
        member_def.dtype._define_static(sh, member_name, member_def.semantic)
        sh._emit(";\n")

    sh._pop_indent()
    sh._emit('};\n\n')

class StructDef:
    def __init__(self, sh, name):
        self._sh = sh
        self._name = name

    def __call__(self, **kwargs):
        define_struct(
            self._sh,
            self._name,
            { name : StructMemberDef(dtype) for name, dtype in kwargs.items() }
        )

