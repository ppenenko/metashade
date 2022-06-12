# Metashade
## What is Metashade?
Metashade is an experimental GPU shading domain-specific language (DSL) embedded in Python.
When a Metashade script executes, it generates code in a target shading language. Only HLSL is supported so far but the intent is definitely to support multiple targets.

## Why Metashade?
* Programming at a more abstract level than the target language:
    * Metaprogramming - think C++ templates but more flexible. Like any other Python code, Mestashade code is polymorphic at generation time.
This approach can replace the traditional ubershader practice, effectively replacing the C preprocessor with Python.
    * Stricter typing - e.g. a 3D point and an RGB color can be represented with different Metashade types, backed by the same data type in HLSL.
* Multi-language/cross-platform support.
Cross-compilation (e.g. with SPIRV-Cross) is an alternative but the code generation approach should offer higher flexibility around:
    * more divergent languages, e.g. HLSL vs OSL;
    * language dialects;
    * integration required by the specific host application (a shader fragment with a known interface, an effect file etc.).
* Integration with content pipeline scripts written in Python.

## How does it work?
Unlike some other Python DSLs, Metashade doesn't rely on introspection to translate the Python AST to the target language.
It uses more straight-forward mechanisms in hopes of making the DSL appear less magical to the user and enabling integration with arbitrary Python code:

* Operator overloading. Basically, `a + b` generates the respective operation in the target language instead of performing the addition in Python.
* Representing scopes in the target C-like language with `with` scopes in Python.
* `__getattr__()` and `__setattr__()` are used to initialize, modify and reference target variables in the current scope.
* C-like assignment by value is represented with assigment to a special data member `_`.

## Metashade in action
To see Metashade in action, check out the [glTF demo](gltfdemo).