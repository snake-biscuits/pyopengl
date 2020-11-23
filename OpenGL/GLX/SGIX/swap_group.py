"""OpenGL extension SGIX.swap_group

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIX.swap_group to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/swap_group.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.SGIX.swap_group import *
from OpenGL.raw.GLX.SGIX.swap_group import _EXTENSION_NAME

def glInitSwapGroupSGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION