"""OpenGL extension MESA.query_renderer

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.query_renderer to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/MESA/query_renderer.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.MESA.query_renderer import *
from OpenGL.raw.GLX.MESA.query_renderer import _EXTENSION_NAME

def glInitQueryRendererMESA():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION