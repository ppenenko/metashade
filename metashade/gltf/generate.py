# Copyright 2020 Pavlo Penenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse, os, pathlib
from pygltflib import GLTF2

import metashade.hlsl.profile as profile
import metashade.hlsl.data_types as t

def _generate_vs_out(sh):
    with sh.vs_output('VsOut') as VsOut:
        VsOut.SV_Position('Pclip', t.Vector4f)

def _generate_vs(vs_file, primitive):
    sh = profile.Generator(vs_file)

    with sh.uniform_buffer(register = 0, name = 'cbPerFrame'):
        sh.uniform('gWvpXf', t.Matrix4x4f)
        sh.uniform('gCameraPos', t.Vector4f)
        sh.uniform('gIblFactor', t.Float)
        sh.uniform('gEmissiveFactor', t.Float)

    attributes = primitive.attributes

    with sh.vs_input('VsIn') as VsIn:
        if attributes.POSITION is None:
            raise RuntimeError('POSITION attribute is mandatory')
        VsIn.position('Po', t.Point3f)

        if attributes.NORMAL is not None:
            VsIn.normal('Normal', t.Vector3f)

        if attributes.TANGENT is not None:
            VsIn.tangent('Tangent', t.Vector4f)

        if attributes.TEXCOORD_0 is not None:
            VsIn.texCoord('UV0', t.Point2f)

        if attributes.TEXCOORD_1 is not None:
            VsIn.texCoord('UV1', t.Point2f)

        if attributes.COLOR_0 is not None:
            VsIn.color('Color0', t.RgbaF)

        if attributes.JOINTS_0 is not None:
            raise RuntimeError('Unsupported attribute JOINTS_0')

        if attributes.WEIGHTS_0 is not None:
            raise RuntimeError('Unsupported attribute WEIGHTS_0')

    _generate_vs_out(sh)

    with sh.vs_main('mainVS', sh.VsOut)(vsIn = sh.VsIn):
        sh.vsOut = sh.VsOut()
        sh.vsOut.Pclip._ = sh.gWvpXf.xform(sh.vsIn.Po)
        
        sh.return_(sh.vsOut)

def _generate_ps(vs_file):
    sh = profile.Generator(vs_file)

    _generate_vs_out(sh)

    with sh.ps_output('PsOut') as PsOut:
        PsOut.SV_Target('color', t.RgbaF)
    
    with sh.ps_main('mainPS', sh.PsOut)(psIn = sh.VsOut):
        sh.psOut = sh.PsOut()
        sh.psOut.color._ = t.RgbaF(rgb = (1.0, 0.0, 1.0), a = 1.0)
        sh.return_(sh.psOut)

def main(gltf_dir, out_dir):
    os.makedirs(out_dir, exist_ok = True)

    for gltf_file in pathlib.Path(args.gltf_dir).glob('**/*.gltf'):
        print(gltf_file)
        gltf = GLTF2().load(gltf_file)

        for mesh in gltf.meshes:
            for primitive_idx, primitive in enumerate(mesh.primitives):
                def _file_name(stage : str):
                    return os.path.join(
                        out_dir,
                        '{mesh}-{i}-{stage}.hlsl'.format(
                            mesh = mesh.name,
                            i = primitive_idx,
                            stage = stage
                        )
                    )
                with open(_file_name("VS"), 'w') as vs_file:
                    _generate_vs(vs_file, primitive)

                with open(_file_name("PS"), 'w') as ps_file:
                    _generate_ps(ps_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Generate shaders from glTF materials."
    )
    parser.add_argument("--gltf-dir", help = "Path to the source glTF assets")
    parser.add_argument("--out-dir", help = "Path to the output directory")
    args = parser.parse_args()
    
    if not os.path.isdir(args.gltf_dir):
        raise NotADirectoryError(args.gltf_dir)

    main(args.gltf_dir, args.out_dir)
