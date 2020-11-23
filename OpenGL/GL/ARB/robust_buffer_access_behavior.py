"""OpenGL extension ARB.robust_buffer_access_behavior

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.robust_buffer_access_behavior to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension specifies the behavior of out-of-bounds buffer and array
	accesses. This is an improvement over the existing ARB_robustness
	extension which stated that the application should not crash, but
	the behavior is otherwise undefined. This extension specifies the access
	protection provided by the GL to ensure that out-of-bounds accesses
	cannot read from or write to data not owned by the application. All
	accesses are contained within the buffer object and program area they
	reference. These additional robustness guarantees apply to contexts
	created with the CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB feature enabled.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/robust_buffer_access_behavior.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.robust_buffer_access_behavior import *
from OpenGL.raw.GL.ARB.robust_buffer_access_behavior import _EXTENSION_NAME

def glInitRobustBufferAccessBehaviorARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION