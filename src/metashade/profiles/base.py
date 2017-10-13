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
        self._file.write(self.get_indent() + '{\n')
        self.push_indent()
        
    def close_scope(self):
        self.pop_indent()
        self._file.write(self.get_indent() + '}\n')

class BaseType(object):
    pass