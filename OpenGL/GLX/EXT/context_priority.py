"""OpenGL extension EXT.context_priority

This module customises the behaviour of the 
OpenGL.raw.GLX.EXT.context_priority to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/context_priority.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.EXT.context_priority import *
from OpenGL.raw.GLX.EXT.context_priority import _EXTENSION_NAME

def glInitContextPriorityEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION