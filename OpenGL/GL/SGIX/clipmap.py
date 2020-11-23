"""OpenGL extension SGIX.clipmap

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.clipmap to provide a more 
Python-friendly API

Overview (from the spec)
	
	Mipmaps provide a general but expensive solution when the texture image
	is very large.  This extension defines clipmaps, which occupy a small
	subset of the memory required by equivalent mipmaps, but provide much
	of the mipmap rendering capabilities.  Clipmaps are especially useful
	for rendering terrain.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/clipmap.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.clipmap import *
from OpenGL.raw.GL.SGIX.clipmap import _EXTENSION_NAME

def glInitClipmapSGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION