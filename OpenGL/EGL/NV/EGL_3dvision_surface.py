"""OpenGL extension NV.EGL_3dvision_surface

This module customises the behaviour of the 
OpenGL.raw.EGL.NV.EGL_3dvision_surface to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/EGL_3dvision_surface.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.NV.EGL_3dvision_surface import *
from OpenGL.raw.EGL.NV.EGL_3dvision_surface import _EXTENSION_NAME

def glInitEgl3DvisionSurfaceNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION