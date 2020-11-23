"""OpenGL extension OES.mapbuffer

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.mapbuffer to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds to the vertex buffer object functionality supported
	by OpenGL ES 1.1 or ES 2.0 by allowing the entire data storage of a
	buffer object to be mapped into the client"s address space.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OES/mapbuffer.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.mapbuffer import *
from OpenGL.raw.GLES2.OES.mapbuffer import _EXTENSION_NAME

def glInitMapbufferOES():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION