"""OpenGL extension NV.draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.draw_buffers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends OpenGL ES 2.0 to allow multiple output
	colors, and provides a mechanism for directing those outputs to
	multiple color buffers.
	
	This extension serves a similar purpose to ARB_draw_buffers except
	that this is for OpenGL ES 2.0.
	
	When OpenGL ES 3.0 is present, this extension relaxes the order
	restriction on color attachments to draw framebuffer objects.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/draw_buffers.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.draw_buffers import *
from OpenGL.raw.GLES2.NV.draw_buffers import _EXTENSION_NAME

def glInitDrawBuffersNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

# INPUT glDrawBuffersNV.bufs size not checked against n
glDrawBuffersNV=wrapper.wrapper(glDrawBuffersNV).setInputArraySize(
    "bufs", None
)
# END AUTOGENERATED SECTION