# Copyright 2022 Pavlo Penenko
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

import io, os, pathlib, pytest, sys
from metashade.hlsl.sm6 import ps_6_0
from metashade.hlsl.common import compile

class TestFunctions:
    @classmethod
    def setup_class(cls):
        parent_dir = pathlib.Path(sys.modules[cls.__module__].__file__).parent
        cls._out_dir = os.path.join(parent_dir, 'out')
        os.makedirs(cls._out_dir, exist_ok = True)

    _entry_point_name = 'psMain'

    def _get_hlsl_path(self, file_name : str) -> str:
        return ( os.path.join(self._out_dir, f'{file_name}.hlsl')
            if file_name is not None else None
        )

    def _open_file(self, hlsl_path : str = None):
        return ( open(hlsl_path, 'w')
            if hlsl_path is not None else io.StringIO()
        )

    def _generate_add_func(self, sh, decl_only = False):
        func = sh.function('add', sh.Float4)(a = sh.Float4, b = sh.Float4)

        # Test that we don't leak the scope created for the parameters
        assert getattr(sh, 'a', None) is None

        if decl_only:
            func.declare()
        else:
            with func:
                sh.return_(sh.a + sh.b)

    def _generate_ps_main(self, sh):
        with sh.ps_output('PsOut') as PsOut:
            PsOut.SV_Target('color', sh.Float4)

        with sh.uniform_buffer(register = 0, name = 'cb'):
            sh.uniform('g_f4A', sh.Float4)
            sh.uniform('g_f4B', sh.Float4)
            sh.uniform('g_f3C', sh.Float3)

        return sh.main(self._entry_point_name, sh.PsOut)()

    def _compile(self, hlsl_path, includes = None, as_lib : bool = False):
        # LIB profiles support DXIL linking and therefore allow function
        # declarations without definitions.
        # Pure declarations may also be useful in other profiles if the
        # definition is found elsewhere in the compilation unit, e.g. in an
        # included header.
        assert 0 == compile(
            path = hlsl_path,
            entry_point_name = self._entry_point_name,
            profile = 'lib_6_6' if as_lib else 'ps_6_0',
            includes = includes
        )

    def _correct_ps_main(self, sh):
        with self._generate_ps_main(sh):
            sh.result = sh.PsOut()
            sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f4B)
            sh.return_(sh.result)

    def test_function_call(self):
        hlsl_path = self._get_hlsl_path('test_function_call')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)
            self._generate_add_func(sh)
            self._correct_ps_main(sh)
        self._compile(hlsl_path)

    def test_function_decl_call(self):
        hlsl_path = self._get_hlsl_path('test_function_decl_call')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)
            self._generate_add_func(sh, decl_only = True)
            self._correct_ps_main(sh)
        self._compile(hlsl_path, as_lib = True)

    def test_included_function_call(self):
        hlsl_path = self._get_hlsl_path('test_included_function_call')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)
            sh.include('include/add.hlsl')
            self._generate_add_func(sh, decl_only = True)
            self._correct_ps_main(sh)
        self._compile(
            hlsl_path,
            includes = [
                pathlib.Path(sys.modules[self.__module__].__file__).parent
            ]
        )

    def test_missing_arg(self):
        with self._open_file() as ps_file:
            sh = ps_6_0.Generator(ps_file)
            self._generate_add_func(sh)

            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A)

    def test_extra_arg(self):
        with self._open_file() as ps_file:
            sh = ps_6_0.Generator(ps_file)
            self._generate_add_func(sh)

            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f4B, c = sh.g_f3C)

    def test_arg_type_mismatch(self):
        with self._open_file() as ps_file:
            sh = ps_6_0.Generator(ps_file)
            self._generate_add_func(sh)
            
            with pytest.raises(Exception):
                sh.result.color = sh.add(a = sh.g_f4A, b = sh.g_f3C)

    def test_void_func_decl(self):
        hlsl_path = self._get_hlsl_path('test_void_func_decl')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)

            sh.function('voidFuncA')(a = sh.Float4, b = sh.Float4).declare()
            sh.function('voidFuncB', type(None))(a = sh.Float4, b = sh.Float4).declare()
            sh.function('voidFuncC', None)(a = sh.Float4, b = sh.Float4).declare()

        self._compile(hlsl_path, as_lib = True)

    def test_void_func_def(self):
        hlsl_path = self._get_hlsl_path('test_void_func_def')
        with self._open_file(hlsl_path) as ps_file:
            sh = ps_6_0.Generator(ps_file)

            with sh.function('voidFunc')(a = sh.Float4, b = sh.Float4):
                sh.c = sh.a + sh.b
                sh.return_()

        self._compile(hlsl_path, as_lib = True)
