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

import filecmp, io, os, sys
from pathlib import Path
from metashade.hlsl.util import dxc

class RefDiffer:
    def __init__(self, ref_dir : Path, out_dir_env_var : str):
        self._ref_dir = ref_dir
        out_dir_env_var = os.getenv(out_dir_env_var, None)
        self._out_dir = (
            Path(out_dir_env_var).resolve() if out_dir_env_var is not None
            else self._ref_dir
        )
        os.makedirs(self._out_dir, exist_ok = True)

    def __call__(self, path : Path):
        if self._out_dir != self._ref_dir:
            assert filecmp.cmp(path, self._ref_dir / path.name)

class Base:
    @classmethod
    def setup_class(cls):
        cls._parent_dir = Path(sys.modules[cls.__module__].__file__).parent

        cls._ref_differ = RefDiffer(
            ref_dir = cls._parent_dir / 'ref',
            out_dir_env_var = 'METASHADE_PYTEST_OUT_DIR'
        )

    _entry_point_name = 'psMain'

    @classmethod
    def _get_out_path(cls, file_name : str, file_extension : str) -> str:
        return ( cls._ref_differ._out_dir / f'{file_name}.{file_extension}'
            if file_name is not None else None
        )

    @classmethod
    def _get_hlsl_path(cls, file_name : str) -> str:
        return cls._get_out_path(file_name, 'hlsl')
    
    @classmethod
    def _get_glsl_path(cls, file_name : str) -> str:
        return cls._get_out_path(file_name, 'glsl')

    @staticmethod
    def _open_file(hlsl_path : str = None):
        return ( open(hlsl_path, 'w')
            if hlsl_path is not None else io.StringIO()
        )

    @classmethod
    def _check_source(cls, hlsl_path, as_lib : bool = False):
        cls._ref_differ(hlsl_path)

        # LIB profiles support DXIL linking and therefore allow function
        # declarations without definitions.
        # Pure declarations may also be useful in other profiles if the
        # definition is found elsewhere in the compilation unit, e.g. in an
        # included header.
        dxc.compile(
            src_path = hlsl_path,
            entry_point_name = cls._entry_point_name,
            profile = 'lib_6_5' if as_lib else 'ps_6_0',
            include_paths = [ cls._parent_dir ]
        )