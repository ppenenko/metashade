# This is just a helper file to test example code snippets for Markdown
# and presentations.

import math
from metashade.hlsl.sm6 import ps_6_0 as hlsl_ps

with open('misc.hlsl', 'w') as hlsl_file:
    sh = hlsl_ps.Generator(hlsl_file)

    with sh.function('foo', sh.Float)(N = sh.Vector3f, L = sh.Vector3f):
        sh // 'Create a float variable with the value of pi'
        sh.x = sh.Float(math.pi)

        sh // 'Swizzling and write masking'
        sh.rgba = sh.RgbaF(rgb = (0, 1, 0), a = 0)

        sh // "The variable type is deduced below, a-la `auto` in C++"
        sh.color = sh.rgba.rgb
        sh.color.r = 1

        sh // 'Some intrinsics'
        sh.N = sh.N.normalize()

        sh // 'Dot product'
        sh.NdotL = sh.N @ sh.L

        sh.return_(sh.NdotL)

        # TODO:
        # texture-sampler combination and sampling
        # Comments
        # build abstractions on top, e.g. glTF textures in my demo

with open('fail.hlsl', 'w') as hlsl_file:
    sh = hlsl_ps.Generator(hlsl_file)
    with sh.function('foo')():
        sh.xyz = sh.rgba.xyz    # Exception: `RgbaF` has no attribute `xyz`
