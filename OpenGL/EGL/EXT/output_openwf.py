"""OpenGL extension EXT.output_openwf

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.output_openwf to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/output_openwf.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.output_openwf import *
from OpenGL.raw.EGL.EXT.output_openwf import _EXTENSION_NAME

def glInitOutputOpenwfEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION