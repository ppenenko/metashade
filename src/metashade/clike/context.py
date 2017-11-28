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

import metashade.base.context as base

class ScopedContext(base.ScopedContext):
    def __enter__(self):
        self._target.write('{\n')
        self._target.push_indent()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):        
        self._target.pop_indent()
        self._target.write('}\n')
    
    def return_(self, value=None):
        self._target.write('return{};\n'.format(
            ' ' + value.get_ref() if value is not None else ''))
        
class Function(base.BaseContext):
    def __init__(self):
        super(Function, self).__init__(None)
        
    def define(self, sh, identifier):
        self._identifier = identifier
        self._parent = sh
        self._target = sh.get_target()
        self._target.write('void {identifier}()\n'.format(
            identifier = self._identifier ))
        
    def body(self):
        return ScopedContext(self)