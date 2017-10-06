import profiles.base

class Target(object):
    def __init__(self, file, profile):
        self.file = file
        
class BaseContext(object):
    def __init__(self, parent):
        self._parent = parent
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def __setattr__(self, name, value):        
        if isinstance(self.__dict__.get(name), profiles.base.BaseType):
            raise AttributeError('Metashade variable ' + name + ' is already defined.')
        
        if hasattr(value, 'define'):
            value.define(self, name)
            
        object.__setattr__(self, name, value)
    
    def return_(self, value):
        pass
    
class FunctionBody(BaseContext):
    def __init__(self, function):
        BaseContext.__init__(self, function._parent)
    
class Function(object):
    def __init__(self, parent):
        self._parent = parent
        
    def body(self):
        return FunctionBody(self)