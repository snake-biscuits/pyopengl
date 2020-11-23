"""OpenGL extension APPLE.texture_max_level

This module customises the behaviour of the 
OpenGL.raw.GLES1.APPLE.texture_max_level to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows an application to specify the maximum (coarsest) 
	mipmap level that may be selected for the specified texture.  This maximum
	level is also used to determine which mip levels are considered when 
	determining texture completeness.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/APPLE/texture_max_level.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.APPLE.texture_max_level import *
from OpenGL.raw.GLES1.APPLE.texture_max_level import _EXTENSION_NAME

def glInitTextureMaxLevelAPPLE():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION