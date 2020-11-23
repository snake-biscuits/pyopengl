"""OpenGL extension ARB.texture_border_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_border_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	The base OpenGL provides clamping such that the texture coordinates are
	limited to exactly the range [0,1].  When a texture coordinate is clamped
	using this algorithm, the texture sampling filter straddles the edge of
	the texture image, taking 1/2 its sample values from within the texture
	image, and the other 1/2 from the texture border.  It is sometimes
	desirable for a texture to be clamped to the border color, rather than to
	an average of the border and edge colors.
	
	This extension defines an additional texture clamping algorithm.
	CLAMP_TO_BORDER_ARB clamps texture coordinates at all mipmap levels such
	that NEAREST and LINEAR filters return only the color of the border
	texels.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/texture_border_clamp.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_border_clamp import *
from OpenGL.raw.GL.ARB.texture_border_clamp import _EXTENSION_NAME

def glInitTextureBorderClampARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION