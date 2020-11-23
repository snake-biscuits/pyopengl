"""OpenGL extension EXT.platform_wayland

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.platform_wayland to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/platform_wayland.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.platform_wayland import *
from OpenGL.raw.EGL.EXT.platform_wayland import _EXTENSION_NAME

def glInitPlatformWaylandEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION