"""OpenGL extension AMD.stencil_operation_extended

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.stencil_operation_extended to provide a more 
Python-friendly API

Overview (from the spec)
	
	Stencil buffers are special buffers that allow tests to be made against an
	incoming value and action taken based on that value. The stencil buffer is
	updated during rasterization, and the operation used to update the stencil
	buffer is chosen based on whether the fragment passes the stencil test,
	and if it does, whether it passes the depth test. Traditional OpenGL
	includes support for several primitive operations, such as incrementing,
	or clearing the content of the stencil buffer, or replacing it with a
	specified reference value.
	
	This extension adds support for an additional set of operations that may
	be performed on the stencil buffer under each circumstance. Additionally,
	this extension separates the value used as the source for stencil
	operations from the reference value, allowing different values to be used
	in the stencil test, and in the update of the stencil buffer.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/AMD/stencil_operation_extended.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.stencil_operation_extended import *
from OpenGL.raw.GL.AMD.stencil_operation_extended import _EXTENSION_NAME

def glInitStencilOperationExtendedAMD():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION