# Copyright 2018 Pavlo Penenko
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

import metashade.hlsl.data_types
import metashade.clike.struct

class StageInterface(metashade.clike.struct.StructDef):
    def _define_member(self, member, member_identifier):
        member.semantic_define(self, member_identifier)

class VertexShaderIn(StageInterface):
    pass

class VertexShaderOut(StageInterface):
    def __init__(self, **kwargs):
        kwargs['position'] = metashade.hlsl.data_types.Vector4f
        super(VertexShaderOut, self).__init__(**kwargs)
