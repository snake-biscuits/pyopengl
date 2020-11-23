"""OpenGL extension ATI.texture_float

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.texture_float to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds texture internal formats with 32 and 16 bit
	floating-point components.  The 32 bit floating-point components
	are in the standard IEEE float format.  The 16 bit floating-point
	components have 1 sign bit, 5 exponent bits, and 10 mantissa bits.
	Floating-point components are clamped to the limits of the range
	representable by their format.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ATI/texture_float.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ATI.texture_float import *
from OpenGL.raw.GL.ATI.texture_float import _EXTENSION_NAME

def glInitTextureFloatATI():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION