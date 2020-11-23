"""OpenGL extension NV.video_output

This module customises the behaviour of the 
OpenGL.raw.GLX.NV.video_output to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/video_output.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.NV.video_output import *
from OpenGL.raw.GLX.NV.video_output import _EXTENSION_NAME

def glInitVideoOutputNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION