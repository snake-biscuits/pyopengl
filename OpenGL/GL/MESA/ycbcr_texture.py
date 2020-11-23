"""OpenGL extension MESA.ycbcr_texture

This module customises the behaviour of the 
OpenGL.raw.GL.MESA.ycbcr_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension supports texture images stored in the YCbCr format.
	There is no support for converting YCbCr images to RGB or vice versa
	during pixel transfer.  The texture"s YCbCr colors are converted to
	RGB during texture sampling, after-which, all the usual per-fragment
	operations take place.  Only 2D texture images are supported (not
	glDrawPixels, glReadPixels, etc).
	
	A YCbCr pixel (texel) is a 16-bit unsigned short with two components.
	The first component is luminance (Y).  For pixels in even-numbered
	image columns, the second component is Cb.  For pixels in odd-numbered
	image columns, the second component is Cr.  If one were to convert the
	data to RGB one would need to examine two pixels from columns N and N+1
	(where N is even) to deduce the RGB color.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/MESA/ycbcr_texture.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.MESA.ycbcr_texture import *
from OpenGL.raw.GL.MESA.ycbcr_texture import _EXTENSION_NAME

def glInitYcbcrTextureMESA():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION