"""OpenGL extension EXT.texture_sRGB

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_sRGB to provide a more 
Python-friendly API

Overview (from the spec)
	
	Conventional texture formats assume a linear color space.  So for
	a conventional internal texture format such as GL_RGB8, the 256
	discrete values for each 8-bit color component map linearly and
	uniformly to the [0,1] range.
	
	The sRGB color space is based on typical (non-linear) monitor
	characteristics expected in a dimly lit office.  It has been
	standardized by the International Electrotechnical Commission (IEC)
	as IEC 61966-2-1. The sRGB color space roughly corresponds to 2.2
	gamma correction.
	
	This extension adds a few new uncompressed and compressed color
	texture formats with sRGB color components.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/texture_sRGB.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.texture_sRGB import *
from OpenGL.raw.GL.EXT.texture_sRGB import _EXTENSION_NAME

def glInitTextureSrgbEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION