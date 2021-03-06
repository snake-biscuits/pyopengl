"""OpenGL extension ARB.transform_feedback_overflow_query

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.transform_feedback_overflow_query to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds new query types which can be used to detect overflow
	of transform feedback buffers. The new query types are also accepted by
	conditional rendering commands.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/transform_feedback_overflow_query.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.transform_feedback_overflow_query import *
from OpenGL.raw.GL.ARB.transform_feedback_overflow_query import _EXTENSION_NAME

def glInitTransformFeedbackOverflowQueryARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION