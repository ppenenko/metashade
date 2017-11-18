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
import context

class Target(context.BaseContext):
    def __init__(self, file):
        self._file = file
        self._indent = 0
        self._indent_char = '\t'
        self._indent_delta = 1
        
        #self.Float = data_types.Float
        
    def get_target(self):
        return self
    
    def push_indent(self):
        self._indent += self._indent_delta
        
    def pop_indent(self):
        self._indent -= self._indent_delta
        
    def get_indent(self):
        return self._indent_char * (self._indent * self._indent_delta)
    
    def write(self, line):
        self._file.write(self.get_indent() + line)
