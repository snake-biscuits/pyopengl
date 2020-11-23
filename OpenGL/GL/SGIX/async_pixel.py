"""OpenGL extension SGIX.async_pixel

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.async_pixel to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces a new asynchronous mode for texture
	download, pixel download and pixel readback commands.  It allows
	programs to transfer textures or images between the host and the
	graphics accelerator in parallel with the execution of other
	graphics commands (possibly taking advantage of a secondary path
	to the graphics accelerator).  It also allows programs to issue
	non-blocking pixel readback commands that return immediately after
	they are issued so that the program can issue other commands while
	the readback takes place.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/async_pixel.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.async_pixel import *
from OpenGL.raw.GL.SGIX.async_pixel import _EXTENSION_NAME

def glInitAsyncPixelSGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION