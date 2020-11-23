"""OpenGL extension QCOM.alpha_test

This module customises the behaviour of the 
OpenGL.raw.GLES2.QCOM.alpha_test to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension reintroduces the alpha test per-fragment operation
	from OpenGL ES 1.x.  Some hardware has a dedicated unit capable of
	performing this operation, and it can save ALU operations in the fragment
	shader by avoiding the conditional discard.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/QCOM/alpha_test.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.QCOM.alpha_test import *
from OpenGL.raw.GLES2.QCOM.alpha_test import _EXTENSION_NAME

def glInitAlphaTestQCOM():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION