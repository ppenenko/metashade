cbuffer cb : register(b0)
{
	float g_f;
	float1 g_f1;
	float2 g_f2;
	float3 g_f3;
	float4 g_f4;
};

float test_acos_Float()
{
	float f_acos = acos(g_f);
	return f_acos;
}

float1 test_acos_Float1()
{
	float1 f1_acos = acos(g_f1);
	return f1_acos;
}

float2 test_acos_Float2()
{
	float2 f2_acos = acos(g_f2);
	return f2_acos;
}

float3 test_acos_Float3()
{
	float3 f3_acos = acos(g_f3);
	return f3_acos;
}

float4 test_acos_Float4()
{
	float4 f4_acos = acos(g_f4);
	return f4_acos;
}

float test_asin_Float()
{
	float f_asin = asin(g_f);
	return f_asin;
}

float1 test_asin_Float1()
{
	float1 f1_asin = asin(g_f1);
	return f1_asin;
}

float2 test_asin_Float2()
{
	float2 f2_asin = asin(g_f2);
	return f2_asin;
}

float3 test_asin_Float3()
{
	float3 f3_asin = asin(g_f3);
	return f3_asin;
}

float4 test_asin_Float4()
{
	float4 f4_asin = asin(g_f4);
	return f4_asin;
}

float test_atan_Float()
{
	float f_atan = atan(g_f);
	return f_atan;
}

float1 test_atan_Float1()
{
	float1 f1_atan = atan(g_f1);
	return f1_atan;
}

float2 test_atan_Float2()
{
	float2 f2_atan = atan(g_f2);
	return f2_atan;
}

float3 test_atan_Float3()
{
	float3 f3_atan = atan(g_f3);
	return f3_atan;
}

float4 test_atan_Float4()
{
	float4 f4_atan = atan(g_f4);
	return f4_atan;
}

float test_ceil_Float()
{
	float f_ceil = ceil(g_f);
	return f_ceil;
}

float1 test_ceil_Float1()
{
	float1 f1_ceil = ceil(g_f1);
	return f1_ceil;
}

float2 test_ceil_Float2()
{
	float2 f2_ceil = ceil(g_f2);
	return f2_ceil;
}

float3 test_ceil_Float3()
{
	float3 f3_ceil = ceil(g_f3);
	return f3_ceil;
}

float4 test_ceil_Float4()
{
	float4 f4_ceil = ceil(g_f4);
	return f4_ceil;
}

float test_cos_Float()
{
	float f_cos = cos(g_f);
	return f_cos;
}

float1 test_cos_Float1()
{
	float1 f1_cos = cos(g_f1);
	return f1_cos;
}

float2 test_cos_Float2()
{
	float2 f2_cos = cos(g_f2);
	return f2_cos;
}

float3 test_cos_Float3()
{
	float3 f3_cos = cos(g_f3);
	return f3_cos;
}

float4 test_cos_Float4()
{
	float4 f4_cos = cos(g_f4);
	return f4_cos;
}

float test_cosh_Float()
{
	float f_cosh = cosh(g_f);
	return f_cosh;
}

float1 test_cosh_Float1()
{
	float1 f1_cosh = cosh(g_f1);
	return f1_cosh;
}

float2 test_cosh_Float2()
{
	float2 f2_cosh = cosh(g_f2);
	return f2_cosh;
}

float3 test_cosh_Float3()
{
	float3 f3_cosh = cosh(g_f3);
	return f3_cosh;
}

float4 test_cosh_Float4()
{
	float4 f4_cosh = cosh(g_f4);
	return f4_cosh;
}

float test_ddx_Float()
{
	float f_ddx = ddx(g_f);
	return f_ddx;
}

float1 test_ddx_Float1()
{
	float1 f1_ddx = ddx(g_f1);
	return f1_ddx;
}

float2 test_ddx_Float2()
{
	float2 f2_ddx = ddx(g_f2);
	return f2_ddx;
}

float3 test_ddx_Float3()
{
	float3 f3_ddx = ddx(g_f3);
	return f3_ddx;
}

float4 test_ddx_Float4()
{
	float4 f4_ddx = ddx(g_f4);
	return f4_ddx;
}

float test_ddx_coarse_Float()
{
	float f_ddx_coarse = ddx_coarse(g_f);
	return f_ddx_coarse;
}

float1 test_ddx_coarse_Float1()
{
	float1 f1_ddx_coarse = ddx_coarse(g_f1);
	return f1_ddx_coarse;
}

float2 test_ddx_coarse_Float2()
{
	float2 f2_ddx_coarse = ddx_coarse(g_f2);
	return f2_ddx_coarse;
}

float3 test_ddx_coarse_Float3()
{
	float3 f3_ddx_coarse = ddx_coarse(g_f3);
	return f3_ddx_coarse;
}

float4 test_ddx_coarse_Float4()
{
	float4 f4_ddx_coarse = ddx_coarse(g_f4);
	return f4_ddx_coarse;
}

float test_ddx_fine_Float()
{
	float f_ddx_fine = ddx_fine(g_f);
	return f_ddx_fine;
}

float1 test_ddx_fine_Float1()
{
	float1 f1_ddx_fine = ddx_fine(g_f1);
	return f1_ddx_fine;
}

float2 test_ddx_fine_Float2()
{
	float2 f2_ddx_fine = ddx_fine(g_f2);
	return f2_ddx_fine;
}

float3 test_ddx_fine_Float3()
{
	float3 f3_ddx_fine = ddx_fine(g_f3);
	return f3_ddx_fine;
}

float4 test_ddx_fine_Float4()
{
	float4 f4_ddx_fine = ddx_fine(g_f4);
	return f4_ddx_fine;
}

float test_ddy_Float()
{
	float f_ddy = ddy(g_f);
	return f_ddy;
}

float1 test_ddy_Float1()
{
	float1 f1_ddy = ddy(g_f1);
	return f1_ddy;
}

float2 test_ddy_Float2()
{
	float2 f2_ddy = ddy(g_f2);
	return f2_ddy;
}

float3 test_ddy_Float3()
{
	float3 f3_ddy = ddy(g_f3);
	return f3_ddy;
}

float4 test_ddy_Float4()
{
	float4 f4_ddy = ddy(g_f4);
	return f4_ddy;
}

float test_ddy_coarse_Float()
{
	float f_ddy_coarse = ddy_coarse(g_f);
	return f_ddy_coarse;
}

float1 test_ddy_coarse_Float1()
{
	float1 f1_ddy_coarse = ddy_coarse(g_f1);
	return f1_ddy_coarse;
}

float2 test_ddy_coarse_Float2()
{
	float2 f2_ddy_coarse = ddy_coarse(g_f2);
	return f2_ddy_coarse;
}

float3 test_ddy_coarse_Float3()
{
	float3 f3_ddy_coarse = ddy_coarse(g_f3);
	return f3_ddy_coarse;
}

float4 test_ddy_coarse_Float4()
{
	float4 f4_ddy_coarse = ddy_coarse(g_f4);
	return f4_ddy_coarse;
}

float test_ddy_fine_Float()
{
	float f_ddy_fine = ddy_fine(g_f);
	return f_ddy_fine;
}

float1 test_ddy_fine_Float1()
{
	float1 f1_ddy_fine = ddy_fine(g_f1);
	return f1_ddy_fine;
}

float2 test_ddy_fine_Float2()
{
	float2 f2_ddy_fine = ddy_fine(g_f2);
	return f2_ddy_fine;
}

float3 test_ddy_fine_Float3()
{
	float3 f3_ddy_fine = ddy_fine(g_f3);
	return f3_ddy_fine;
}

float4 test_ddy_fine_Float4()
{
	float4 f4_ddy_fine = ddy_fine(g_f4);
	return f4_ddy_fine;
}

float test_degrees_Float()
{
	float f_degrees = degrees(g_f);
	return f_degrees;
}

float1 test_degrees_Float1()
{
	float1 f1_degrees = degrees(g_f1);
	return f1_degrees;
}

float2 test_degrees_Float2()
{
	float2 f2_degrees = degrees(g_f2);
	return f2_degrees;
}

float3 test_degrees_Float3()
{
	float3 f3_degrees = degrees(g_f3);
	return f3_degrees;
}

float4 test_degrees_Float4()
{
	float4 f4_degrees = degrees(g_f4);
	return f4_degrees;
}

float test_exp_Float()
{
	float f_exp = exp(g_f);
	return f_exp;
}

float1 test_exp_Float1()
{
	float1 f1_exp = exp(g_f1);
	return f1_exp;
}

float2 test_exp_Float2()
{
	float2 f2_exp = exp(g_f2);
	return f2_exp;
}

float3 test_exp_Float3()
{
	float3 f3_exp = exp(g_f3);
	return f3_exp;
}

float4 test_exp_Float4()
{
	float4 f4_exp = exp(g_f4);
	return f4_exp;
}

float test_exp2_Float()
{
	float f_exp2 = exp2(g_f);
	return f_exp2;
}

float1 test_exp2_Float1()
{
	float1 f1_exp2 = exp2(g_f1);
	return f1_exp2;
}

float2 test_exp2_Float2()
{
	float2 f2_exp2 = exp2(g_f2);
	return f2_exp2;
}

float3 test_exp2_Float3()
{
	float3 f3_exp2 = exp2(g_f3);
	return f3_exp2;
}

float4 test_exp2_Float4()
{
	float4 f4_exp2 = exp2(g_f4);
	return f4_exp2;
}

float test_floor_Float()
{
	float f_floor = floor(g_f);
	return f_floor;
}

float1 test_floor_Float1()
{
	float1 f1_floor = floor(g_f1);
	return f1_floor;
}

float2 test_floor_Float2()
{
	float2 f2_floor = floor(g_f2);
	return f2_floor;
}

float3 test_floor_Float3()
{
	float3 f3_floor = floor(g_f3);
	return f3_floor;
}

float4 test_floor_Float4()
{
	float4 f4_floor = floor(g_f4);
	return f4_floor;
}

float test_frac_Float()
{
	float f_frac = frac(g_f);
	return f_frac;
}

float1 test_frac_Float1()
{
	float1 f1_frac = frac(g_f1);
	return f1_frac;
}

float2 test_frac_Float2()
{
	float2 f2_frac = frac(g_f2);
	return f2_frac;
}

float3 test_frac_Float3()
{
	float3 f3_frac = frac(g_f3);
	return f3_frac;
}

float4 test_frac_Float4()
{
	float4 f4_frac = frac(g_f4);
	return f4_frac;
}

float test_fwidth_Float()
{
	float f_fwidth = fwidth(g_f);
	return f_fwidth;
}

float1 test_fwidth_Float1()
{
	float1 f1_fwidth = fwidth(g_f1);
	return f1_fwidth;
}

float2 test_fwidth_Float2()
{
	float2 f2_fwidth = fwidth(g_f2);
	return f2_fwidth;
}

float3 test_fwidth_Float3()
{
	float3 f3_fwidth = fwidth(g_f3);
	return f3_fwidth;
}

float4 test_fwidth_Float4()
{
	float4 f4_fwidth = fwidth(g_f4);
	return f4_fwidth;
}

float test_log_Float()
{
	float f_log = log(g_f);
	return f_log;
}

float1 test_log_Float1()
{
	float1 f1_log = log(g_f1);
	return f1_log;
}

float2 test_log_Float2()
{
	float2 f2_log = log(g_f2);
	return f2_log;
}

float3 test_log_Float3()
{
	float3 f3_log = log(g_f3);
	return f3_log;
}

float4 test_log_Float4()
{
	float4 f4_log = log(g_f4);
	return f4_log;
}

float test_log10_Float()
{
	float f_log10 = log10(g_f);
	return f_log10;
}

float1 test_log10_Float1()
{
	float1 f1_log10 = log10(g_f1);
	return f1_log10;
}

float2 test_log10_Float2()
{
	float2 f2_log10 = log10(g_f2);
	return f2_log10;
}

float3 test_log10_Float3()
{
	float3 f3_log10 = log10(g_f3);
	return f3_log10;
}

float4 test_log10_Float4()
{
	float4 f4_log10 = log10(g_f4);
	return f4_log10;
}

float test_log2_Float()
{
	float f_log2 = log2(g_f);
	return f_log2;
}

float1 test_log2_Float1()
{
	float1 f1_log2 = log2(g_f1);
	return f1_log2;
}

float2 test_log2_Float2()
{
	float2 f2_log2 = log2(g_f2);
	return f2_log2;
}

float3 test_log2_Float3()
{
	float3 f3_log2 = log2(g_f3);
	return f3_log2;
}

float4 test_log2_Float4()
{
	float4 f4_log2 = log2(g_f4);
	return f4_log2;
}

float test_radians_Float()
{
	float f_radians = radians(g_f);
	return f_radians;
}

float1 test_radians_Float1()
{
	float1 f1_radians = radians(g_f1);
	return f1_radians;
}

float2 test_radians_Float2()
{
	float2 f2_radians = radians(g_f2);
	return f2_radians;
}

float3 test_radians_Float3()
{
	float3 f3_radians = radians(g_f3);
	return f3_radians;
}

float4 test_radians_Float4()
{
	float4 f4_radians = radians(g_f4);
	return f4_radians;
}

float test_rcp_Float()
{
	float f_rcp = rcp(g_f);
	return f_rcp;
}

float1 test_rcp_Float1()
{
	float1 f1_rcp = rcp(g_f1);
	return f1_rcp;
}

float2 test_rcp_Float2()
{
	float2 f2_rcp = rcp(g_f2);
	return f2_rcp;
}

float3 test_rcp_Float3()
{
	float3 f3_rcp = rcp(g_f3);
	return f3_rcp;
}

float4 test_rcp_Float4()
{
	float4 f4_rcp = rcp(g_f4);
	return f4_rcp;
}

float test_round_Float()
{
	float f_round = round(g_f);
	return f_round;
}

float1 test_round_Float1()
{
	float1 f1_round = round(g_f1);
	return f1_round;
}

float2 test_round_Float2()
{
	float2 f2_round = round(g_f2);
	return f2_round;
}

float3 test_round_Float3()
{
	float3 f3_round = round(g_f3);
	return f3_round;
}

float4 test_round_Float4()
{
	float4 f4_round = round(g_f4);
	return f4_round;
}

float test_rsqrt_Float()
{
	float f_rsqrt = rsqrt(g_f);
	return f_rsqrt;
}

float1 test_rsqrt_Float1()
{
	float1 f1_rsqrt = rsqrt(g_f1);
	return f1_rsqrt;
}

float2 test_rsqrt_Float2()
{
	float2 f2_rsqrt = rsqrt(g_f2);
	return f2_rsqrt;
}

float3 test_rsqrt_Float3()
{
	float3 f3_rsqrt = rsqrt(g_f3);
	return f3_rsqrt;
}

float4 test_rsqrt_Float4()
{
	float4 f4_rsqrt = rsqrt(g_f4);
	return f4_rsqrt;
}

float test_saturate_Float()
{
	float f_saturate = saturate(g_f);
	return f_saturate;
}

float1 test_saturate_Float1()
{
	float1 f1_saturate = saturate(g_f1);
	return f1_saturate;
}

float2 test_saturate_Float2()
{
	float2 f2_saturate = saturate(g_f2);
	return f2_saturate;
}

float3 test_saturate_Float3()
{
	float3 f3_saturate = saturate(g_f3);
	return f3_saturate;
}

float4 test_saturate_Float4()
{
	float4 f4_saturate = saturate(g_f4);
	return f4_saturate;
}

float test_sin_Float()
{
	float f_sin = sin(g_f);
	return f_sin;
}

float1 test_sin_Float1()
{
	float1 f1_sin = sin(g_f1);
	return f1_sin;
}

float2 test_sin_Float2()
{
	float2 f2_sin = sin(g_f2);
	return f2_sin;
}

float3 test_sin_Float3()
{
	float3 f3_sin = sin(g_f3);
	return f3_sin;
}

float4 test_sin_Float4()
{
	float4 f4_sin = sin(g_f4);
	return f4_sin;
}

float test_sinh_Float()
{
	float f_sinh = sinh(g_f);
	return f_sinh;
}

float1 test_sinh_Float1()
{
	float1 f1_sinh = sinh(g_f1);
	return f1_sinh;
}

float2 test_sinh_Float2()
{
	float2 f2_sinh = sinh(g_f2);
	return f2_sinh;
}

float3 test_sinh_Float3()
{
	float3 f3_sinh = sinh(g_f3);
	return f3_sinh;
}

float4 test_sinh_Float4()
{
	float4 f4_sinh = sinh(g_f4);
	return f4_sinh;
}

float test_sqrt_Float()
{
	float f_sqrt = sqrt(g_f);
	return f_sqrt;
}

float1 test_sqrt_Float1()
{
	float1 f1_sqrt = sqrt(g_f1);
	return f1_sqrt;
}

float2 test_sqrt_Float2()
{
	float2 f2_sqrt = sqrt(g_f2);
	return f2_sqrt;
}

float3 test_sqrt_Float3()
{
	float3 f3_sqrt = sqrt(g_f3);
	return f3_sqrt;
}

float4 test_sqrt_Float4()
{
	float4 f4_sqrt = sqrt(g_f4);
	return f4_sqrt;
}

float test_tan_Float()
{
	float f_tan = tan(g_f);
	return f_tan;
}

float1 test_tan_Float1()
{
	float1 f1_tan = tan(g_f1);
	return f1_tan;
}

float2 test_tan_Float2()
{
	float2 f2_tan = tan(g_f2);
	return f2_tan;
}

float3 test_tan_Float3()
{
	float3 f3_tan = tan(g_f3);
	return f3_tan;
}

float4 test_tan_Float4()
{
	float4 f4_tan = tan(g_f4);
	return f4_tan;
}

float test_tanh_Float()
{
	float f_tanh = tanh(g_f);
	return f_tanh;
}

float1 test_tanh_Float1()
{
	float1 f1_tanh = tanh(g_f1);
	return f1_tanh;
}

float2 test_tanh_Float2()
{
	float2 f2_tanh = tanh(g_f2);
	return f2_tanh;
}

float3 test_tanh_Float3()
{
	float3 f3_tanh = tanh(g_f3);
	return f3_tanh;
}

float4 test_tanh_Float4()
{
	float4 f4_tanh = tanh(g_f4);
	return f4_tanh;
}

float test_trunc_Float()
{
	float f_trunc = trunc(g_f);
	return f_trunc;
}

float1 test_trunc_Float1()
{
	float1 f1_trunc = trunc(g_f1);
	return f1_trunc;
}

float2 test_trunc_Float2()
{
	float2 f2_trunc = trunc(g_f2);
	return f2_trunc;
}

float3 test_trunc_Float3()
{
	float3 f3_trunc = trunc(g_f3);
	return f3_trunc;
}

float4 test_trunc_Float4()
{
	float4 f4_trunc = trunc(g_f4);
	return f4_trunc;
}

