"""OpenGL extension ARB.window_pos

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.window_pos to provide a more 
Python-friendly API

Overview (from the spec)
	
	In order to set the current raster position to a specific window
	coordinate with the RasterPos command, the modelview matrix, projection
	matrix and viewport must be set very carefully.  Furthermore, if the
	desired window coordinate is outside of the window"s bounds one must rely
	on a subtle side-effect of the Bitmap command in order to avoid frustum
	clipping.
	
	This extension provides a set of functions to directly set the current
	raster position in window coordinates, bypassing the modelview matrix, the
	projection matrix and the viewport-to-window mapping.  Furthermore, clip
	testing is not performed, so that the current raster position is always
	valid.
	
	This greatly simplifies the process of setting the current raster position
	to a specific window coordinate prior to calling DrawPixels, CopyPixels or
	Bitmap.  Many matrix operations can be avoided when mixing 2D and 3D
	rendering.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/window_pos.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.window_pos import *
from OpenGL.raw.GL.ARB.window_pos import _EXTENSION_NAME

def glInitWindowPosARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

glWindowPos2dvARB=wrapper.wrapper(glWindowPos2dvARB).setInputArraySize(
    "v", 2
)
glWindowPos2fvARB=wrapper.wrapper(glWindowPos2fvARB).setInputArraySize(
    "v", 2
)
glWindowPos2ivARB=wrapper.wrapper(glWindowPos2ivARB).setInputArraySize(
    "v", 2
)
glWindowPos2svARB=wrapper.wrapper(glWindowPos2svARB).setInputArraySize(
    "v", 2
)
glWindowPos3dvARB=wrapper.wrapper(glWindowPos3dvARB).setInputArraySize(
    "v", 3
)
glWindowPos3fvARB=wrapper.wrapper(glWindowPos3fvARB).setInputArraySize(
    "v", 3
)
glWindowPos3ivARB=wrapper.wrapper(glWindowPos3ivARB).setInputArraySize(
    "v", 3
)
glWindowPos3svARB=wrapper.wrapper(glWindowPos3svARB).setInputArraySize(
    "v", 3
)
# END AUTOGENERATED SECTION
