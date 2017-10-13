import sys

import context
import profiles.hlsl as profile

def test_simple():
    target = profile.Target(sys.stderr)
    func = context.Function(target)
    
    with func.body() as sh:
        sh.a = profile.Float(1)
        #sh.Float(1).a
        #sh.Float('a', 1)
        #sh.c = sh.a + sh.b
        #sh.Float('c', sh.a + sh.b)
        
        sh.b = profile.Float(2)
        #sh.return_(sh.a + sh.b)
    
def test_double_definition():
    target = profile.Target(sys.stderr)
    func = context.Function(target)
    
    with func.body() as sh:
        sh.a = profile.Float(1)        
        try:
            sh.a = profile.Float(2)
        except AttributeError:
            pass
        else:
            assert False
                        
                