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

class ScopedContext(object):
    """
    The context class that allows adding new attributes of Metashade types.
    """    
    def __init__(self, sh):
        self._sh = sh
    
    def __setattr__(self, name, value):
        if not name.startswith('_'): #private variables are never meta
            if isinstance(self.__dict__.get(name), data_types.BaseType):
                raise AttributeError(
                    'Metashade variable ' + name + ' is already defined.')
            
            if hasattr(value, '_define'):
                value._define(self._sh, name)
            
        object.__setattr__(self, name, value)
