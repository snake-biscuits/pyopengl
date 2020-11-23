"""OpenGL extension EXT.shader_texture_lod

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.shader_texture_lod to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds additional texture functions to the
	OpenGL ES Shading Language which provide the shader writer
	with explicit control of LOD.
	
	Mipmap texture fetches and anisotropic texture fetches
	require implicit derivatives to calculate rho, lambda
	and/or the line of anisotropy.  These implicit derivatives
	will be undefined for texture fetches occurring inside
	non-uniform control flow or for vertex shader texture
	fetches, resulting in undefined texels.
	
	The additional texture functions introduced with
	this extension provide explicit control of LOD
	(isotropic texture functions) or provide explicit
	derivatives (anisotropic texture functions).
	
	Anisotropic texture functions return defined texels
	for mipmap texture fetches or anisotropic texture fetches,
	even inside non-uniform control flow.  Isotropic texture
	functions return defined texels for mipmap texture fetches,
	even inside non-uniform control flow.  However, isotropic
	texture functions return undefined texels for anisotropic
	texture fetches.
	
	The existing isotropic vertex texture functions:
	
	    vec4 texture2DLodEXT(sampler2D sampler,
	                         vec2 coord, 
	                         float lod);
	    vec4 texture2DProjLodEXT(sampler2D sampler,
	                             vec3 coord, 
	                             float lod);
	    vec4 texture2DProjLodEXT(sampler2D sampler,
	                             vec4 coord, 
	                             float lod);
	
	    vec4 textureCubeLodEXT(samplerCube sampler,
	                           vec3 coord,
	                           float lod);
	
	are added to the built-in functions for fragment shaders
	with "EXT" suffix appended.
	
	New anisotropic texture functions, providing explicit
	derivatives:
	
	    vec4 texture2DGradEXT(sampler2D sampler,
	                          vec2 P, 
	                          vec2 dPdx, 
	                          vec2  dPdy);
	    vec4 texture2DProjGradEXT(sampler2D sampler,
	                              vec3 P, 
	                              vec2 dPdx, 
	                              vec2 dPdy);
	    vec4 texture2DProjGradEXT(sampler2D sampler,
	                              vec4 P,
	                              vec2 dPdx, 
	                              vec2 dPdy);
	
	    vec4 textureCubeGradEXT(samplerCube sampler,
	                            vec3 P,
	                            vec3 dPdx, 
	                            vec3 dPdy);
	
	 are added to the built-in functions for vertex shaders
	 and fragment shaders.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/shader_texture_lod.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.shader_texture_lod import *
from OpenGL.raw.GLES2.EXT.shader_texture_lod import _EXTENSION_NAME

def glInitShaderTextureLodEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION