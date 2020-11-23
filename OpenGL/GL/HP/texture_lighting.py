"""OpenGL extension HP.texture_lighting

This module customises the behaviour of the 
OpenGL.raw.GL.HP.texture_lighting to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines a mechanism for applications to request
	that color originating from specular lighting be added to
	the fragment color _after_ texture application.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/HP/texture_lighting.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.HP.texture_lighting import *
from OpenGL.raw.GL.HP.texture_lighting import _EXTENSION_NAME

def glInitTextureLightingHP():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION