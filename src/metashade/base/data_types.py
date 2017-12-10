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

class BaseType(object):
    def __init__(self, initializer = None):
        self._identifier = None
        self._value = initializer
        
    #TODO: this is obviously too C-like to be here, move it elsewhere
    def define(self, sh, identifier):
        self._identifier = identifier
        self._target = sh.get_target()
        self._target.write('{type_name} {identifier}{initializer};\n'.format(
            type_name = self.__class__._target_name,
            identifier = self._identifier,
            initializer = '' if self._value is None else ' = {}'.format(self._value) ))
        
    def arg_define(self, sh, identifier):
        if self._value is not None:
            raise RuntimeError('Arguments with default values are not supported.')
            
        self._identifier = identifier
        self._target = sh.get_target()
        self._target.write('{type_name} {identifier}'.format(
            type_name = self.__class__._target_name,
            identifier = self._identifier))
        
    def get_ref(self):
        if self._identifier is not None:
            #TODO this check fails for function arguments, revisit
#             if self._value is None:
#                 raise RuntimeError(
#                     'Variable is used before it has been assigned a value')
            
            return self._identifier
        
        elif self._value is not None:
            return self._value
        else:        
            raise RuntimeError('Instance is neither a variable nor expression.')
        
    def __setattr__(self, name, value):
        if name == '_':
            self._value = value
            self._target.write('{identifier} = {value};\n'.format(
                identifier = self._identifier,
                value = value.get_ref() if hasattr(value, 'get_ref') else value ))
        else:
            object.__setattr__(self, name, value)
            
class Float(BaseType):
    def __add__(self, rhs):
        # TODO: handle implicit type conversions
        return self.__class__('{this} + {rhs}'.format(
            this = self.get_ref(), rhs = rhs.get_ref() ))