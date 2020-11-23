"""OpenGL extension DL.stereo_control

This module customises the behaviour of the 
OpenGL.raw.WGL.DL.stereo_control to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/DL/stereo_control.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.WGL import _types, _glgets
from OpenGL.raw.WGL.DL.stereo_control import *
from OpenGL.raw.WGL.DL.stereo_control import _EXTENSION_NAME

def glInitStereoControlDL():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION