import base

class Target(base.Target):
    pass

class Float(base.BaseType):
    def __init__(self, initializer):
        pass        
    
    def define(self, sh, name):
        self.sh = sh