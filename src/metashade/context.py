class Target:
    def __init__(self, file, profile):
        self.file = file
        
class BaseContext:
    def __init__(self, parent):
        self.parent = parent
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
class FunctionBody(BaseContext):
    def __init__(self, function):
        BaseContext.__init__(self, function.parent)
    
class Function:
    def __init__(self, parent):
        self.parent = parent
        
    def body(self):
        return FunctionBody(self)