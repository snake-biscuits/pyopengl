"""OpenGL extension NVX.conditional_render

This module customises the behaviour of the 
OpenGL.raw.GL.NVX.conditional_render to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides support for conditional rendering based on the
	results of an occlusion query.  This mechanism allows an application to
	potentially reduce the latency between the completion of an occlusion
	query and the rendering commands depending on its result.  It additionally
	allows the decision of whether to render to be made without application
	intervention.
	
	This extension defines two new functions, BeginConditionalRenderNVX and
	EndConditionalRenderNVX, between which rendering commands may be discarded
	based on the results of an occlusion query.  If the specified occlusion
	query returns a non-zero value, rendering commands between these calls are
	executed.  If the occlusion query returns a value of zero, all rendering
	commands between the calls are discarded.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NVX/conditional_render.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NVX.conditional_render import *
from OpenGL.raw.GL.NVX.conditional_render import _EXTENSION_NAME

def glInitConditionalRenderNVX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION