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

class Function:
    def __init__(self, sh, name, return_type = type(None)):
        self._sh = sh
        self._name = name
        self._return_type = return_type
        self._args = dict()

    def __call__(self, **kwargs):
        self._args = {name : arg_type() \
                      for name, arg_type in kwargs.items()}
        return self

    def __getattr__(self, name):
        try:
            return self._args[name]
        except KeyError:
            raise AttributeError
        
    def __enter__(self):
        return_type = self._return_type.get_target_type_name() \
            if self._return_type != type(None) else 'void'

        self._sh._emit_indent()
        self._sh._emit('{return_type} {name}('.format(
            return_type = return_type,
            name = self._name ))
        
        first = True
        for name, arg in self._args.items():
            if first:
                first = False
            else:
                self._sh._emit(', ')
            arg._define(self._sh, name, allow_init=False)
                        
        self._sh._emit(')\n{\n')
        self._sh._push_indent()
        
        body = base.Scope()
        self._sh._push_context(body)
        return body
        
    def __exit__(self, exc_type, exc_value, traceback):
        self._sh._pop_context() # pop the function body
        self._sh._pop_context() # pop the function definition
        self._sh._pop_indent()
        self._sh._emit('}\n\n')
    
    def return_(self, value=None):
        mismatch_error = 'Return value type mismatch'
        if self._return_type is type(None):
            if value is not None:
                raise RuntimeError(mismatch_error)
        else:                
            if not isinstance(value, self._return_type):
                raise RuntimeError(mismatch_error)

        self._sh._emit_indent()
        self._sh._emit('return{};\n'.format(
            ' ' + value.get_ref() if value is not None else ''))
