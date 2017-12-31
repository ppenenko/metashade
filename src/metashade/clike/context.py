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
from types import NoneType

class ScopedContext(base.ScopedContext):
    def __enter__(self):
        self._target.write('{\n')
        self._target.push_indent()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):        
        self._target.pop_indent()
        self._target.write('}\n')
        
class Function(base.BaseContext):
    def __init__(self, **kwargs):
        super(Function, self).__init__(parent=None)
        
        self._args = dict()
        self._return_type = NoneType
        
        for name, arg_type in kwargs.iteritems():
            if name == 'return_type':
                self._return_type = arg_type
            else:
                self._args[name] = arg_type()
        
    def define(self, sh, identifier):
        self._identifier = identifier
        self._parent = sh
        self._target = sh.get_target()
        
        return_type = self._return_type._target_name \
            if self._return_type != NoneType else 'void'
            
        self._target.write('{return_type} {identifier}('.format(
            return_type = return_type,            
            identifier = self._identifier ))
        
        first = True
        for name, arg in self._args.iteritems():
            if first:
                first = False
            else:
                self._target.write(', ')
            arg.arg_define(self, name)
                        
        self._target.write(')\n')
        
    def __getattr__(self, name):
        arg = self._args.get(name)
        return arg if arg is not None \
            else super(Function, self).__getattr__(name)
        
    def body(self):
        return ScopedContext(self)
    
    def return_(self, value=None):
        if not isinstance(value, self._return_type):
            raise RuntimeError('Return value type mismatch')
            
        self._target.write('return{};\n'.format(
            ' ' + value.get_ref() if value is not None else ''))
