### Create a float variable with the value of pi

```Python
    sh.x = sh.Float(math.pi)
```

```HLSL
    float x = 3.141592653589793;
```

### Swizzling and write masking

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

### Dot product

```Python
    sh.NdotL = sh.N @ sh.L
```

```HLSL
    float NdotL = dot(N, L);
```

### Intrinsics

```Python
    sh.N = sh.N.normalize()
```

```HLSL
    N = normalize(N);
```

### Comments

```Python
    sh // 'This is a comment'
```
```HLSL
	// This is a comment
```