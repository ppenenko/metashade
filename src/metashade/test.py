import sys
import context
import profiles.hlsl as hlsl

def test_simple():
    target = context.Target(sys.stdout, hlsl.Profile)
    func = context.Function(target)
    
    with func.body() as sh:
        sh.a = sh.Float(1)
        sh.b = sh.Float(2)
        sh.return_(sh.a + sh.b)
    