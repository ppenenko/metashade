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
    
    def open_scope(self):
        self.write('{\n')
        self.push_indent()
        
    def close_scope(self):
        self.pop_indent()
        self.write('}\n')
        
    def write(self, line):
        self._file.write(self.get_indent() + line)        

class BaseType(object):
    pass

class Float(BaseType):
    def __init__(self, initializer=None):
        self._initializer = initializer
    
    def define(self, sh, identifier):
        self._identifier = identifier
        self._sh = sh        
        self._target = sh.get_target()
        self._target.write('{type_name} {identifier}{initializer};\n'.format(
            type_name = self.__class__._target_name,
            identifier = self._identifier,
            initializer = '' if self._initializer is None else ' = {}'.format(self._initializer) ))
        
    def __add__(self, rhs):
        # TODO: handle implicit type conversions
        return self.__class__('{this} + {rhs}'.format(
            this = self._identifier, rhs = rhs._identifier )) 
        