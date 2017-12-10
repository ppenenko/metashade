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

import data_types        
            
class BaseContext(object):
    def __init__(self, parent):
        self._parent = parent
        self._target = None if parent is None else parent.get_target()
        
    def get_target(self):
        return self._target
    
    def __getattr__(self, name):
        if self.__dict__.get('_parent') is None:
            raise RuntimeError('Identifier {name} is not defined.'.format(
                name=name))
        return getattr(self._parent, name)

class ScopedContext(BaseContext):    
    def __setattr__(self, name, value):
        if not name.startswith('_'): #private variables are never meta
            if isinstance(self.__dict__.get(name), data_types.BaseType):
                raise AttributeError(
                    'Metashade variable ' + name + ' is already defined.')
            
            if hasattr(value, 'define'):
                value.define(self, name)
            
        object.__setattr__(self, name, value)
