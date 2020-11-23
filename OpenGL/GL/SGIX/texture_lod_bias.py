"""OpenGL extension SGIX.texture_lod_bias

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.texture_lod_bias to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension modifies the calculation of texture level of detail 
	parameter LOD, which is represented by the Greek character lambda
	in the GL Specification. The LOD equation assumes that a 2^n x 2^m x 2^l
	texture is band limited at 2^(n-1), 2^(m-1), 2^(l-1).  Often a texture is 
	oversampled or filtered such that the texture is band limited at lower
	frequencies in one or more dimensions.  The result is that texture-mapped 
	primitives appear excessively blurry.  This extension provides biases 
	for n, m, and l in the LOD calculation to to compensate for under or over 
	sampled texture images.  Mipmapped textures can be made to appear sharper or
	blurrier by supplying a negative or positive bias respectively. 
	
	Examples of textures which can benefit from this LOD control include
	video-capture images which are filtered differently horizontally and
	vertically; a texture which appears blurry because it is mapped with 
	a nonuniform scale, such as a road texture which is repeated hundreds of 
	times in one dimension and only once in the other; and textures which
	had to be magnified to a power-of-two for mipmapping.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/texture_lod_bias.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.texture_lod_bias import *
from OpenGL.raw.GL.SGIX.texture_lod_bias import _EXTENSION_NAME

def glInitTextureLodBiasSGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION