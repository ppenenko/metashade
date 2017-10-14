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

import profiles.base        
            
class BaseContext(object):
    def __init__(self, parent):
        self._parent = parent
        self._target = parent.get_target()
        
    def get_target(self):
        return self._target
        
class ScopedContext(BaseContext):
    def __enter__(self):
        self._target.open_scope()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self._target.close_scope()
    
    def __setattr__(self, name, value):        
        if isinstance(self.__dict__.get(name), profiles.base.BaseType):
            raise AttributeError('Metashade variable ' + name + ' is already defined.')
        
        if hasattr(value, 'define'):
            value.define(self, name)
            
        object.__setattr__(self, name, value)
    
    def return_(self, value=None):
        self._target.return_(value)
        
class Function(BaseContext):        
    def body(self):
        return ScopedContext(self)