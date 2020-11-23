"""OpenGL extension AMD.draw_buffers_blend

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.draw_buffers_blend to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds upon the ARB_draw_buffers and EXT_draw_buffers2
	extensions. In ARB_draw_buffers (part of OpenGL 2.0), separate values
	could be written to each color buffer.  This was further enhanced by
	EXT_draw_buffers2 by adding in the ability to enable blending and to set
	color write masks independently per color output.
	
	This extension provides the ability to set individual blend equations and
	blend functions for each color output.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/AMD/draw_buffers_blend.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.draw_buffers_blend import *
from OpenGL.raw.GL.AMD.draw_buffers_blend import _EXTENSION_NAME

def glInitDrawBuffersBlendAMD():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION