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
	return EvaluateAttributeCentroid(g_f);
}

float1 test_EvaluateAttributeCentroid_Float1()
{
	return EvaluateAttributeCentroid(g_f1);
}

float2 test_EvaluateAttributeCentroid_Float2()
{
	return EvaluateAttributeCentroid(g_f2);
}

float3 test_EvaluateAttributeCentroid_Float3()
{
	return EvaluateAttributeCentroid(g_f3);
}

float4 test_EvaluateAttributeCentroid_Float4()
{
	return EvaluateAttributeCentroid(g_f4);
}

float1x1 test_EvaluateAttributeCentroid_Float1x1()
{
	return EvaluateAttributeCentroid(g_f1x1);
}

float1x2 test_EvaluateAttributeCentroid_Float1x2()
{
	return EvaluateAttributeCentroid(g_f1x2);
}

float1x3 test_EvaluateAttributeCentroid_Float1x3()
{
	return EvaluateAttributeCentroid(g_f1x3);
}

float1x4 test_EvaluateAttributeCentroid_Float1x4()
{
	return EvaluateAttributeCentroid(g_f1x4);
}

float2x1 test_EvaluateAttributeCentroid_Float2x1()
{
	return EvaluateAttributeCentroid(g_f2x1);
}

float2x2 test_EvaluateAttributeCentroid_Float2x2()
{
	return EvaluateAttributeCentroid(g_f2x2);
}

float2x3 test_EvaluateAttributeCentroid_Float2x3()
{
	return EvaluateAttributeCentroid(g_f2x3);
}

float2x4 test_EvaluateAttributeCentroid_Float2x4()
{
	return EvaluateAttributeCentroid(g_f2x4);
}

float3x1 test_EvaluateAttributeCentroid_Float3x1()
{
	return EvaluateAttributeCentroid(g_f3x1);
}

float3x2 test_EvaluateAttributeCentroid_Float3x2()
{
	return EvaluateAttributeCentroid(g_f3x2);
}

float3x3 test_EvaluateAttributeCentroid_Float3x3()
{
	return EvaluateAttributeCentroid(g_f3x3);
}

float3x4 test_EvaluateAttributeCentroid_Float3x4()
{
	return EvaluateAttributeCentroid(g_f3x4);
}

float4x1 test_EvaluateAttributeCentroid_Float4x1()
{
	return EvaluateAttributeCentroid(g_f4x1);
}

float4x2 test_EvaluateAttributeCentroid_Float4x2()
{
	return EvaluateAttributeCentroid(g_f4x2);
}

float4x3 test_EvaluateAttributeCentroid_Float4x3()
{
	return EvaluateAttributeCentroid(g_f4x3);
}

float4x4 test_EvaluateAttributeCentroid_Float4x4()
{
	return EvaluateAttributeCentroid(g_f4x4);
}

float test_QuadReadAcrossDiagonal_Float()
{
	return QuadReadAcrossDiagonal(g_f);
}

float1 test_QuadReadAcrossDiagonal_Float1()
{
	return QuadReadAcrossDiagonal(g_f1);
}

float2 test_QuadReadAcrossDiagonal_Float2()
{
	return QuadReadAcrossDiagonal(g_f2);
}

float3 test_QuadReadAcrossDiagonal_Float3()
{
	return QuadReadAcrossDiagonal(g_f3);
}

float4 test_QuadReadAcrossDiagonal_Float4()
{
	return QuadReadAcrossDiagonal(g_f4);
}

float1x1 test_QuadReadAcrossDiagonal_Float1x1()
{
	return QuadReadAcrossDiagonal(g_f1x1);
}

float1x2 test_QuadReadAcrossDiagonal_Float1x2()
{
	return QuadReadAcrossDiagonal(g_f1x2);
}

float1x3 test_QuadReadAcrossDiagonal_Float1x3()
{
	return QuadReadAcrossDiagonal(g_f1x3);
}

float1x4 test_QuadReadAcrossDiagonal_Float1x4()
{
	return QuadReadAcrossDiagonal(g_f1x4);
}

float2x1 test_QuadReadAcrossDiagonal_Float2x1()
{
	return QuadReadAcrossDiagonal(g_f2x1);
}

float2x2 test_QuadReadAcrossDiagonal_Float2x2()
{
	return QuadReadAcrossDiagonal(g_f2x2);
}

float2x3 test_QuadReadAcrossDiagonal_Float2x3()
{
	return QuadReadAcrossDiagonal(g_f2x3);
}

float2x4 test_QuadReadAcrossDiagonal_Float2x4()
{
	return QuadReadAcrossDiagonal(g_f2x4);
}

float3x1 test_QuadReadAcrossDiagonal_Float3x1()
{
	return QuadReadAcrossDiagonal(g_f3x1);
}

float3x2 test_QuadReadAcrossDiagonal_Float3x2()
{
	return QuadReadAcrossDiagonal(g_f3x2);
}

float3x3 test_QuadReadAcrossDiagonal_Float3x3()
{
	return QuadReadAcrossDiagonal(g_f3x3);
}

float3x4 test_QuadReadAcrossDiagonal_Float3x4()
{
	return QuadReadAcrossDiagonal(g_f3x4);
}

float4x1 test_QuadReadAcrossDiagonal_Float4x1()
{
	return QuadReadAcrossDiagonal(g_f4x1);
}

float4x2 test_QuadReadAcrossDiagonal_Float4x2()
{
	return QuadReadAcrossDiagonal(g_f4x2);
}

float4x3 test_QuadReadAcrossDiagonal_Float4x3()
{
	return QuadReadAcrossDiagonal(g_f4x3);
}

float4x4 test_QuadReadAcrossDiagonal_Float4x4()
{
	return QuadReadAcrossDiagonal(g_f4x4);
}

float test_QuadReadAcrossX_Float()
{
	return QuadReadAcrossX(g_f);
}

float1 test_QuadReadAcrossX_Float1()
{
	return QuadReadAcrossX(g_f1);
}

float2 test_QuadReadAcrossX_Float2()
{
	return QuadReadAcrossX(g_f2);
}

float3 test_QuadReadAcrossX_Float3()
{
	return QuadReadAcrossX(g_f3);
}

float4 test_QuadReadAcrossX_Float4()
{
	return QuadReadAcrossX(g_f4);
}

float1x1 test_QuadReadAcrossX_Float1x1()
{
	return QuadReadAcrossX(g_f1x1);
}

float1x2 test_QuadReadAcrossX_Float1x2()
{
	return QuadReadAcrossX(g_f1x2);
}

float1x3 test_QuadReadAcrossX_Float1x3()
{
	return QuadReadAcrossX(g_f1x3);
}

float1x4 test_QuadReadAcrossX_Float1x4()
{
	return QuadReadAcrossX(g_f1x4);
}

float2x1 test_QuadReadAcrossX_Float2x1()
{
	return QuadReadAcrossX(g_f2x1);
}

float2x2 test_QuadReadAcrossX_Float2x2()
{
	return QuadReadAcrossX(g_f2x2);
}

float2x3 test_QuadReadAcrossX_Float2x3()
{
	return QuadReadAcrossX(g_f2x3);
}

float2x4 test_QuadReadAcrossX_Float2x4()
{
	return QuadReadAcrossX(g_f2x4);
}

float3x1 test_QuadReadAcrossX_Float3x1()
{
	return QuadReadAcrossX(g_f3x1);
}

float3x2 test_QuadReadAcrossX_Float3x2()
{
	return QuadReadAcrossX(g_f3x2);
}

float3x3 test_QuadReadAcrossX_Float3x3()
{
	return QuadReadAcrossX(g_f3x3);
}

float3x4 test_QuadReadAcrossX_Float3x4()
{
	return QuadReadAcrossX(g_f3x4);
}

float4x1 test_QuadReadAcrossX_Float4x1()
{
	return QuadReadAcrossX(g_f4x1);
}

float4x2 test_QuadReadAcrossX_Float4x2()
{
	return QuadReadAcrossX(g_f4x2);
}

float4x3 test_QuadReadAcrossX_Float4x3()
{
	return QuadReadAcrossX(g_f4x3);
}

float4x4 test_QuadReadAcrossX_Float4x4()
{
	return QuadReadAcrossX(g_f4x4);
}

float test_QuadReadAcrossY_Float()
{
	return QuadReadAcrossY(g_f);
}

float1 test_QuadReadAcrossY_Float1()
{
	return QuadReadAcrossY(g_f1);
}

float2 test_QuadReadAcrossY_Float2()
{
	return QuadReadAcrossY(g_f2);
}

float3 test_QuadReadAcrossY_Float3()
{
	return QuadReadAcrossY(g_f3);
}

float4 test_QuadReadAcrossY_Float4()
{
	return QuadReadAcrossY(g_f4);
}

float1x1 test_QuadReadAcrossY_Float1x1()
{
	return QuadReadAcrossY(g_f1x1);
}

float1x2 test_QuadReadAcrossY_Float1x2()
{
	return QuadReadAcrossY(g_f1x2);
}

float1x3 test_QuadReadAcrossY_Float1x3()
{
	return QuadReadAcrossY(g_f1x3);
}

float1x4 test_QuadReadAcrossY_Float1x4()
{
	return QuadReadAcrossY(g_f1x4);
}

float2x1 test_QuadReadAcrossY_Float2x1()
{
	return QuadReadAcrossY(g_f2x1);
}

float2x2 test_QuadReadAcrossY_Float2x2()
{
	return QuadReadAcrossY(g_f2x2);
}

float2x3 test_QuadReadAcrossY_Float2x3()
{
	return QuadReadAcrossY(g_f2x3);
}

float2x4 test_QuadReadAcrossY_Float2x4()
{
	return QuadReadAcrossY(g_f2x4);
}

float3x1 test_QuadReadAcrossY_Float3x1()
{
	return QuadReadAcrossY(g_f3x1);
}

float3x2 test_QuadReadAcrossY_Float3x2()
{
	return QuadReadAcrossY(g_f3x2);
}

float3x3 test_QuadReadAcrossY_Float3x3()
{
	return QuadReadAcrossY(g_f3x3);
}

float3x4 test_QuadReadAcrossY_Float3x4()
{
	return QuadReadAcrossY(g_f3x4);
}

float4x1 test_QuadReadAcrossY_Float4x1()
{
	return QuadReadAcrossY(g_f4x1);
}

float4x2 test_QuadReadAcrossY_Float4x2()
{
	return QuadReadAcrossY(g_f4x2);
}

float4x3 test_QuadReadAcrossY_Float4x3()
{
	return QuadReadAcrossY(g_f4x3);
}

float4x4 test_QuadReadAcrossY_Float4x4()
{
	return QuadReadAcrossY(g_f4x4);
}

float test_WaveActiveMax_Float()
{
	return WaveActiveMax(g_f);
}

float1 test_WaveActiveMax_Float1()
{
	return WaveActiveMax(g_f1);
}

float2 test_WaveActiveMax_Float2()
{
	return WaveActiveMax(g_f2);
}

float3 test_WaveActiveMax_Float3()
{
	return WaveActiveMax(g_f3);
}

float4 test_WaveActiveMax_Float4()
{
	return WaveActiveMax(g_f4);
}

float1x1 test_WaveActiveMax_Float1x1()
{
	return WaveActiveMax(g_f1x1);
}

float1x2 test_WaveActiveMax_Float1x2()
{
	return WaveActiveMax(g_f1x2);
}

float1x3 test_WaveActiveMax_Float1x3()
{
	return WaveActiveMax(g_f1x3);
}

float1x4 test_WaveActiveMax_Float1x4()
{
	return WaveActiveMax(g_f1x4);
}

float2x1 test_WaveActiveMax_Float2x1()
{
	return WaveActiveMax(g_f2x1);
}

float2x2 test_WaveActiveMax_Float2x2()
{
	return WaveActiveMax(g_f2x2);
}

float2x3 test_WaveActiveMax_Float2x3()
{
	return WaveActiveMax(g_f2x3);
}

float2x4 test_WaveActiveMax_Float2x4()
{
	return WaveActiveMax(g_f2x4);
}

float3x1 test_WaveActiveMax_Float3x1()
{
	return WaveActiveMax(g_f3x1);
}

float3x2 test_WaveActiveMax_Float3x2()
{
	return WaveActiveMax(g_f3x2);
}

float3x3 test_WaveActiveMax_Float3x3()
{
	return WaveActiveMax(g_f3x3);
}

float3x4 test_WaveActiveMax_Float3x4()
{
	return WaveActiveMax(g_f3x4);
}

float4x1 test_WaveActiveMax_Float4x1()
{
	return WaveActiveMax(g_f4x1);
}

float4x2 test_WaveActiveMax_Float4x2()
{
	return WaveActiveMax(g_f4x2);
}

float4x3 test_WaveActiveMax_Float4x3()
{
	return WaveActiveMax(g_f4x3);
}

float4x4 test_WaveActiveMax_Float4x4()
{
	return WaveActiveMax(g_f4x4);
}

float test_WaveActiveMin_Float()
{
	return WaveActiveMin(g_f);
}

float1 test_WaveActiveMin_Float1()
{
	return WaveActiveMin(g_f1);
}

float2 test_WaveActiveMin_Float2()
{
	return WaveActiveMin(g_f2);
}

float3 test_WaveActiveMin_Float3()
{
	return WaveActiveMin(g_f3);
}

float4 test_WaveActiveMin_Float4()
{
	return WaveActiveMin(g_f4);
}

float1x1 test_WaveActiveMin_Float1x1()
{
	return WaveActiveMin(g_f1x1);
}

float1x2 test_WaveActiveMin_Float1x2()
{
	return WaveActiveMin(g_f1x2);
}

float1x3 test_WaveActiveMin_Float1x3()
{
	return WaveActiveMin(g_f1x3);
}

float1x4 test_WaveActiveMin_Float1x4()
{
	return WaveActiveMin(g_f1x4);
}

float2x1 test_WaveActiveMin_Float2x1()
{
	return WaveActiveMin(g_f2x1);
}

float2x2 test_WaveActiveMin_Float2x2()
{
	return WaveActiveMin(g_f2x2);
}

float2x3 test_WaveActiveMin_Float2x3()
{
	return WaveActiveMin(g_f2x3);
}

float2x4 test_WaveActiveMin_Float2x4()
{
	return WaveActiveMin(g_f2x4);
}

float3x1 test_WaveActiveMin_Float3x1()
{
	return WaveActiveMin(g_f3x1);
}

float3x2 test_WaveActiveMin_Float3x2()
{
	return WaveActiveMin(g_f3x2);
}

float3x3 test_WaveActiveMin_Float3x3()
{
	return WaveActiveMin(g_f3x3);
}

float3x4 test_WaveActiveMin_Float3x4()
{
	return WaveActiveMin(g_f3x4);
}

float4x1 test_WaveActiveMin_Float4x1()
{
	return WaveActiveMin(g_f4x1);
}

float4x2 test_WaveActiveMin_Float4x2()
{
	return WaveActiveMin(g_f4x2);
}

float4x3 test_WaveActiveMin_Float4x3()
{
	return WaveActiveMin(g_f4x3);
}

float4x4 test_WaveActiveMin_Float4x4()
{
	return WaveActiveMin(g_f4x4);
}

float test_WaveActiveProduct_Float()
{
	return WaveActiveProduct(g_f);
}

float1 test_WaveActiveProduct_Float1()
{
	return WaveActiveProduct(g_f1);
}

float2 test_WaveActiveProduct_Float2()
{
	return WaveActiveProduct(g_f2);
}

float3 test_WaveActiveProduct_Float3()
{
	return WaveActiveProduct(g_f3);
}

float4 test_WaveActiveProduct_Float4()
{
	return WaveActiveProduct(g_f4);
}

float1x1 test_WaveActiveProduct_Float1x1()
{
	return WaveActiveProduct(g_f1x1);
}

float1x2 test_WaveActiveProduct_Float1x2()
{
	return WaveActiveProduct(g_f1x2);
}

float1x3 test_WaveActiveProduct_Float1x3()
{
	return WaveActiveProduct(g_f1x3);
}

float1x4 test_WaveActiveProduct_Float1x4()
{
	return WaveActiveProduct(g_f1x4);
}

float2x1 test_WaveActiveProduct_Float2x1()
{
	return WaveActiveProduct(g_f2x1);
}

float2x2 test_WaveActiveProduct_Float2x2()
{
	return WaveActiveProduct(g_f2x2);
}

float2x3 test_WaveActiveProduct_Float2x3()
{
	return WaveActiveProduct(g_f2x3);
}

float2x4 test_WaveActiveProduct_Float2x4()
{
	return WaveActiveProduct(g_f2x4);
}

float3x1 test_WaveActiveProduct_Float3x1()
{
	return WaveActiveProduct(g_f3x1);
}

float3x2 test_WaveActiveProduct_Float3x2()
{
	return WaveActiveProduct(g_f3x2);
}

float3x3 test_WaveActiveProduct_Float3x3()
{
	return WaveActiveProduct(g_f3x3);
}

float3x4 test_WaveActiveProduct_Float3x4()
{
	return WaveActiveProduct(g_f3x4);
}

float4x1 test_WaveActiveProduct_Float4x1()
{
	return WaveActiveProduct(g_f4x1);
}

float4x2 test_WaveActiveProduct_Float4x2()
{
	return WaveActiveProduct(g_f4x2);
}

float4x3 test_WaveActiveProduct_Float4x3()
{
	return WaveActiveProduct(g_f4x3);
}

float4x4 test_WaveActiveProduct_Float4x4()
{
	return WaveActiveProduct(g_f4x4);
}

float test_WaveActiveSum_Float()
{
	return WaveActiveSum(g_f);
}

float1 test_WaveActiveSum_Float1()
{
	return WaveActiveSum(g_f1);
}

float2 test_WaveActiveSum_Float2()
{
	return WaveActiveSum(g_f2);
}

float3 test_WaveActiveSum_Float3()
{
	return WaveActiveSum(g_f3);
}

float4 test_WaveActiveSum_Float4()
{
	return WaveActiveSum(g_f4);
}

float1x1 test_WaveActiveSum_Float1x1()
{
	return WaveActiveSum(g_f1x1);
}

float1x2 test_WaveActiveSum_Float1x2()
{
	return WaveActiveSum(g_f1x2);
}

float1x3 test_WaveActiveSum_Float1x3()
{
	return WaveActiveSum(g_f1x3);
}

float1x4 test_WaveActiveSum_Float1x4()
{
	return WaveActiveSum(g_f1x4);
}

float2x1 test_WaveActiveSum_Float2x1()
{
	return WaveActiveSum(g_f2x1);
}

float2x2 test_WaveActiveSum_Float2x2()
{
	return WaveActiveSum(g_f2x2);
}

float2x3 test_WaveActiveSum_Float2x3()
{
	return WaveActiveSum(g_f2x3);
}

float2x4 test_WaveActiveSum_Float2x4()
{
	return WaveActiveSum(g_f2x4);
}

float3x1 test_WaveActiveSum_Float3x1()
{
	return WaveActiveSum(g_f3x1);
}

float3x2 test_WaveActiveSum_Float3x2()
{
	return WaveActiveSum(g_f3x2);
}

float3x3 test_WaveActiveSum_Float3x3()
{
	return WaveActiveSum(g_f3x3);
}

float3x4 test_WaveActiveSum_Float3x4()
{
	return WaveActiveSum(g_f3x4);
}

float4x1 test_WaveActiveSum_Float4x1()
{
	return WaveActiveSum(g_f4x1);
}

float4x2 test_WaveActiveSum_Float4x2()
{
	return WaveActiveSum(g_f4x2);
}

float4x3 test_WaveActiveSum_Float4x3()
{
	return WaveActiveSum(g_f4x3);
}

float4x4 test_WaveActiveSum_Float4x4()
{
	return WaveActiveSum(g_f4x4);
}

float test_WavePrefixProduct_Float()
{
	return WavePrefixProduct(g_f);
}

float1 test_WavePrefixProduct_Float1()
{
	return WavePrefixProduct(g_f1);
}

float2 test_WavePrefixProduct_Float2()
{
	return WavePrefixProduct(g_f2);
}

float3 test_WavePrefixProduct_Float3()
{
	return WavePrefixProduct(g_f3);
}

float4 test_WavePrefixProduct_Float4()
{
	return WavePrefixProduct(g_f4);
}

float1x1 test_WavePrefixProduct_Float1x1()
{
	return WavePrefixProduct(g_f1x1);
}

float1x2 test_WavePrefixProduct_Float1x2()
{
	return WavePrefixProduct(g_f1x2);
}

float1x3 test_WavePrefixProduct_Float1x3()
{
	return WavePrefixProduct(g_f1x3);
}

float1x4 test_WavePrefixProduct_Float1x4()
{
	return WavePrefixProduct(g_f1x4);
}

float2x1 test_WavePrefixProduct_Float2x1()
{
	return WavePrefixProduct(g_f2x1);
}

float2x2 test_WavePrefixProduct_Float2x2()
{
	return WavePrefixProduct(g_f2x2);
}

float2x3 test_WavePrefixProduct_Float2x3()
{
	return WavePrefixProduct(g_f2x3);
}

float2x4 test_WavePrefixProduct_Float2x4()
{
	return WavePrefixProduct(g_f2x4);
}

float3x1 test_WavePrefixProduct_Float3x1()
{
	return WavePrefixProduct(g_f3x1);
}

float3x2 test_WavePrefixProduct_Float3x2()
{
	return WavePrefixProduct(g_f3x2);
}

float3x3 test_WavePrefixProduct_Float3x3()
{
	return WavePrefixProduct(g_f3x3);
}

float3x4 test_WavePrefixProduct_Float3x4()
{
	return WavePrefixProduct(g_f3x4);
}

float4x1 test_WavePrefixProduct_Float4x1()
{
	return WavePrefixProduct(g_f4x1);
}

float4x2 test_WavePrefixProduct_Float4x2()
{
	return WavePrefixProduct(g_f4x2);
}

float4x3 test_WavePrefixProduct_Float4x3()
{
	return WavePrefixProduct(g_f4x3);
}

float4x4 test_WavePrefixProduct_Float4x4()
{
	return WavePrefixProduct(g_f4x4);
}

float test_WavePrefixSum_Float()
{
	return WavePrefixSum(g_f);
}

float1 test_WavePrefixSum_Float1()
{
	return WavePrefixSum(g_f1);
}

float2 test_WavePrefixSum_Float2()
{
	return WavePrefixSum(g_f2);
}

float3 test_WavePrefixSum_Float3()
{
	return WavePrefixSum(g_f3);
}

float4 test_WavePrefixSum_Float4()
{
	return WavePrefixSum(g_f4);
}

float1x1 test_WavePrefixSum_Float1x1()
{
	return WavePrefixSum(g_f1x1);
}

float1x2 test_WavePrefixSum_Float1x2()
{
	return WavePrefixSum(g_f1x2);
}

float1x3 test_WavePrefixSum_Float1x3()
{
	return WavePrefixSum(g_f1x3);
}

float1x4 test_WavePrefixSum_Float1x4()
{
	return WavePrefixSum(g_f1x4);
}

float2x1 test_WavePrefixSum_Float2x1()
{
	return WavePrefixSum(g_f2x1);
}

float2x2 test_WavePrefixSum_Float2x2()
{
	return WavePrefixSum(g_f2x2);
}

float2x3 test_WavePrefixSum_Float2x3()
{
	return WavePrefixSum(g_f2x3);
}

float2x4 test_WavePrefixSum_Float2x4()
{
	return WavePrefixSum(g_f2x4);
}

float3x1 test_WavePrefixSum_Float3x1()
{
	return WavePrefixSum(g_f3x1);
}

float3x2 test_WavePrefixSum_Float3x2()
{
	return WavePrefixSum(g_f3x2);
}

float3x3 test_WavePrefixSum_Float3x3()
{
	return WavePrefixSum(g_f3x3);
}

float3x4 test_WavePrefixSum_Float3x4()
{
	return WavePrefixSum(g_f3x4);
}

float4x1 test_WavePrefixSum_Float4x1()
{
	return WavePrefixSum(g_f4x1);
}

float4x2 test_WavePrefixSum_Float4x2()
{
	return WavePrefixSum(g_f4x2);
}

float4x3 test_WavePrefixSum_Float4x3()
{
	return WavePrefixSum(g_f4x3);
}

float4x4 test_WavePrefixSum_Float4x4()
{
	return WavePrefixSum(g_f4x4);
}

float test_abs_Float()
{
	return abs(g_f);
}

float1 test_abs_Float1()
{
	return abs(g_f1);
}

float2 test_abs_Float2()
{
	return abs(g_f2);
}

float3 test_abs_Float3()
{
	return abs(g_f3);
}

float4 test_abs_Float4()
{
	return abs(g_f4);
}

float1x1 test_abs_Float1x1()
{
	return abs(g_f1x1);
}

float1x2 test_abs_Float1x2()
{
	return abs(g_f1x2);
}

float1x3 test_abs_Float1x3()
{
	return abs(g_f1x3);
}

float1x4 test_abs_Float1x4()
{
	return abs(g_f1x4);
}

float2x1 test_abs_Float2x1()
{
	return abs(g_f2x1);
}

float2x2 test_abs_Float2x2()
{
	return abs(g_f2x2);
}

float2x3 test_abs_Float2x3()
{
	return abs(g_f2x3);
}

float2x4 test_abs_Float2x4()
{
	return abs(g_f2x4);
}

float3x1 test_abs_Float3x1()
{
	return abs(g_f3x1);
}

float3x2 test_abs_Float3x2()
{
	return abs(g_f3x2);
}

float3x3 test_abs_Float3x3()
{
	return abs(g_f3x3);
}

float3x4 test_abs_Float3x4()
{
	return abs(g_f3x4);
}

float4x1 test_abs_Float4x1()
{
	return abs(g_f4x1);
}

float4x2 test_abs_Float4x2()
{
	return abs(g_f4x2);
}

float4x3 test_abs_Float4x3()
{
	return abs(g_f4x3);
}

float4x4 test_abs_Float4x4()
{
	return abs(g_f4x4);
}

float test_clamp_Float(float min, float max)
{
	return clamp(g_f, min, max);
}

float1 test_clamp_Float1(float1 min, float1 max)
{
	return clamp(g_f1, min, max);
}

float2 test_clamp_Float2(float2 min, float2 max)
{
	return clamp(g_f2, min, max);
}

float3 test_clamp_Float3(float3 min, float3 max)
{
	return clamp(g_f3, min, max);
}

float4 test_clamp_Float4(float4 min, float4 max)
{
	return clamp(g_f4, min, max);
}

float1x1 test_clamp_Float1x1(float1x1 min, float1x1 max)
{
	return clamp(g_f1x1, min, max);
}

float1x2 test_clamp_Float1x2(float1x2 min, float1x2 max)
{
	return clamp(g_f1x2, min, max);
}

float1x3 test_clamp_Float1x3(float1x3 min, float1x3 max)
{
	return clamp(g_f1x3, min, max);
}

float1x4 test_clamp_Float1x4(float1x4 min, float1x4 max)
{
	return clamp(g_f1x4, min, max);
}

float2x1 test_clamp_Float2x1(float2x1 min, float2x1 max)
{
	return clamp(g_f2x1, min, max);
}

float2x2 test_clamp_Float2x2(float2x2 min, float2x2 max)
{
	return clamp(g_f2x2, min, max);
}

float2x3 test_clamp_Float2x3(float2x3 min, float2x3 max)
{
	return clamp(g_f2x3, min, max);
}

float2x4 test_clamp_Float2x4(float2x4 min, float2x4 max)
{
	return clamp(g_f2x4, min, max);
}

float3x1 test_clamp_Float3x1(float3x1 min, float3x1 max)
{
	return clamp(g_f3x1, min, max);
}

float3x2 test_clamp_Float3x2(float3x2 min, float3x2 max)
{
	return clamp(g_f3x2, min, max);
}

float3x3 test_clamp_Float3x3(float3x3 min, float3x3 max)
{
	return clamp(g_f3x3, min, max);
}

float3x4 test_clamp_Float3x4(float3x4 min, float3x4 max)
{
	return clamp(g_f3x4, min, max);
}

float4x1 test_clamp_Float4x1(float4x1 min, float4x1 max)
{
	return clamp(g_f4x1, min, max);
}

float4x2 test_clamp_Float4x2(float4x2 min, float4x2 max)
{
	return clamp(g_f4x2, min, max);
}

float4x3 test_clamp_Float4x3(float4x3 min, float4x3 max)
{
	return clamp(g_f4x3, min, max);
}

float4x4 test_clamp_Float4x4(float4x4 min, float4x4 max)
{
	return clamp(g_f4x4, min, max);
}

float test_mad_Float(float b, float c)
{
	return mad(g_f, b, c);
}

float1 test_mad_Float1(float1 b, float1 c)
{
	return mad(g_f1, b, c);
}

float2 test_mad_Float2(float2 b, float2 c)
{
	return mad(g_f2, b, c);
}

float3 test_mad_Float3(float3 b, float3 c)
{
	return mad(g_f3, b, c);
}

float4 test_mad_Float4(float4 b, float4 c)
{
	return mad(g_f4, b, c);
}

float1x1 test_mad_Float1x1(float1x1 b, float1x1 c)
{
	return mad(g_f1x1, b, c);
}

float1x2 test_mad_Float1x2(float1x2 b, float1x2 c)
{
	return mad(g_f1x2, b, c);
}

float1x3 test_mad_Float1x3(float1x3 b, float1x3 c)
{
	return mad(g_f1x3, b, c);
}

float1x4 test_mad_Float1x4(float1x4 b, float1x4 c)
{
	return mad(g_f1x4, b, c);
}

float2x1 test_mad_Float2x1(float2x1 b, float2x1 c)
{
	return mad(g_f2x1, b, c);
}

float2x2 test_mad_Float2x2(float2x2 b, float2x2 c)
{
	return mad(g_f2x2, b, c);
}

float2x3 test_mad_Float2x3(float2x3 b, float2x3 c)
{
	return mad(g_f2x3, b, c);
}

float2x4 test_mad_Float2x4(float2x4 b, float2x4 c)
{
	return mad(g_f2x4, b, c);
}

float3x1 test_mad_Float3x1(float3x1 b, float3x1 c)
{
	return mad(g_f3x1, b, c);
}

float3x2 test_mad_Float3x2(float3x2 b, float3x2 c)
{
	return mad(g_f3x2, b, c);
}

float3x3 test_mad_Float3x3(float3x3 b, float3x3 c)
{
	return mad(g_f3x3, b, c);
}

float3x4 test_mad_Float3x4(float3x4 b, float3x4 c)
{
	return mad(g_f3x4, b, c);
}

float4x1 test_mad_Float4x1(float4x1 b, float4x1 c)
{
	return mad(g_f4x1, b, c);
}

float4x2 test_mad_Float4x2(float4x2 b, float4x2 c)
{
	return mad(g_f4x2, b, c);
}

float4x3 test_mad_Float4x3(float4x3 b, float4x3 c)
{
	return mad(g_f4x3, b, c);
}

float4x4 test_mad_Float4x4(float4x4 b, float4x4 c)
{
	return mad(g_f4x4, b, c);
}

float test_max_Float(float b)
{
	return max(g_f, b);
}

float1 test_max_Float1(float1 b)
{
	return max(g_f1, b);
}

float2 test_max_Float2(float2 b)
{
	return max(g_f2, b);
}

float3 test_max_Float3(float3 b)
{
	return max(g_f3, b);
}

float4 test_max_Float4(float4 b)
{
	return max(g_f4, b);
}

float1x1 test_max_Float1x1(float1x1 b)
{
	return max(g_f1x1, b);
}

float1x2 test_max_Float1x2(float1x2 b)
{
	return max(g_f1x2, b);
}

float1x3 test_max_Float1x3(float1x3 b)
{
	return max(g_f1x3, b);
}

float1x4 test_max_Float1x4(float1x4 b)
{
	return max(g_f1x4, b);
}

float2x1 test_max_Float2x1(float2x1 b)
{
	return max(g_f2x1, b);
}

float2x2 test_max_Float2x2(float2x2 b)
{
	return max(g_f2x2, b);
}

float2x3 test_max_Float2x3(float2x3 b)
{
	return max(g_f2x3, b);
}

float2x4 test_max_Float2x4(float2x4 b)
{
	return max(g_f2x4, b);
}

float3x1 test_max_Float3x1(float3x1 b)
{
	return max(g_f3x1, b);
}

float3x2 test_max_Float3x2(float3x2 b)
{
	return max(g_f3x2, b);
}

float3x3 test_max_Float3x3(float3x3 b)
{
	return max(g_f3x3, b);
}

float3x4 test_max_Float3x4(float3x4 b)
{
	return max(g_f3x4, b);
}

float4x1 test_max_Float4x1(float4x1 b)
{
	return max(g_f4x1, b);
}

float4x2 test_max_Float4x2(float4x2 b)
{
	return max(g_f4x2, b);
}

float4x3 test_max_Float4x3(float4x3 b)
{
	return max(g_f4x3, b);
}

float4x4 test_max_Float4x4(float4x4 b)
{
	return max(g_f4x4, b);
}

float test_min_Float(float b)
{
	return min(g_f, b);
}

float1 test_min_Float1(float1 b)
{
	return min(g_f1, b);
}

float2 test_min_Float2(float2 b)
{
	return min(g_f2, b);
}

float3 test_min_Float3(float3 b)
{
	return min(g_f3, b);
}

float4 test_min_Float4(float4 b)
{
	return min(g_f4, b);
}

float1x1 test_min_Float1x1(float1x1 b)
{
	return min(g_f1x1, b);
}

float1x2 test_min_Float1x2(float1x2 b)
{
	return min(g_f1x2, b);
}

float1x3 test_min_Float1x3(float1x3 b)
{
	return min(g_f1x3, b);
}

float1x4 test_min_Float1x4(float1x4 b)
{
	return min(g_f1x4, b);
}

float2x1 test_min_Float2x1(float2x1 b)
{
	return min(g_f2x1, b);
}

float2x2 test_min_Float2x2(float2x2 b)
{
	return min(g_f2x2, b);
}

float2x3 test_min_Float2x3(float2x3 b)
{
	return min(g_f2x3, b);
}

float2x4 test_min_Float2x4(float2x4 b)
{
	return min(g_f2x4, b);
}

float3x1 test_min_Float3x1(float3x1 b)
{
	return min(g_f3x1, b);
}

float3x2 test_min_Float3x2(float3x2 b)
{
	return min(g_f3x2, b);
}

float3x3 test_min_Float3x3(float3x3 b)
{
	return min(g_f3x3, b);
}

float3x4 test_min_Float3x4(float3x4 b)
{
	return min(g_f3x4, b);
}

float4x1 test_min_Float4x1(float4x1 b)
{
	return min(g_f4x1, b);
}

float4x2 test_min_Float4x2(float4x2 b)
{
	return min(g_f4x2, b);
}

float4x3 test_min_Float4x3(float4x3 b)
{
	return min(g_f4x3, b);
}

float4x4 test_min_Float4x4(float4x4 b)
{
	return min(g_f4x4, b);
}

