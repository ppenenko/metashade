cbuffer cb : register(b0)
{
	float g_f;
	float1 g_f1;
	float2 g_f2;
	float3 g_f3;
	float4 g_f4;
	float1x1 g_f1x1;
	float1x2 g_f1x2;
	float1x3 g_f1x3;
	float1x4 g_f1x4;
	float2x1 g_f2x1;
	float2x2 g_f2x2;
	float2x3 g_f2x3;
	float2x4 g_f2x4;
	float3x1 g_f3x1;
	float3x2 g_f3x2;
	float3x3 g_f3x3;
	float3x4 g_f3x4;
	float4x1 g_f4x1;
	float4x2 g_f4x2;
	float4x3 g_f4x3;
	float4x4 g_f4x4;
};

float test_EvaluateAttributeCentroid_Float()
{
	float f_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f);
	return f_EvaluateAttributeCentroid;
}

float1 test_EvaluateAttributeCentroid_Float1()
{
	float1 f1_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f1);
	return f1_EvaluateAttributeCentroid;
}

float2 test_EvaluateAttributeCentroid_Float2()
{
	float2 f2_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f2);
	return f2_EvaluateAttributeCentroid;
}

float3 test_EvaluateAttributeCentroid_Float3()
{
	float3 f3_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f3);
	return f3_EvaluateAttributeCentroid;
}

float4 test_EvaluateAttributeCentroid_Float4()
{
	float4 f4_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f4);
	return f4_EvaluateAttributeCentroid;
}

float1x1 test_EvaluateAttributeCentroid_Float1x1()
{
	float1x1 f1x1_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f1x1);
	return f1x1_EvaluateAttributeCentroid;
}

float1x2 test_EvaluateAttributeCentroid_Float1x2()
{
	float1x2 f1x2_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f1x2);
	return f1x2_EvaluateAttributeCentroid;
}

float1x3 test_EvaluateAttributeCentroid_Float1x3()
{
	float1x3 f1x3_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f1x3);
	return f1x3_EvaluateAttributeCentroid;
}

float1x4 test_EvaluateAttributeCentroid_Float1x4()
{
	float1x4 f1x4_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f1x4);
	return f1x4_EvaluateAttributeCentroid;
}

float2x1 test_EvaluateAttributeCentroid_Float2x1()
{
	float2x1 f2x1_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f2x1);
	return f2x1_EvaluateAttributeCentroid;
}

float2x2 test_EvaluateAttributeCentroid_Float2x2()
{
	float2x2 f2x2_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f2x2);
	return f2x2_EvaluateAttributeCentroid;
}

float2x3 test_EvaluateAttributeCentroid_Float2x3()
{
	float2x3 f2x3_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f2x3);
	return f2x3_EvaluateAttributeCentroid;
}

float2x4 test_EvaluateAttributeCentroid_Float2x4()
{
	float2x4 f2x4_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f2x4);
	return f2x4_EvaluateAttributeCentroid;
}

float3x1 test_EvaluateAttributeCentroid_Float3x1()
{
	float3x1 f3x1_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f3x1);
	return f3x1_EvaluateAttributeCentroid;
}

float3x2 test_EvaluateAttributeCentroid_Float3x2()
{
	float3x2 f3x2_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f3x2);
	return f3x2_EvaluateAttributeCentroid;
}

float3x3 test_EvaluateAttributeCentroid_Float3x3()
{
	float3x3 f3x3_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f3x3);
	return f3x3_EvaluateAttributeCentroid;
}

float3x4 test_EvaluateAttributeCentroid_Float3x4()
{
	float3x4 f3x4_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f3x4);
	return f3x4_EvaluateAttributeCentroid;
}

float4x1 test_EvaluateAttributeCentroid_Float4x1()
{
	float4x1 f4x1_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f4x1);
	return f4x1_EvaluateAttributeCentroid;
}

float4x2 test_EvaluateAttributeCentroid_Float4x2()
{
	float4x2 f4x2_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f4x2);
	return f4x2_EvaluateAttributeCentroid;
}

float4x3 test_EvaluateAttributeCentroid_Float4x3()
{
	float4x3 f4x3_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f4x3);
	return f4x3_EvaluateAttributeCentroid;
}

float4x4 test_EvaluateAttributeCentroid_Float4x4()
{
	float4x4 f4x4_EvaluateAttributeCentroid = EvaluateAttributeCentroid(g_f4x4);
	return f4x4_EvaluateAttributeCentroid;
}

float test_QuadReadAcrossDiagonal_Float()
{
	float f_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f);
	return f_QuadReadAcrossDiagonal;
}

float1 test_QuadReadAcrossDiagonal_Float1()
{
	float1 f1_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f1);
	return f1_QuadReadAcrossDiagonal;
}

float2 test_QuadReadAcrossDiagonal_Float2()
{
	float2 f2_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f2);
	return f2_QuadReadAcrossDiagonal;
}

float3 test_QuadReadAcrossDiagonal_Float3()
{
	float3 f3_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f3);
	return f3_QuadReadAcrossDiagonal;
}

float4 test_QuadReadAcrossDiagonal_Float4()
{
	float4 f4_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f4);
	return f4_QuadReadAcrossDiagonal;
}

float1x1 test_QuadReadAcrossDiagonal_Float1x1()
{
	float1x1 f1x1_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f1x1);
	return f1x1_QuadReadAcrossDiagonal;
}

float1x2 test_QuadReadAcrossDiagonal_Float1x2()
{
	float1x2 f1x2_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f1x2);
	return f1x2_QuadReadAcrossDiagonal;
}

float1x3 test_QuadReadAcrossDiagonal_Float1x3()
{
	float1x3 f1x3_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f1x3);
	return f1x3_QuadReadAcrossDiagonal;
}

float1x4 test_QuadReadAcrossDiagonal_Float1x4()
{
	float1x4 f1x4_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f1x4);
	return f1x4_QuadReadAcrossDiagonal;
}

float2x1 test_QuadReadAcrossDiagonal_Float2x1()
{
	float2x1 f2x1_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f2x1);
	return f2x1_QuadReadAcrossDiagonal;
}

float2x2 test_QuadReadAcrossDiagonal_Float2x2()
{
	float2x2 f2x2_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f2x2);
	return f2x2_QuadReadAcrossDiagonal;
}

float2x3 test_QuadReadAcrossDiagonal_Float2x3()
{
	float2x3 f2x3_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f2x3);
	return f2x3_QuadReadAcrossDiagonal;
}

float2x4 test_QuadReadAcrossDiagonal_Float2x4()
{
	float2x4 f2x4_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f2x4);
	return f2x4_QuadReadAcrossDiagonal;
}

float3x1 test_QuadReadAcrossDiagonal_Float3x1()
{
	float3x1 f3x1_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f3x1);
	return f3x1_QuadReadAcrossDiagonal;
}

float3x2 test_QuadReadAcrossDiagonal_Float3x2()
{
	float3x2 f3x2_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f3x2);
	return f3x2_QuadReadAcrossDiagonal;
}

float3x3 test_QuadReadAcrossDiagonal_Float3x3()
{
	float3x3 f3x3_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f3x3);
	return f3x3_QuadReadAcrossDiagonal;
}

float3x4 test_QuadReadAcrossDiagonal_Float3x4()
{
	float3x4 f3x4_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f3x4);
	return f3x4_QuadReadAcrossDiagonal;
}

float4x1 test_QuadReadAcrossDiagonal_Float4x1()
{
	float4x1 f4x1_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f4x1);
	return f4x1_QuadReadAcrossDiagonal;
}

float4x2 test_QuadReadAcrossDiagonal_Float4x2()
{
	float4x2 f4x2_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f4x2);
	return f4x2_QuadReadAcrossDiagonal;
}

float4x3 test_QuadReadAcrossDiagonal_Float4x3()
{
	float4x3 f4x3_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f4x3);
	return f4x3_QuadReadAcrossDiagonal;
}

float4x4 test_QuadReadAcrossDiagonal_Float4x4()
{
	float4x4 f4x4_QuadReadAcrossDiagonal = QuadReadAcrossDiagonal(g_f4x4);
	return f4x4_QuadReadAcrossDiagonal;
}

float test_QuadReadAcrossX_Float()
{
	float f_QuadReadAcrossX = QuadReadAcrossX(g_f);
	return f_QuadReadAcrossX;
}

float1 test_QuadReadAcrossX_Float1()
{
	float1 f1_QuadReadAcrossX = QuadReadAcrossX(g_f1);
	return f1_QuadReadAcrossX;
}

float2 test_QuadReadAcrossX_Float2()
{
	float2 f2_QuadReadAcrossX = QuadReadAcrossX(g_f2);
	return f2_QuadReadAcrossX;
}

float3 test_QuadReadAcrossX_Float3()
{
	float3 f3_QuadReadAcrossX = QuadReadAcrossX(g_f3);
	return f3_QuadReadAcrossX;
}

float4 test_QuadReadAcrossX_Float4()
{
	float4 f4_QuadReadAcrossX = QuadReadAcrossX(g_f4);
	return f4_QuadReadAcrossX;
}

float1x1 test_QuadReadAcrossX_Float1x1()
{
	float1x1 f1x1_QuadReadAcrossX = QuadReadAcrossX(g_f1x1);
	return f1x1_QuadReadAcrossX;
}

float1x2 test_QuadReadAcrossX_Float1x2()
{
	float1x2 f1x2_QuadReadAcrossX = QuadReadAcrossX(g_f1x2);
	return f1x2_QuadReadAcrossX;
}

float1x3 test_QuadReadAcrossX_Float1x3()
{
	float1x3 f1x3_QuadReadAcrossX = QuadReadAcrossX(g_f1x3);
	return f1x3_QuadReadAcrossX;
}

float1x4 test_QuadReadAcrossX_Float1x4()
{
	float1x4 f1x4_QuadReadAcrossX = QuadReadAcrossX(g_f1x4);
	return f1x4_QuadReadAcrossX;
}

float2x1 test_QuadReadAcrossX_Float2x1()
{
	float2x1 f2x1_QuadReadAcrossX = QuadReadAcrossX(g_f2x1);
	return f2x1_QuadReadAcrossX;
}

float2x2 test_QuadReadAcrossX_Float2x2()
{
	float2x2 f2x2_QuadReadAcrossX = QuadReadAcrossX(g_f2x2);
	return f2x2_QuadReadAcrossX;
}

float2x3 test_QuadReadAcrossX_Float2x3()
{
	float2x3 f2x3_QuadReadAcrossX = QuadReadAcrossX(g_f2x3);
	return f2x3_QuadReadAcrossX;
}

float2x4 test_QuadReadAcrossX_Float2x4()
{
	float2x4 f2x4_QuadReadAcrossX = QuadReadAcrossX(g_f2x4);
	return f2x4_QuadReadAcrossX;
}

float3x1 test_QuadReadAcrossX_Float3x1()
{
	float3x1 f3x1_QuadReadAcrossX = QuadReadAcrossX(g_f3x1);
	return f3x1_QuadReadAcrossX;
}

float3x2 test_QuadReadAcrossX_Float3x2()
{
	float3x2 f3x2_QuadReadAcrossX = QuadReadAcrossX(g_f3x2);
	return f3x2_QuadReadAcrossX;
}

float3x3 test_QuadReadAcrossX_Float3x3()
{
	float3x3 f3x3_QuadReadAcrossX = QuadReadAcrossX(g_f3x3);
	return f3x3_QuadReadAcrossX;
}

float3x4 test_QuadReadAcrossX_Float3x4()
{
	float3x4 f3x4_QuadReadAcrossX = QuadReadAcrossX(g_f3x4);
	return f3x4_QuadReadAcrossX;
}

float4x1 test_QuadReadAcrossX_Float4x1()
{
	float4x1 f4x1_QuadReadAcrossX = QuadReadAcrossX(g_f4x1);
	return f4x1_QuadReadAcrossX;
}

float4x2 test_QuadReadAcrossX_Float4x2()
{
	float4x2 f4x2_QuadReadAcrossX = QuadReadAcrossX(g_f4x2);
	return f4x2_QuadReadAcrossX;
}

float4x3 test_QuadReadAcrossX_Float4x3()
{
	float4x3 f4x3_QuadReadAcrossX = QuadReadAcrossX(g_f4x3);
	return f4x3_QuadReadAcrossX;
}

float4x4 test_QuadReadAcrossX_Float4x4()
{
	float4x4 f4x4_QuadReadAcrossX = QuadReadAcrossX(g_f4x4);
	return f4x4_QuadReadAcrossX;
}

float test_QuadReadAcrossY_Float()
{
	float f_QuadReadAcrossY = QuadReadAcrossY(g_f);
	return f_QuadReadAcrossY;
}

float1 test_QuadReadAcrossY_Float1()
{
	float1 f1_QuadReadAcrossY = QuadReadAcrossY(g_f1);
	return f1_QuadReadAcrossY;
}

float2 test_QuadReadAcrossY_Float2()
{
	float2 f2_QuadReadAcrossY = QuadReadAcrossY(g_f2);
	return f2_QuadReadAcrossY;
}

float3 test_QuadReadAcrossY_Float3()
{
	float3 f3_QuadReadAcrossY = QuadReadAcrossY(g_f3);
	return f3_QuadReadAcrossY;
}

float4 test_QuadReadAcrossY_Float4()
{
	float4 f4_QuadReadAcrossY = QuadReadAcrossY(g_f4);
	return f4_QuadReadAcrossY;
}

float1x1 test_QuadReadAcrossY_Float1x1()
{
	float1x1 f1x1_QuadReadAcrossY = QuadReadAcrossY(g_f1x1);
	return f1x1_QuadReadAcrossY;
}

float1x2 test_QuadReadAcrossY_Float1x2()
{
	float1x2 f1x2_QuadReadAcrossY = QuadReadAcrossY(g_f1x2);
	return f1x2_QuadReadAcrossY;
}

float1x3 test_QuadReadAcrossY_Float1x3()
{
	float1x3 f1x3_QuadReadAcrossY = QuadReadAcrossY(g_f1x3);
	return f1x3_QuadReadAcrossY;
}

float1x4 test_QuadReadAcrossY_Float1x4()
{
	float1x4 f1x4_QuadReadAcrossY = QuadReadAcrossY(g_f1x4);
	return f1x4_QuadReadAcrossY;
}

float2x1 test_QuadReadAcrossY_Float2x1()
{
	float2x1 f2x1_QuadReadAcrossY = QuadReadAcrossY(g_f2x1);
	return f2x1_QuadReadAcrossY;
}

float2x2 test_QuadReadAcrossY_Float2x2()
{
	float2x2 f2x2_QuadReadAcrossY = QuadReadAcrossY(g_f2x2);
	return f2x2_QuadReadAcrossY;
}

float2x3 test_QuadReadAcrossY_Float2x3()
{
	float2x3 f2x3_QuadReadAcrossY = QuadReadAcrossY(g_f2x3);
	return f2x3_QuadReadAcrossY;
}

float2x4 test_QuadReadAcrossY_Float2x4()
{
	float2x4 f2x4_QuadReadAcrossY = QuadReadAcrossY(g_f2x4);
	return f2x4_QuadReadAcrossY;
}

float3x1 test_QuadReadAcrossY_Float3x1()
{
	float3x1 f3x1_QuadReadAcrossY = QuadReadAcrossY(g_f3x1);
	return f3x1_QuadReadAcrossY;
}

float3x2 test_QuadReadAcrossY_Float3x2()
{
	float3x2 f3x2_QuadReadAcrossY = QuadReadAcrossY(g_f3x2);
	return f3x2_QuadReadAcrossY;
}

float3x3 test_QuadReadAcrossY_Float3x3()
{
	float3x3 f3x3_QuadReadAcrossY = QuadReadAcrossY(g_f3x3);
	return f3x3_QuadReadAcrossY;
}

float3x4 test_QuadReadAcrossY_Float3x4()
{
	float3x4 f3x4_QuadReadAcrossY = QuadReadAcrossY(g_f3x4);
	return f3x4_QuadReadAcrossY;
}

float4x1 test_QuadReadAcrossY_Float4x1()
{
	float4x1 f4x1_QuadReadAcrossY = QuadReadAcrossY(g_f4x1);
	return f4x1_QuadReadAcrossY;
}

float4x2 test_QuadReadAcrossY_Float4x2()
{
	float4x2 f4x2_QuadReadAcrossY = QuadReadAcrossY(g_f4x2);
	return f4x2_QuadReadAcrossY;
}

float4x3 test_QuadReadAcrossY_Float4x3()
{
	float4x3 f4x3_QuadReadAcrossY = QuadReadAcrossY(g_f4x3);
	return f4x3_QuadReadAcrossY;
}

float4x4 test_QuadReadAcrossY_Float4x4()
{
	float4x4 f4x4_QuadReadAcrossY = QuadReadAcrossY(g_f4x4);
	return f4x4_QuadReadAcrossY;
}

float test_WaveActiveMax_Float()
{
	float f_WaveActiveMax = WaveActiveMax(g_f);
	return f_WaveActiveMax;
}

float1 test_WaveActiveMax_Float1()
{
	float1 f1_WaveActiveMax = WaveActiveMax(g_f1);
	return f1_WaveActiveMax;
}

float2 test_WaveActiveMax_Float2()
{
	float2 f2_WaveActiveMax = WaveActiveMax(g_f2);
	return f2_WaveActiveMax;
}

float3 test_WaveActiveMax_Float3()
{
	float3 f3_WaveActiveMax = WaveActiveMax(g_f3);
	return f3_WaveActiveMax;
}

float4 test_WaveActiveMax_Float4()
{
	float4 f4_WaveActiveMax = WaveActiveMax(g_f4);
	return f4_WaveActiveMax;
}

float1x1 test_WaveActiveMax_Float1x1()
{
	float1x1 f1x1_WaveActiveMax = WaveActiveMax(g_f1x1);
	return f1x1_WaveActiveMax;
}

float1x2 test_WaveActiveMax_Float1x2()
{
	float1x2 f1x2_WaveActiveMax = WaveActiveMax(g_f1x2);
	return f1x2_WaveActiveMax;
}

float1x3 test_WaveActiveMax_Float1x3()
{
	float1x3 f1x3_WaveActiveMax = WaveActiveMax(g_f1x3);
	return f1x3_WaveActiveMax;
}

float1x4 test_WaveActiveMax_Float1x4()
{
	float1x4 f1x4_WaveActiveMax = WaveActiveMax(g_f1x4);
	return f1x4_WaveActiveMax;
}

float2x1 test_WaveActiveMax_Float2x1()
{
	float2x1 f2x1_WaveActiveMax = WaveActiveMax(g_f2x1);
	return f2x1_WaveActiveMax;
}

float2x2 test_WaveActiveMax_Float2x2()
{
	float2x2 f2x2_WaveActiveMax = WaveActiveMax(g_f2x2);
	return f2x2_WaveActiveMax;
}

float2x3 test_WaveActiveMax_Float2x3()
{
	float2x3 f2x3_WaveActiveMax = WaveActiveMax(g_f2x3);
	return f2x3_WaveActiveMax;
}

float2x4 test_WaveActiveMax_Float2x4()
{
	float2x4 f2x4_WaveActiveMax = WaveActiveMax(g_f2x4);
	return f2x4_WaveActiveMax;
}

float3x1 test_WaveActiveMax_Float3x1()
{
	float3x1 f3x1_WaveActiveMax = WaveActiveMax(g_f3x1);
	return f3x1_WaveActiveMax;
}

float3x2 test_WaveActiveMax_Float3x2()
{
	float3x2 f3x2_WaveActiveMax = WaveActiveMax(g_f3x2);
	return f3x2_WaveActiveMax;
}

float3x3 test_WaveActiveMax_Float3x3()
{
	float3x3 f3x3_WaveActiveMax = WaveActiveMax(g_f3x3);
	return f3x3_WaveActiveMax;
}

float3x4 test_WaveActiveMax_Float3x4()
{
	float3x4 f3x4_WaveActiveMax = WaveActiveMax(g_f3x4);
	return f3x4_WaveActiveMax;
}

float4x1 test_WaveActiveMax_Float4x1()
{
	float4x1 f4x1_WaveActiveMax = WaveActiveMax(g_f4x1);
	return f4x1_WaveActiveMax;
}

float4x2 test_WaveActiveMax_Float4x2()
{
	float4x2 f4x2_WaveActiveMax = WaveActiveMax(g_f4x2);
	return f4x2_WaveActiveMax;
}

float4x3 test_WaveActiveMax_Float4x3()
{
	float4x3 f4x3_WaveActiveMax = WaveActiveMax(g_f4x3);
	return f4x3_WaveActiveMax;
}

float4x4 test_WaveActiveMax_Float4x4()
{
	float4x4 f4x4_WaveActiveMax = WaveActiveMax(g_f4x4);
	return f4x4_WaveActiveMax;
}

float test_WaveActiveMin_Float()
{
	float f_WaveActiveMin = WaveActiveMin(g_f);
	return f_WaveActiveMin;
}

float1 test_WaveActiveMin_Float1()
{
	float1 f1_WaveActiveMin = WaveActiveMin(g_f1);
	return f1_WaveActiveMin;
}

float2 test_WaveActiveMin_Float2()
{
	float2 f2_WaveActiveMin = WaveActiveMin(g_f2);
	return f2_WaveActiveMin;
}

float3 test_WaveActiveMin_Float3()
{
	float3 f3_WaveActiveMin = WaveActiveMin(g_f3);
	return f3_WaveActiveMin;
}

float4 test_WaveActiveMin_Float4()
{
	float4 f4_WaveActiveMin = WaveActiveMin(g_f4);
	return f4_WaveActiveMin;
}

float1x1 test_WaveActiveMin_Float1x1()
{
	float1x1 f1x1_WaveActiveMin = WaveActiveMin(g_f1x1);
	return f1x1_WaveActiveMin;
}

float1x2 test_WaveActiveMin_Float1x2()
{
	float1x2 f1x2_WaveActiveMin = WaveActiveMin(g_f1x2);
	return f1x2_WaveActiveMin;
}

float1x3 test_WaveActiveMin_Float1x3()
{
	float1x3 f1x3_WaveActiveMin = WaveActiveMin(g_f1x3);
	return f1x3_WaveActiveMin;
}

float1x4 test_WaveActiveMin_Float1x4()
{
	float1x4 f1x4_WaveActiveMin = WaveActiveMin(g_f1x4);
	return f1x4_WaveActiveMin;
}

float2x1 test_WaveActiveMin_Float2x1()
{
	float2x1 f2x1_WaveActiveMin = WaveActiveMin(g_f2x1);
	return f2x1_WaveActiveMin;
}

float2x2 test_WaveActiveMin_Float2x2()
{
	float2x2 f2x2_WaveActiveMin = WaveActiveMin(g_f2x2);
	return f2x2_WaveActiveMin;
}

float2x3 test_WaveActiveMin_Float2x3()
{
	float2x3 f2x3_WaveActiveMin = WaveActiveMin(g_f2x3);
	return f2x3_WaveActiveMin;
}

float2x4 test_WaveActiveMin_Float2x4()
{
	float2x4 f2x4_WaveActiveMin = WaveActiveMin(g_f2x4);
	return f2x4_WaveActiveMin;
}

float3x1 test_WaveActiveMin_Float3x1()
{
	float3x1 f3x1_WaveActiveMin = WaveActiveMin(g_f3x1);
	return f3x1_WaveActiveMin;
}

float3x2 test_WaveActiveMin_Float3x2()
{
	float3x2 f3x2_WaveActiveMin = WaveActiveMin(g_f3x2);
	return f3x2_WaveActiveMin;
}

float3x3 test_WaveActiveMin_Float3x3()
{
	float3x3 f3x3_WaveActiveMin = WaveActiveMin(g_f3x3);
	return f3x3_WaveActiveMin;
}

float3x4 test_WaveActiveMin_Float3x4()
{
	float3x4 f3x4_WaveActiveMin = WaveActiveMin(g_f3x4);
	return f3x4_WaveActiveMin;
}

float4x1 test_WaveActiveMin_Float4x1()
{
	float4x1 f4x1_WaveActiveMin = WaveActiveMin(g_f4x1);
	return f4x1_WaveActiveMin;
}

float4x2 test_WaveActiveMin_Float4x2()
{
	float4x2 f4x2_WaveActiveMin = WaveActiveMin(g_f4x2);
	return f4x2_WaveActiveMin;
}

float4x3 test_WaveActiveMin_Float4x3()
{
	float4x3 f4x3_WaveActiveMin = WaveActiveMin(g_f4x3);
	return f4x3_WaveActiveMin;
}

float4x4 test_WaveActiveMin_Float4x4()
{
	float4x4 f4x4_WaveActiveMin = WaveActiveMin(g_f4x4);
	return f4x4_WaveActiveMin;
}

float test_WaveActiveProduct_Float()
{
	float f_WaveActiveProduct = WaveActiveProduct(g_f);
	return f_WaveActiveProduct;
}

float1 test_WaveActiveProduct_Float1()
{
	float1 f1_WaveActiveProduct = WaveActiveProduct(g_f1);
	return f1_WaveActiveProduct;
}

float2 test_WaveActiveProduct_Float2()
{
	float2 f2_WaveActiveProduct = WaveActiveProduct(g_f2);
	return f2_WaveActiveProduct;
}

float3 test_WaveActiveProduct_Float3()
{
	float3 f3_WaveActiveProduct = WaveActiveProduct(g_f3);
	return f3_WaveActiveProduct;
}

float4 test_WaveActiveProduct_Float4()
{
	float4 f4_WaveActiveProduct = WaveActiveProduct(g_f4);
	return f4_WaveActiveProduct;
}

float1x1 test_WaveActiveProduct_Float1x1()
{
	float1x1 f1x1_WaveActiveProduct = WaveActiveProduct(g_f1x1);
	return f1x1_WaveActiveProduct;
}

float1x2 test_WaveActiveProduct_Float1x2()
{
	float1x2 f1x2_WaveActiveProduct = WaveActiveProduct(g_f1x2);
	return f1x2_WaveActiveProduct;
}

float1x3 test_WaveActiveProduct_Float1x3()
{
	float1x3 f1x3_WaveActiveProduct = WaveActiveProduct(g_f1x3);
	return f1x3_WaveActiveProduct;
}

float1x4 test_WaveActiveProduct_Float1x4()
{
	float1x4 f1x4_WaveActiveProduct = WaveActiveProduct(g_f1x4);
	return f1x4_WaveActiveProduct;
}

float2x1 test_WaveActiveProduct_Float2x1()
{
	float2x1 f2x1_WaveActiveProduct = WaveActiveProduct(g_f2x1);
	return f2x1_WaveActiveProduct;
}

float2x2 test_WaveActiveProduct_Float2x2()
{
	float2x2 f2x2_WaveActiveProduct = WaveActiveProduct(g_f2x2);
	return f2x2_WaveActiveProduct;
}

float2x3 test_WaveActiveProduct_Float2x3()
{
	float2x3 f2x3_WaveActiveProduct = WaveActiveProduct(g_f2x3);
	return f2x3_WaveActiveProduct;
}

float2x4 test_WaveActiveProduct_Float2x4()
{
	float2x4 f2x4_WaveActiveProduct = WaveActiveProduct(g_f2x4);
	return f2x4_WaveActiveProduct;
}

float3x1 test_WaveActiveProduct_Float3x1()
{
	float3x1 f3x1_WaveActiveProduct = WaveActiveProduct(g_f3x1);
	return f3x1_WaveActiveProduct;
}

float3x2 test_WaveActiveProduct_Float3x2()
{
	float3x2 f3x2_WaveActiveProduct = WaveActiveProduct(g_f3x2);
	return f3x2_WaveActiveProduct;
}

float3x3 test_WaveActiveProduct_Float3x3()
{
	float3x3 f3x3_WaveActiveProduct = WaveActiveProduct(g_f3x3);
	return f3x3_WaveActiveProduct;
}

float3x4 test_WaveActiveProduct_Float3x4()
{
	float3x4 f3x4_WaveActiveProduct = WaveActiveProduct(g_f3x4);
	return f3x4_WaveActiveProduct;
}

float4x1 test_WaveActiveProduct_Float4x1()
{
	float4x1 f4x1_WaveActiveProduct = WaveActiveProduct(g_f4x1);
	return f4x1_WaveActiveProduct;
}

float4x2 test_WaveActiveProduct_Float4x2()
{
	float4x2 f4x2_WaveActiveProduct = WaveActiveProduct(g_f4x2);
	return f4x2_WaveActiveProduct;
}

float4x3 test_WaveActiveProduct_Float4x3()
{
	float4x3 f4x3_WaveActiveProduct = WaveActiveProduct(g_f4x3);
	return f4x3_WaveActiveProduct;
}

float4x4 test_WaveActiveProduct_Float4x4()
{
	float4x4 f4x4_WaveActiveProduct = WaveActiveProduct(g_f4x4);
	return f4x4_WaveActiveProduct;
}

float test_WaveActiveSum_Float()
{
	float f_WaveActiveSum = WaveActiveSum(g_f);
	return f_WaveActiveSum;
}

float1 test_WaveActiveSum_Float1()
{
	float1 f1_WaveActiveSum = WaveActiveSum(g_f1);
	return f1_WaveActiveSum;
}

float2 test_WaveActiveSum_Float2()
{
	float2 f2_WaveActiveSum = WaveActiveSum(g_f2);
	return f2_WaveActiveSum;
}

float3 test_WaveActiveSum_Float3()
{
	float3 f3_WaveActiveSum = WaveActiveSum(g_f3);
	return f3_WaveActiveSum;
}

float4 test_WaveActiveSum_Float4()
{
	float4 f4_WaveActiveSum = WaveActiveSum(g_f4);
	return f4_WaveActiveSum;
}

float1x1 test_WaveActiveSum_Float1x1()
{
	float1x1 f1x1_WaveActiveSum = WaveActiveSum(g_f1x1);
	return f1x1_WaveActiveSum;
}

float1x2 test_WaveActiveSum_Float1x2()
{
	float1x2 f1x2_WaveActiveSum = WaveActiveSum(g_f1x2);
	return f1x2_WaveActiveSum;
}

float1x3 test_WaveActiveSum_Float1x3()
{
	float1x3 f1x3_WaveActiveSum = WaveActiveSum(g_f1x3);
	return f1x3_WaveActiveSum;
}

float1x4 test_WaveActiveSum_Float1x4()
{
	float1x4 f1x4_WaveActiveSum = WaveActiveSum(g_f1x4);
	return f1x4_WaveActiveSum;
}

float2x1 test_WaveActiveSum_Float2x1()
{
	float2x1 f2x1_WaveActiveSum = WaveActiveSum(g_f2x1);
	return f2x1_WaveActiveSum;
}

float2x2 test_WaveActiveSum_Float2x2()
{
	float2x2 f2x2_WaveActiveSum = WaveActiveSum(g_f2x2);
	return f2x2_WaveActiveSum;
}

float2x3 test_WaveActiveSum_Float2x3()
{
	float2x3 f2x3_WaveActiveSum = WaveActiveSum(g_f2x3);
	return f2x3_WaveActiveSum;
}

float2x4 test_WaveActiveSum_Float2x4()
{
	float2x4 f2x4_WaveActiveSum = WaveActiveSum(g_f2x4);
	return f2x4_WaveActiveSum;
}

float3x1 test_WaveActiveSum_Float3x1()
{
	float3x1 f3x1_WaveActiveSum = WaveActiveSum(g_f3x1);
	return f3x1_WaveActiveSum;
}

float3x2 test_WaveActiveSum_Float3x2()
{
	float3x2 f3x2_WaveActiveSum = WaveActiveSum(g_f3x2);
	return f3x2_WaveActiveSum;
}

float3x3 test_WaveActiveSum_Float3x3()
{
	float3x3 f3x3_WaveActiveSum = WaveActiveSum(g_f3x3);
	return f3x3_WaveActiveSum;
}

float3x4 test_WaveActiveSum_Float3x4()
{
	float3x4 f3x4_WaveActiveSum = WaveActiveSum(g_f3x4);
	return f3x4_WaveActiveSum;
}

float4x1 test_WaveActiveSum_Float4x1()
{
	float4x1 f4x1_WaveActiveSum = WaveActiveSum(g_f4x1);
	return f4x1_WaveActiveSum;
}

float4x2 test_WaveActiveSum_Float4x2()
{
	float4x2 f4x2_WaveActiveSum = WaveActiveSum(g_f4x2);
	return f4x2_WaveActiveSum;
}

float4x3 test_WaveActiveSum_Float4x3()
{
	float4x3 f4x3_WaveActiveSum = WaveActiveSum(g_f4x3);
	return f4x3_WaveActiveSum;
}

float4x4 test_WaveActiveSum_Float4x4()
{
	float4x4 f4x4_WaveActiveSum = WaveActiveSum(g_f4x4);
	return f4x4_WaveActiveSum;
}

float test_WavePrefixProduct_Float()
{
	float f_WavePrefixProduct = WavePrefixProduct(g_f);
	return f_WavePrefixProduct;
}

float1 test_WavePrefixProduct_Float1()
{
	float1 f1_WavePrefixProduct = WavePrefixProduct(g_f1);
	return f1_WavePrefixProduct;
}

float2 test_WavePrefixProduct_Float2()
{
	float2 f2_WavePrefixProduct = WavePrefixProduct(g_f2);
	return f2_WavePrefixProduct;
}

float3 test_WavePrefixProduct_Float3()
{
	float3 f3_WavePrefixProduct = WavePrefixProduct(g_f3);
	return f3_WavePrefixProduct;
}

float4 test_WavePrefixProduct_Float4()
{
	float4 f4_WavePrefixProduct = WavePrefixProduct(g_f4);
	return f4_WavePrefixProduct;
}

float1x1 test_WavePrefixProduct_Float1x1()
{
	float1x1 f1x1_WavePrefixProduct = WavePrefixProduct(g_f1x1);
	return f1x1_WavePrefixProduct;
}

float1x2 test_WavePrefixProduct_Float1x2()
{
	float1x2 f1x2_WavePrefixProduct = WavePrefixProduct(g_f1x2);
	return f1x2_WavePrefixProduct;
}

float1x3 test_WavePrefixProduct_Float1x3()
{
	float1x3 f1x3_WavePrefixProduct = WavePrefixProduct(g_f1x3);
	return f1x3_WavePrefixProduct;
}

float1x4 test_WavePrefixProduct_Float1x4()
{
	float1x4 f1x4_WavePrefixProduct = WavePrefixProduct(g_f1x4);
	return f1x4_WavePrefixProduct;
}

float2x1 test_WavePrefixProduct_Float2x1()
{
	float2x1 f2x1_WavePrefixProduct = WavePrefixProduct(g_f2x1);
	return f2x1_WavePrefixProduct;
}

float2x2 test_WavePrefixProduct_Float2x2()
{
	float2x2 f2x2_WavePrefixProduct = WavePrefixProduct(g_f2x2);
	return f2x2_WavePrefixProduct;
}

float2x3 test_WavePrefixProduct_Float2x3()
{
	float2x3 f2x3_WavePrefixProduct = WavePrefixProduct(g_f2x3);
	return f2x3_WavePrefixProduct;
}

float2x4 test_WavePrefixProduct_Float2x4()
{
	float2x4 f2x4_WavePrefixProduct = WavePrefixProduct(g_f2x4);
	return f2x4_WavePrefixProduct;
}

float3x1 test_WavePrefixProduct_Float3x1()
{
	float3x1 f3x1_WavePrefixProduct = WavePrefixProduct(g_f3x1);
	return f3x1_WavePrefixProduct;
}

float3x2 test_WavePrefixProduct_Float3x2()
{
	float3x2 f3x2_WavePrefixProduct = WavePrefixProduct(g_f3x2);
	return f3x2_WavePrefixProduct;
}

float3x3 test_WavePrefixProduct_Float3x3()
{
	float3x3 f3x3_WavePrefixProduct = WavePrefixProduct(g_f3x3);
	return f3x3_WavePrefixProduct;
}

float3x4 test_WavePrefixProduct_Float3x4()
{
	float3x4 f3x4_WavePrefixProduct = WavePrefixProduct(g_f3x4);
	return f3x4_WavePrefixProduct;
}

float4x1 test_WavePrefixProduct_Float4x1()
{
	float4x1 f4x1_WavePrefixProduct = WavePrefixProduct(g_f4x1);
	return f4x1_WavePrefixProduct;
}

float4x2 test_WavePrefixProduct_Float4x2()
{
	float4x2 f4x2_WavePrefixProduct = WavePrefixProduct(g_f4x2);
	return f4x2_WavePrefixProduct;
}

float4x3 test_WavePrefixProduct_Float4x3()
{
	float4x3 f4x3_WavePrefixProduct = WavePrefixProduct(g_f4x3);
	return f4x3_WavePrefixProduct;
}

float4x4 test_WavePrefixProduct_Float4x4()
{
	float4x4 f4x4_WavePrefixProduct = WavePrefixProduct(g_f4x4);
	return f4x4_WavePrefixProduct;
}

float test_WavePrefixSum_Float()
{
	float f_WavePrefixSum = WavePrefixSum(g_f);
	return f_WavePrefixSum;
}

float1 test_WavePrefixSum_Float1()
{
	float1 f1_WavePrefixSum = WavePrefixSum(g_f1);
	return f1_WavePrefixSum;
}

float2 test_WavePrefixSum_Float2()
{
	float2 f2_WavePrefixSum = WavePrefixSum(g_f2);
	return f2_WavePrefixSum;
}

float3 test_WavePrefixSum_Float3()
{
	float3 f3_WavePrefixSum = WavePrefixSum(g_f3);
	return f3_WavePrefixSum;
}

float4 test_WavePrefixSum_Float4()
{
	float4 f4_WavePrefixSum = WavePrefixSum(g_f4);
	return f4_WavePrefixSum;
}

float1x1 test_WavePrefixSum_Float1x1()
{
	float1x1 f1x1_WavePrefixSum = WavePrefixSum(g_f1x1);
	return f1x1_WavePrefixSum;
}

float1x2 test_WavePrefixSum_Float1x2()
{
	float1x2 f1x2_WavePrefixSum = WavePrefixSum(g_f1x2);
	return f1x2_WavePrefixSum;
}

float1x3 test_WavePrefixSum_Float1x3()
{
	float1x3 f1x3_WavePrefixSum = WavePrefixSum(g_f1x3);
	return f1x3_WavePrefixSum;
}

float1x4 test_WavePrefixSum_Float1x4()
{
	float1x4 f1x4_WavePrefixSum = WavePrefixSum(g_f1x4);
	return f1x4_WavePrefixSum;
}

float2x1 test_WavePrefixSum_Float2x1()
{
	float2x1 f2x1_WavePrefixSum = WavePrefixSum(g_f2x1);
	return f2x1_WavePrefixSum;
}

float2x2 test_WavePrefixSum_Float2x2()
{
	float2x2 f2x2_WavePrefixSum = WavePrefixSum(g_f2x2);
	return f2x2_WavePrefixSum;
}

float2x3 test_WavePrefixSum_Float2x3()
{
	float2x3 f2x3_WavePrefixSum = WavePrefixSum(g_f2x3);
	return f2x3_WavePrefixSum;
}

float2x4 test_WavePrefixSum_Float2x4()
{
	float2x4 f2x4_WavePrefixSum = WavePrefixSum(g_f2x4);
	return f2x4_WavePrefixSum;
}

float3x1 test_WavePrefixSum_Float3x1()
{
	float3x1 f3x1_WavePrefixSum = WavePrefixSum(g_f3x1);
	return f3x1_WavePrefixSum;
}

float3x2 test_WavePrefixSum_Float3x2()
{
	float3x2 f3x2_WavePrefixSum = WavePrefixSum(g_f3x2);
	return f3x2_WavePrefixSum;
}

float3x3 test_WavePrefixSum_Float3x3()
{
	float3x3 f3x3_WavePrefixSum = WavePrefixSum(g_f3x3);
	return f3x3_WavePrefixSum;
}

float3x4 test_WavePrefixSum_Float3x4()
{
	float3x4 f3x4_WavePrefixSum = WavePrefixSum(g_f3x4);
	return f3x4_WavePrefixSum;
}

float4x1 test_WavePrefixSum_Float4x1()
{
	float4x1 f4x1_WavePrefixSum = WavePrefixSum(g_f4x1);
	return f4x1_WavePrefixSum;
}

float4x2 test_WavePrefixSum_Float4x2()
{
	float4x2 f4x2_WavePrefixSum = WavePrefixSum(g_f4x2);
	return f4x2_WavePrefixSum;
}

float4x3 test_WavePrefixSum_Float4x3()
{
	float4x3 f4x3_WavePrefixSum = WavePrefixSum(g_f4x3);
	return f4x3_WavePrefixSum;
}

float4x4 test_WavePrefixSum_Float4x4()
{
	float4x4 f4x4_WavePrefixSum = WavePrefixSum(g_f4x4);
	return f4x4_WavePrefixSum;
}

float test_abs_Float()
{
	float f_abs = abs(g_f);
	return f_abs;
}

float1 test_abs_Float1()
{
	float1 f1_abs = abs(g_f1);
	return f1_abs;
}

float2 test_abs_Float2()
{
	float2 f2_abs = abs(g_f2);
	return f2_abs;
}

float3 test_abs_Float3()
{
	float3 f3_abs = abs(g_f3);
	return f3_abs;
}

float4 test_abs_Float4()
{
	float4 f4_abs = abs(g_f4);
	return f4_abs;
}

float1x1 test_abs_Float1x1()
{
	float1x1 f1x1_abs = abs(g_f1x1);
	return f1x1_abs;
}

float1x2 test_abs_Float1x2()
{
	float1x2 f1x2_abs = abs(g_f1x2);
	return f1x2_abs;
}

float1x3 test_abs_Float1x3()
{
	float1x3 f1x3_abs = abs(g_f1x3);
	return f1x3_abs;
}

float1x4 test_abs_Float1x4()
{
	float1x4 f1x4_abs = abs(g_f1x4);
	return f1x4_abs;
}

float2x1 test_abs_Float2x1()
{
	float2x1 f2x1_abs = abs(g_f2x1);
	return f2x1_abs;
}

float2x2 test_abs_Float2x2()
{
	float2x2 f2x2_abs = abs(g_f2x2);
	return f2x2_abs;
}

float2x3 test_abs_Float2x3()
{
	float2x3 f2x3_abs = abs(g_f2x3);
	return f2x3_abs;
}

float2x4 test_abs_Float2x4()
{
	float2x4 f2x4_abs = abs(g_f2x4);
	return f2x4_abs;
}

float3x1 test_abs_Float3x1()
{
	float3x1 f3x1_abs = abs(g_f3x1);
	return f3x1_abs;
}

float3x2 test_abs_Float3x2()
{
	float3x2 f3x2_abs = abs(g_f3x2);
	return f3x2_abs;
}

float3x3 test_abs_Float3x3()
{
	float3x3 f3x3_abs = abs(g_f3x3);
	return f3x3_abs;
}

float3x4 test_abs_Float3x4()
{
	float3x4 f3x4_abs = abs(g_f3x4);
	return f3x4_abs;
}

float4x1 test_abs_Float4x1()
{
	float4x1 f4x1_abs = abs(g_f4x1);
	return f4x1_abs;
}

float4x2 test_abs_Float4x2()
{
	float4x2 f4x2_abs = abs(g_f4x2);
	return f4x2_abs;
}

float4x3 test_abs_Float4x3()
{
	float4x3 f4x3_abs = abs(g_f4x3);
	return f4x3_abs;
}

float4x4 test_abs_Float4x4()
{
	float4x4 f4x4_abs = abs(g_f4x4);
	return f4x4_abs;
}

