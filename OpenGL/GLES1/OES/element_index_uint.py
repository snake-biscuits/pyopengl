"""OpenGL extension OES.element_index_uint

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.element_index_uint to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL ES 1.0 supports DrawElements with <type> value of
	UNSIGNED_BYTE and UNSIGNED_SHORT.  This extension adds
	support for UNSIGNED_INT <type> values.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OES/element_index_uint.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.element_index_uint import *
from OpenGL.raw.GLES1.OES.element_index_uint import _EXTENSION_NAME

def glInitElementIndexUintOES():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION