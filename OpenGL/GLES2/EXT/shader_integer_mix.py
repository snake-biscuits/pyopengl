"""OpenGL extension EXT.shader_integer_mix

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.shader_integer_mix to provide a more 
Python-friendly API

Overview (from the spec)
	
	GLSL 1.30 (and GLSL ES 3.00) expanded the mix() built-in function to
	operate on a boolean third argument that does not interpolate but
	selects. This extension extends mix() to select between int, uint,
	and bool components.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/shader_integer_mix.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.shader_integer_mix import *
from OpenGL.raw.GLES2.EXT.shader_integer_mix import _EXTENSION_NAME

def glInitShaderIntegerMixEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION