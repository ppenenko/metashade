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

import metashade.base.data_types as base

class BaseType(base.BaseType):
    @classmethod
    def _define_static(
        cls, sh, identifier,
        semantic = None, initializer = None, annotations = None
    ):
        sh._emit(
            '{type_name} {identifier}{semantic}'.format(
                type_name = cls.get_target_type_name(),
                identifier = identifier,
                semantic = '' if semantic is None \
                    else ' : {}'.format(semantic),
            )
        )

        if annotations is not None and annotations:
            sh._emit(' <\n')
            sh._push_indent()
            for annotation in annotations:
                sh._emit_indent()
                sh._emit('{};\n'.format(annotation))
            sh._pop_indent()
            sh._emit_indent()
            sh._emit('>')

        if initializer is not None:
            sh._emit(' = {}'.format(initializer))

    def _define(
        self, sh, identifier,
        semantic = None, allow_init = True, annotations = None
    ):
        self._bind(sh, identifier, allow_init)
        self.__class__._define_static(
            sh, self._name, initializer = self._expression,
            semantic = semantic, annotations = annotations
        )
        
    def __setattr__(self, name, value):
        if name == '_':
            self._expression = value
            self._sh._emit_indent()
            self._sh._emit(
                '{identifier} = {value};\n'.format(
                    identifier = self._name,
                    value = value.get_ref() if hasattr(value, 'get_ref') \
                        else value
                )
            )
        else:
            object.__setattr__(self, name, value)

    @classmethod
    def get_target_type_name(cls):
        try:
            return cls._target_name
        except AttributeError:
            return cls.__name__

class ArithmeticType(BaseType):
    def _binary_operator(self, rhs, op):
        return self.__class__(
            '({this} {op} {rhs})'.format(
                this = self.get_ref(), rhs = rhs.get_ref(), op = op
            )
        )

    def __add__(self, rhs):
        return self._binary_operator(rhs, '+')

    def __sub__(self, rhs):
        return self._binary_operator(rhs, '-')

    def __mul__(self, rhs):
        return self._binary_operator(rhs, '*')

    def __div__(self, rhs):
        return self._binary_operator(rhs, '/')

class Float(ArithmeticType):
    _target_name = 'float'