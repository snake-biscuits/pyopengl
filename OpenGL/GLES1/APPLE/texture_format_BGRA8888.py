"""OpenGL extension APPLE.texture_format_BGRA8888

This module customises the behaviour of the 
OpenGL.raw.GLES1.APPLE.texture_format_BGRA8888 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces BGRA_EXT as an acceptable external format.  
	This avoids byte swizzling when loading RGBA internal format
	textures, which may be stored in BGRA order internally.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/APPLE/texture_format_BGRA8888.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.APPLE.texture_format_BGRA8888 import *
from OpenGL.raw.GLES1.APPLE.texture_format_BGRA8888 import _EXTENSION_NAME

def glInitTextureFormatBgra8888APPLE():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION