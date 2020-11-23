"""OpenGL extension KHR.create_context_no_error

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.create_context_no_error to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/KHR/create_context_no_error.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.KHR.create_context_no_error import *
from OpenGL.raw.EGL.KHR.create_context_no_error import _EXTENSION_NAME

def glInitCreateContextNoErrorKHR():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION