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

import sys

import metashade.hlsl.profile as profile
import metashade.hlsl.data_types as t 

def test_simple():
    sh = profile.Target(sys.stderr)
    
    with sh.Function('test_func',
                     return_type = t.Float,
                     a = t.Float,
                     e = t.Float) as sh:
        sh.b = t.Float(2)
        sh.c = sh.a + sh.b
        
        sh.d = t.Float()
        sh.d._ = sh.b + sh.a
        sh.d._ = t.Float(4)
        sh.d._ = 5
        
        #sh.return_()
        sh.return_(sh.c)
        sh.return_(sh.a + sh.b)
        sh.return_(sh.a + t.Float(3.0))
    
# def test_double_definition():
#     sh = profile.Target(sys.stderr)
#     sh.test_func = sh.Function()
#      
#     with sh.test_func.body() as sh:
#         sh.a = sh.Float(1)        
#         try:
#             sh.a = sh.Float(2)
#         except AttributeError:
#             pass
#         else:
#             assert False
                        
                