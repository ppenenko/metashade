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

import metashade.base.profile as base
from . import context
from . import struct

class Generator(base.Generator):
    def function(self, name : str, return_type):
        function_def = context.FunctionDef(self, name, return_type)
        self._set_global(name, context.Function(function_def))
        self._push_context(function_def)
        return function_def
    
    def struct(self, name):
        return struct.StructDef(self, name)
