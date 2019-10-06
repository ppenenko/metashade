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
        super(Struct, self).__init__()
        
        for name, dtype in self.__class__._member_defs.iteritems():
            setattr(self, name, dtype())
        
        self._constructed = True
        
    def _define(self, sh, identifier):
        super(Struct, self)._define(sh, identifier)
        
        for member_name, member in vars(self).iteritems():
            if not member_name.startswith('_'):
                nested_name='{struct_name}.{member_name}'.format(
                    struct_name=identifier, member_name=member_name)

                member._bind(sh, nested_name, allow_defaults=False)
    
    def __setattr__(self, name, value):
        if not name.startswith('_') and hasattr(self, '_constructed'):
            raise RuntimeError(
                "Metashade struct member can't be bound after construction")
            
        super(Struct, self).__setattr__(name, value)

class StructDef(object):
    def __init__(self, sh, name):
        self._sh = sh
        self._name = name

    def __call__(self, **kwargs):
        struct_type = type( self._name,
                            (Struct,),
                            {'_member_defs' : kwargs})
        self._sh._set_global(self._name, struct_type)

        self._sh._write('struct {name}\n{{\n'.format(name = self._name))
        self._sh._push_indent()

        first = True
        for member_name, dtype in kwargs.iteritems():
            if first:
                first = False
            else:
                self._sh._write(',\n')
            dtype.define_member(self._sh, member_name)

        self._sh._pop_indent()
        self._sh._write('};\n\n')
