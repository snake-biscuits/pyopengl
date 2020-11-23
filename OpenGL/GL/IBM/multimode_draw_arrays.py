"""OpenGL extension IBM.multimode_draw_arrays

This module customises the behaviour of the 
OpenGL.raw.GL.IBM.multimode_draw_arrays to provide a more 
Python-friendly API

Overview (from the spec)
	
	These functions behave identically to the standard OpenGL 1.1 functions
	glDrawArrays() and glDrawElements() except they handle multiple lists of
	vertices and multiple primitive modes in one call. Their main purpose is
	to allow one function call to render more than one primitive regardless
	of the primitive mode. 
	
	This extension is similar to the EXT_multi_draw_arrays extension 
	except that it accomodates the specification of a  unique mode for
	each primitive.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/IBM/multimode_draw_arrays.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.IBM.multimode_draw_arrays import *
from OpenGL.raw.GL.IBM.multimode_draw_arrays import _EXTENSION_NAME

def glInitMultimodeDrawArraysIBM():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

# INPUT glMultiModeDrawArraysIBM.count size not checked against "primcount"
# INPUT glMultiModeDrawArraysIBM.first size not checked against "primcount"
# INPUT glMultiModeDrawArraysIBM.mode size not checked against "primcount"
glMultiModeDrawArraysIBM=wrapper.wrapper(glMultiModeDrawArraysIBM).setInputArraySize(
    "count", None
).setInputArraySize(
    "first", None
).setInputArraySize(
    "mode", None
)
# INPUT glMultiModeDrawElementsIBM.count size not checked against "primcount"
# INPUT glMultiModeDrawElementsIBM.indices size not checked against "primcount"
# INPUT glMultiModeDrawElementsIBM.mode size not checked against "primcount"
glMultiModeDrawElementsIBM=wrapper.wrapper(glMultiModeDrawElementsIBM).setInputArraySize(
    "count", None
).setInputArraySize(
    "indices", None
).setInputArraySize(
    "mode", None
)
# END AUTOGENERATED SECTION