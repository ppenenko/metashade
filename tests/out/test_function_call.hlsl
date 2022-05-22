float4 add(float4 a, float4 b)
{
	return (a + b);
}

struct PsOut
{
	float4 color : SV_TARGET;
};

cbuffer cb : register(b0)
{
	float4 gA;
	float4 gB;
};

PsOut psMain()
{
	PsOut result;
	result.color = add(gA, gB);
	return result;
}

