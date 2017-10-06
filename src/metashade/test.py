import sys

import context
import profiles.hlsl as hlsl

def test_simple():
    target = context.Target(sys.stdout, hlsl.Profile)
    func = context.Function(target)
    
    with func.body() as sh:
        sh.a = hlsl.Float(1)
        #sh.Float(1).a
        #sh.Float('a', 1)
        #sh.c = sh.a + sh.b
        #sh.Float('c', sh.a + sh.b)
        
        sh.b = hlsl.Float(2)
        #sh.return_(sh.a + sh.b)
    
def test_double_definition():
    target = context.Target(sys.stdout, hlsl.Profile)
    func = context.Function(target)
    
    with func.body() as sh:
        sh.a = hlsl.Float(1)        
        try:
            sh.a = hlsl.Float(2)
        except AttributeError:
            pass
        else:
            assert False
                        
                