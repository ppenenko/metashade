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

def _generate_vs(vs_file, primitive):
    sh = profile.Generator(vs_file)
    attributes = primitive.attributes
    
    with sh.vs_input('VsIn') as VsIn:
        if attributes.POSITION is None:
            raise RuntimeError('POSITION attribute is mandatory')
        VsIn.position('Position', t.Point3f)

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

def main(gltf_dir, out_dir):
    os.makedirs(out_dir, exist_ok = True)

    for gltf_file in pathlib.Path(args.gltf_dir).glob('**/*.gltf'):
        print(gltf_file)
        gltf = GLTF2().load(gltf_file)

        for mesh in gltf.meshes:
            for primitive_idx, primitive in enumerate(mesh.primitives):
                vs_file_name = os.path.join(
                    out_dir,
                    '{mesh}-{i}-VS.hlsl'.format(
                        mesh = mesh.name, i = primitive_idx
                    )
                )
                with open(vs_file_name, 'w') as vs_file:
                    _generate_vs(vs_file, primitive)

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
