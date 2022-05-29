Test coverage is currently far from complete. The HLSL Shader Model 5.0 generator is tested only. Our test cases follow [pytest](https://pytest.org/) conventions. Visual Studio Code sets up a pytest integration automagically.

Some of the test cases cover situations where the Metashade framework is supposed to gracefully handle logical errors in user scripts. Ideally, all such errors must be handled at generation time by raising Python exceptions, as opposed to compilation time. I.e. any shaders generated with Metashade without exceptions should compile. For such test cases, the [pytest.raises](ttps://docs.pytest.org/en/stable/reference/reference.html?highlight=raises#pytest.raises) pattern is used and no output HLSL file is generated.

Other tests are supposed to generate valid shaders. For these, we verify correctness with the following checks:
* The script has executed without Python exceptions.
* The output HLSL file is generated in the [out](./out) subdirectory, which makes it possible to:
    * Review the correctness of the generated code manually. The generated files are checked in to git, so if a Metashade code change leads to changes in the generated files, those changes can be analyzed with `git diff`. If a change appears to be non-breaking, purely cosmetic, then the new version should be "blessed" and committed to git.
    * Compile the file with [DXC](https://github.com/microsoft/DirectXShaderCompiler) as part of the test case (`dxc.exe` has to be in `PATH`).