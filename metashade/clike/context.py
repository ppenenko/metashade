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

class FunctionDef:
    def __init__(self, sh, name, return_type = type(None)):
        self._sh = sh
        self._name = name
        self._return_type = return_type
        self._parameters = dict()

    def __getattr__(self, name):
        try:
            return self._parameters[name]
        except KeyError:
            raise AttributeError

    def __call__(self, **kwargs):
        '''
        This doesn't generate a function call from external code.
        Instead, this initializes a part of the function signature -
        the declarations of parameters with their names and types.
        '''
        self._parameters = {
            name : arg_type() for name, arg_type in kwargs.items()
        }
        # Return self, so that it can be entered in a with scope
        return self

    def __enter__(self):
        return_type = (
            self._return_type._get_target_type_name()
            if self._return_type != type(None)
            else 'void'
        )

        self._sh._emit_indent()
        self._sh._emit(f'{return_type} {self._name}(')
        
        # emit the argument declarations
        first = True
        for name, arg in self._parameters.items():
            if first:
                first = False
            else:
                self._sh._emit(', ')
            arg._define(self._sh, name, allow_init=False)
                        
        self._sh._emit(')\n{\n')
        self._sh._push_indent()
        
        # push and return the function body - a separate scope that can have
        # its own locals
        body = base.Scope()
        self._sh._push_context(body)
        return body
        
    def __exit__(self, exc_type, exc_value, traceback):
        self._sh._pop_context() # pop the function body
        self._sh._pop_context() # pop the function definition
        self._sh._pop_indent()
        self._sh._emit('}\n\n')
    
    def return_(self, value=None):
        if ( (self._return_type is type(None) and value is not None)
            or not isinstance(value, self._return_type)
        ):
            raise RuntimeError('Return value type mismatch')

        self._sh._emit_indent()
        self._sh._emit('return{};\n'.format(
            ' ' + str(value) if value is not None else ''
        ))

class Function:
    def __init__(self, definition : FunctionDef) -> None:
        self._def = definition

    def __call__(self, **kwargs):
        parameters_to_fill = {name for name in self._def._parameters.keys()}

        def _get_value_ref(name, arg) -> str:
            parameter = self._def._parameters.get(name)
            if parameter is None:
                raise RuntimeError(f'Unknown parameter "{name}"')
            ref = parameter.__class__._get_value_ref(arg)
            if ref is None:
                raise RuntimeError(f'Parameter "{name}" type mismatch')
            parameters_to_fill.remove(name)
            return str(ref)

        args_str = ', '.join(
            [ _get_value_ref(name, arg) for name, arg in kwargs.items() ]
        )

        if parameters_to_fill:
            raise RuntimeError(f'Missing arguments: {parameters_to_fill}')
        return self._def._return_type(f'{self._def._name}({args_str})')
