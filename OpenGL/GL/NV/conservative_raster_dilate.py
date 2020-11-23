"""OpenGL extension NV.conservative_raster_dilate

This module customises the behaviour of the 
OpenGL.raw.GL.NV.conservative_raster_dilate to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the conservative rasterization functionality 
	provided by NV_conservative_raster. It provides a new control to generate 
	an "over-conservative" rasterization by dilating primitives prior to 
	rasterization.
	
	When using conservative raster to bin geometry, this extension provides a 
	programmable overlap region between adjacent primitives.  Regular 
	rasterization bins triangles with a shared edge uniquely into pixels. 
	Conservative raster has a one-pixel overlap along the shared edge.  Using 
	a half-pixel raster dilation, this overlap region increases to two pixels.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/conservative_raster_dilate.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.conservative_raster_dilate import *
from OpenGL.raw.GL.NV.conservative_raster_dilate import _EXTENSION_NAME

def glInitConservativeRasterDilateNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION