"""OpenGL extension EXT.platform_base

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.platform_base to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/platform_base.txt
"""
from OpenGL import constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.platform_base import *
from OpenGL.raw.EGL.EXT.platform_base import _EXTENSION_NAME

# Cannot use this to check for the extension because the extension
# checking requires a context
#eglGetPlatformDisplayEXT.extension = None

def glInitPlatformBaseEXT():
    """Return boolean indicating whether this extension is available"""
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION
eglGetPlatformDisplayEXT.extension = None
eglGetPlatformDisplayEXT.force_extension = True 
