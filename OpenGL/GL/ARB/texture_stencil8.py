"""OpenGL extension ARB.texture_stencil8

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_stencil8 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension accepts STENCIL_INDEX8 as a texture internal format, and
	adds STENCIL_INDEX8 to the required internal format list. This removes the
	need to use renderbuffers if a stencil-only format is desired.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/texture_stencil8.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_stencil8 import *
from OpenGL.raw.GL.ARB.texture_stencil8 import _EXTENSION_NAME

def glInitTextureStencil8ARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION