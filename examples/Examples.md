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

    sh // "The variable type is deduced below, a-la `auto` in C++"
    sh.color = sh.rgba.rgb
    sh.color.r = 1
```

```HLSL
    float4 rgba = float4(float3(0, 1, 0), 0);
	// The variable type is deduced below, a-la `auto` in C++
	float3 color = rgba.rgb;
	color.r = 1;
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