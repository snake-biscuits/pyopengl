"""OpenGL extension SGIX.fog_offset

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.fog_offset to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows fragments to look brighter in a foggy
	environment, by biasing the fragment eye-coordinate distance prior
	to fog computation. A reference point in eye space (rx ry rz) and an offset
	amount toward the viewpoint (f_o) are specified. When fog offset is
	enabled, the offset amount will be subtracted from the fragment
	distance, making objects appear less foggy.
	
	If fog computation is done in screen-space coordinates under
	perspective projection, the reference point is used in adjusting the
	fog offset to be correct for fragments whose depth is close to that
	point. The reference point should be redefined when it becomes too
	far away from the primitives being drawn. Under orthographic
	projection, or if fog computation is done in eye-space coordinates,
	the reference point is ignored.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/fog_offset.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.fog_offset import *
from OpenGL.raw.GL.SGIX.fog_offset import _EXTENSION_NAME

def glInitFogOffsetSGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION