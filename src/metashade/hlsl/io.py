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

class ShaderInOut(metashade.base.context.BaseContext):
    def __init__(self, **kwargs):        
        self._members = {name : data_type() \
                         for name, data_type in kwargs.iteritems()}
                
    def define(self, sh, identifier):
        self._identifier = identifier
        self._parent = sh
        self._target = sh.get_target()
            
        self._target.write('struct {identifier}{{\n'.format(
            identifier = self._identifier ))
        
        first = True
        for name, member in self._members.iteritems():
            if first:
                first = False
            else:
                self._target.write(', ')
            member.semantic_define(self, name)
                        
        self._target.write('};\n')

class VertexShaderIn(ShaderInOut):
    pass

class VertexShaderOut(ShaderInOut):
    pass