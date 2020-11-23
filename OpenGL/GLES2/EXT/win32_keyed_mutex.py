"""OpenGL extension EXT.win32_keyed_mutex

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.win32_keyed_mutex to provide a more 
Python-friendly API

Overview (from the spec)
	
	Direct3D image objects may have a built-in synchronization primitive
	associated with them that can be used to synchronize access to their
	contents across process and API boundaries.  This extension provides
	access to that synchronization primitive via two new commands that
	operate on GL memory objects.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/win32_keyed_mutex.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.win32_keyed_mutex import *
from OpenGL.raw.GLES2.EXT.win32_keyed_mutex import _EXTENSION_NAME

def glInitWin32KeyedMutexEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION