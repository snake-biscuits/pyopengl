"""OpenGL extension NV.viewport_array2

This module customises the behaviour of the 
OpenGL.raw.GL.NV.viewport_array2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides new support allowing a single primitive to be
	broadcast to multiple viewports and/or multiple layers.  A shader output
	gl_ViewportMask[] is provided, allowing a single primitive to be output to
	multiple viewports simultaneously.  Also, a new shader option is provided
	to control whether the effective viewport index is added into gl_Layer.
	These capabilities allow a single primitive to be output to multiple
	layers simultaneously.
	
	The gl_ViewportMask[] output is available in vertex, tessellation
	control, tessellation evaluation, and geometry shaders. gl_ViewportIndex
	and gl_Layer are also made available in all these shader stages. The
	actual viewport index or mask and render target layer values are taken
	from the last active shader stage from this set of stages.
	
	This extension is a superset of the GL_AMD_vertex_shader_layer and
	GL_AMD_vertex_shader_viewport_index extensions, and thus those extension
	strings are expected to be exported if GL_NV_viewport_array2 is
	supported. This extension includes the edits for those extensions, recast
	against the reorganized OpenGL 4.3 specification.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/viewport_array2.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.viewport_array2 import *
from OpenGL.raw.GL.NV.viewport_array2 import _EXTENSION_NAME

def glInitViewportArray2NV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION