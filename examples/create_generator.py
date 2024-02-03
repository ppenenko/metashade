from metashade.hlsl.sm6 import ps_6_0

with open('ps.hlsl', 'w') as ps_file:
    sh = ps_6_0.Generator(ps_file)
    # Generate some code with `sh`
