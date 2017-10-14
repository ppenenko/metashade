class Target(object):
    def __init__(self, file):
        self._file = file
        self._indent = 0
        self._indent_char = '\t'
        self._indent_delta = 1
        
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
    
    def open_scope(self):
        self.write('{\n')
        self.push_indent()
        
    def close_scope(self):
        self.pop_indent()
        self.write('}\n')
        
    def return_(self, value):
        self.write('return {};\n'.format(value.get_ref()))

class BaseType(object):
    def __init__(self, initializer = None):
        self._identifier = None
        self._value = initializer
        
    def define(self, sh, identifier):
        self._identifier = identifier
        self._target = sh.get_target()
        self._target.write('{type_name} {identifier}{initializer};\n'.format(
            type_name = self.__class__._target_name,
            identifier = self._identifier,
            initializer = '' if self._value is None else ' = {}'.format(self._value) ))
        
    def get_ref(self):
        if self._identifier is not None:
            if self._value is None:
                raise RuntimeError('Variable is used before it has been assigned a value')
            
            return self._identifier
        
        elif self._value is not None:
            return self._value
        else:        
            raise RuntimeError('Instance is neiher a variable nor expression.')
        
    def __setattr__(self, name, value):
        if name == '_':
            self._value = value
            self._target.write('{identifier} = {value};\n'.format(
                identifier = self._identifier,
                value = value.get_ref() if hasattr(value, 'get_ref') else value ))
        else:
            object.__setattr__(self, name, value)  

class Float(BaseType):            
    def __add__(self, rhs):
        # TODO: handle implicit type conversions
        return self.__class__('{this} + {rhs}'.format(
            this = self.get_ref(), rhs = rhs.get_ref() )) 
        