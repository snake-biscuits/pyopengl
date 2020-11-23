"""OpenGL extension ARB.shader_bit_encoding

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_bit_encoding to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension trivially adds built-in functions for getting/setting
	the bit encoding for floating-point values in the OpenGL Shading Language.
	
	These functions are pulled out of ARB_gpu_shader5, since support for such
	built-in functions exists in current hardware.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/shader_bit_encoding.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shader_bit_encoding import *
from OpenGL.raw.GL.ARB.shader_bit_encoding import _EXTENSION_NAME

def glInitShaderBitEncodingARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION