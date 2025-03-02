# Copyright 2025 Pavlo Penenko
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

import metashade._clike.context as clike
from . import stage_interface

class EntryPointDecl(clike.FunctionDecl):
    def __init__(self, sh, name, return_type):
        super().__init__(sh, name, return_type)
        
        output_cls = (
            stage_interface.PsOutputDef if sh._is_pixel_shader 
            else stage_interface.VsOutputDef
        )

        if not isinstance( self._return_type, output_cls):
            raise RuntimeError(
                f"Entry point expected to return an object of type '{output_cls.__name__}'"
            )