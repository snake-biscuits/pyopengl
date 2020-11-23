"""OpenGL extension ANGLE.device_d3d

This module customises the behaviour of the 
OpenGL.raw.EGL.ANGLE.device_d3d to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ANGLE/device_d3d.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.ANGLE.device_d3d import *
from OpenGL.raw.EGL.ANGLE.device_d3d import _EXTENSION_NAME

def glInitDeviceD3DANGLE():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION