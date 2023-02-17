cbuffer cb : register(b0)
{
	float g_f;
};

float test_acos()
{
	float f_acos = acos(g_f);
	return f_acos;
}

float test_asin()
{
	float f_asin = asin(g_f);
	return f_asin;
}

float test_atan()
{
	float f_atan = atan(g_f);
	return f_atan;
}

float test_ceil()
{
	float f_ceil = ceil(g_f);
	return f_ceil;
}

float test_cos()
{
	float f_cos = cos(g_f);
	return f_cos;
}

float test_cosh()
{
	float f_cosh = cosh(g_f);
	return f_cosh;
}

float test_ddx()
{
	float f_ddx = ddx(g_f);
	return f_ddx;
}

float test_ddx_coarse()
{
	float f_ddx_coarse = ddx_coarse(g_f);
	return f_ddx_coarse;
}

float test_ddx_fine()
{
	float f_ddx_fine = ddx_fine(g_f);
	return f_ddx_fine;
}

float test_ddy()
{
	float f_ddy = ddy(g_f);
	return f_ddy;
}

float test_ddy_coarse()
{
	float f_ddy_coarse = ddy_coarse(g_f);
	return f_ddy_coarse;
}

float test_ddy_fine()
{
	float f_ddy_fine = ddy_fine(g_f);
	return f_ddy_fine;
}

float test_degrees()
{
	float f_degrees = degrees(g_f);
	return f_degrees;
}

float test_exp()
{
	float f_exp = exp(g_f);
	return f_exp;
}

float test_exp2()
{
	float f_exp2 = exp2(g_f);
	return f_exp2;
}

float test_floor()
{
	float f_floor = floor(g_f);
	return f_floor;
}

float test_frac()
{
	float f_frac = frac(g_f);
	return f_frac;
}

float test_fwidth()
{
	float f_fwidth = fwidth(g_f);
	return f_fwidth;
}

float test_log()
{
	float f_log = log(g_f);
	return f_log;
}

float test_log10()
{
	float f_log10 = log10(g_f);
	return f_log10;
}

float test_log2()
{
	float f_log2 = log2(g_f);
	return f_log2;
}

float test_radians()
{
	float f_radians = radians(g_f);
	return f_radians;
}

float test_rcp()
{
	float f_rcp = rcp(g_f);
	return f_rcp;
}

float test_round()
{
	float f_round = round(g_f);
	return f_round;
}

float test_rsqrt()
{
	float f_rsqrt = rsqrt(g_f);
	return f_rsqrt;
}

float test_saturate()
{
	float f_saturate = saturate(g_f);
	return f_saturate;
}

float test_sin()
{
	float f_sin = sin(g_f);
	return f_sin;
}

float test_sinh()
{
	float f_sinh = sinh(g_f);
	return f_sinh;
}

float test_sqrt()
{
	float f_sqrt = sqrt(g_f);
	return f_sqrt;
}

float test_tan()
{
	float f_tan = tan(g_f);
	return f_tan;
}

float test_tanh()
{
	float f_tanh = tanh(g_f);
	return f_tanh;
}

float test_trunc()
{
	float f_trunc = trunc(g_f);
	return f_trunc;
}

