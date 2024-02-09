
```Python
    sh // 'Create a float variable with the value of pi'
    sh.x = sh.Float(math.pi)
```

```HLSL
    // Create a float variable with the value of pi
    float x = 3.141592653589793;
```

```Python
    sh.rgba = sh.RgbaF(rgb = (0, 1, 0), a = 0)

    sh // 'Swizzling'
    sh.rgb = sh.rgba.rgb    # The result's type is deduced, a-la `auto` in modern C++, to `RgbF`

    sh // '...and write masking'
    sh.rgb.r = 1
```

```HLSL
    float4 rgba = float4(float3(0, 1, 0), 0);
	// Swizzling
	float3 rgb = rgba.rgb;
	// ...and write masking
	rgb.r = 1;
```

```Python
    sh // 'Dot product'
    sh.NdotL = sh.N @ sh.L
```

```HLSL
    // Dot product
    float NdotL = dot(N, L);
```

```Python
    sh // 'Some intrinsics'
    sh.N = sh.N.normalize()
```

```HLSL
    // Some intrinsics
    N = normalize(N);
```
