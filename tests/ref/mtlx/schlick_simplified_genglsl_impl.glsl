#include "mx_generalized_schlick_bsdf.glsl"
void schlick_metal(ClosureData closureData, vec3 color0, vec3 color90, vec2 roughness, vec3 normal, vec3 tangent, out BSDF out_)
{
	mx_generalized_schlick_bsdf(closureData, 1.0, color0, vec3(1.0, 1.0, 1.0), color90, 5.0, roughness, 0.0, 1.5, normal, tangent, 0, 0, out_);
}

