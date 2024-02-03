from metashade.hlsl.sm6 import ps_6_0 as hlsl_ps
from metashade.glsl.v460 import frag as glsl_fs # hypothetical

def generate(sh):
    # Polymorphic shader code for multiple targets
    pass

with open('ps.hlsl', 'w') as hlsl_file:
    sh = hlsl_ps.Generator(hlsl_file)
    generate(sh)

with open('fs.glsl', 'w') as glsl_file:
    sh = glsl_fs.Generator(glsl_file)
    generate(sh)

