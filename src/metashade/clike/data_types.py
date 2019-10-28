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
    def _define_static(cls, sh, identifier, semantic=None, initializer=None):
        sh._write('{type_name} {identifier}{semantic}{initializer}'.format(
            type_name = cls.get_target_type_name(),
            identifier = identifier,
            semantic = '' if semantic is None \
                else ' : {}'.format(semantic),
            initializer = '' if initializer is None \
                else ' = {}'.format(initializer) ))

    def _define(self, sh, identifier, semantic=None, allow_init=True):
        self._bind(sh, identifier, allow_init)
        self.__class__._define_static(
            sh, self._name, self._expression, semantic)
        
    def __setattr__(self, name, value):
        if name == '_':
            self._expression = value
            self._sh._write('{identifier} = {value};\n'.format(
                identifier = self._name,
                value = value.get_ref() if hasattr(value, 'get_ref') else value ))
        else:
            object.__setattr__(self, name, value)

    @classmethod
    def get_target_type_name(cls):
        try:
            return cls._target_name
        except AttributeError:
            return cls.__name__

class AddMixIn(object):
    def __add__(self, rhs):
        return self.__class__('{this} + {rhs}'.format(
            this = self.get_ref(), rhs = rhs.get_ref() ))
        
class Float(BaseType, AddMixIn):
    pass