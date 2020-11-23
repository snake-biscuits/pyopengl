"""OpenGL extension KHR.no_error

This module customises the behaviour of the 
OpenGL.raw.GLES2.KHR.no_error to provide a more 
Python-friendly API

Overview (from the spec)
	
	With this extension enabled any behavior that generates a GL error will
	have undefined behavior.  The reason this extension exists is performance
	can be increased and power usage decreased.  When this mode is used, a GL
	driver can have undefined behavior where it would have generated a GL error
	without this extension.  This could include application termination.  In
	general this extension should be used after you have verified all the GL
	errors are removed, and an application is not the kind that would check
	for GL errors and adjust behavior based on those errors.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/KHR/no_error.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.KHR.no_error import *
from OpenGL.raw.GLES2.KHR.no_error import _EXTENSION_NAME

def glInitNoErrorKHR():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION