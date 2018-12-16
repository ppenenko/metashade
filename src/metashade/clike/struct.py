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
    def __init__(self, struct_def):        
        super(Struct, self).__init__()
        self._struct_def = struct_def
        
    def get_target_type_name(self):
        return self._struct_def._identifier
    
    def __getattr__(self, name):
        return self._struct_def._members[name]

# TODO: perhaps this could be a metaclass?
class StructDef(object):
    def __init__(self, **kwargs):
        self._members = {name : data_type() \
                         for name, data_type in kwargs.iteritems()}
        
    def get_target(self):
        return self._target
    
    """
    Called by the wrapping context.
    """
    def define(self, sh, identifier):
        self._identifier = identifier
        #self._parent = sh
        self._target = sh.get_target()
            
        self._target.write('struct {identifier}\n{{\n'.format(
            identifier = self._identifier ))        
        self._target.push_indent()
        
        first = True
        for name, member in self._members.iteritems():
            if first:
                first = False
            else:
                self._target.write(',\n')
            self._define_member(member, name)
                        
        self._target.pop_indent()
        self._target.write('};\n\n')
        
    """
    Extracted to enable overrides
    """
    def _define_member(self, member, member_identifier):
        member.semantic_define(self, member_identifier)        
        
    def __call__(self):
        return Struct(self)

    def is_type_of(self, value):
        return value._struct_def == self
