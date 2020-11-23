"""OpenGL extension EXT.depth_bounds_test

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.depth_bounds_test to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds a new per-fragment test that is, logically,
	after the scissor test and before the alpha test.  The depth bounds
	test compares the depth value stored at the location given by the
	incoming fragment"s (xw,yw) coordinates to a user-defined minimum
	and maximum depth value.  If the stored depth value is outside the
	user-defined range (exclusive), the incoming fragment is discarded.
	
	Unlike the depth test, the depth bounds test has NO dependency on
	the fragment"s window-space depth value.
	
	This functionality is useful in the context of attenuated stenciled
	shadow volume rendering.  To motivate the functionality"s utility
	in this context, we first describe how conventional scissor testing
	can be used to optimize shadow volume rendering.
	
	If an attenuated light source"s illumination can be bounded to a
	rectangle in XY window-space, the conventional scissor test can be
	used to discard shadow volume fragments that are guaranteed to be
	outside the light source"s window-space XY rectangle.  The stencil
	increments and decrements that would otherwise be generated by these
	scissored fragments are inconsequential because the light source"s
	illumination can pre-determined to be fully attenuated outside the
	scissored region.  In other words, the scissor test can be used to
	discard shadow volume fragments rendered outside the scissor, thereby
	improving performance, without affecting the ultimate illumination
	of these pixels with respect to the attenuated light source.
	
	This scissoring optimization can be used both when rendering
	the stenciled shadow volumes to update stencil (incrementing and
	decrementing the stencil buffer) AND when adding the illumination
	contribution of attenuated light source"s.
	
	In a similar fashion, we can compute the attenuated light source"s
	window-space Z bounds (zmin,zmax) of consequential illumination.
	Unless a depth value (in the depth buffer) at a pixel is within
	the range [zmin,zmax], the light source"s illumination can be
	pre-determined to be inconsequential for the pixel.  Said another
	way, the pixel being illuminated is either far enough in front of
	or behind the attenuated light source so that the light source"s
	illumination for the pixel is fully attenuated.  The depth bounds
	test can perform this test.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/depth_bounds_test.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.depth_bounds_test import *
from OpenGL.raw.GL.EXT.depth_bounds_test import _EXTENSION_NAME

def glInitDepthBoundsTestEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION