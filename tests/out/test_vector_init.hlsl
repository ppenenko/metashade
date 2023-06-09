float vector_init(float3 rgb, float4 rgba)
{
	float f = 1;
	float2 f2 = f.xx;
	f2 = 2.xx;
	f2 = 0.xx;
	f2 = float2(0, 1);
	float3 f3 = f.xxx;
	f3 = 0.xxx;
	f3 = 2.xxx;
	f3 = float3(0, 1, 2);
	return f;
}

