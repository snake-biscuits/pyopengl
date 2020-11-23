"""OpenGL extension EXT.output_base

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.output_base to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/output_base.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.output_base import *
from OpenGL.raw.EGL.EXT.output_base import _EXTENSION_NAME

def glInitOutputBaseEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION