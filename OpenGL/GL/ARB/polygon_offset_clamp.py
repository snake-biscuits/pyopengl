"""OpenGL extension ARB.polygon_offset_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.polygon_offset_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds a new parameter to the polygon offset function
	that clamps the calculated offset to a minimum or maximum value.
	The clamping functionality is useful when polygons are nearly
	parallel to the view direction because their high slopes can result
	in arbitrarily large polygon offsets. In the particular case of
	shadow mapping, the lack of clamping can produce the appearance of
	unwanted holes when the shadow casting polygons are offset beyond
	the shadow receiving polygons, and this problem can be alleviated by
	enforcing a maximum offset value.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/polygon_offset_clamp.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.polygon_offset_clamp import *
from OpenGL.raw.GL.ARB.polygon_offset_clamp import _EXTENSION_NAME

def glInitPolygonOffsetClampARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION