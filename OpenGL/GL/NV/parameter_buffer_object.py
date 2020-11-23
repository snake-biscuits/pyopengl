"""OpenGL extension NV.parameter_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.NV.parameter_buffer_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension, in conjunction with NV_gpu_program4, provides a new type
	of program parameter than can be used as a constant during vertex,
	fragment, or geometry program execution.  Each program target has a set of
	parameter buffer binding points to which buffer objects can be attached.
	
	A vertex, fragment, or geometry program can read data from the attached
	buffer objects using a binding of the form "program.buffer[a][b]".  This
	binding reads data from the buffer object attached to binding point <a>.
	The buffer object attached is treated either as an array of 32-bit words
	or an array of four-component vectors, and the binding above reads the
	array element numbered <b>.
	
	The use of buffer objects allows applications to change large blocks of
	program parameters at once, simply by binding a new buffer object.  It
	also provides a number of new ways to load parameter values, including
	readback from the frame buffer (EXT_pixel_buffer_object), transform
	feedback (NV_transform_feedback), buffer object loading functions such as
	MapBuffer and BufferData, as well as dedicated parameter buffer update
	functions provided by this extension.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/parameter_buffer_object.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.parameter_buffer_object import *
from OpenGL.raw.GL.NV.parameter_buffer_object import _EXTENSION_NAME

def glInitParameterBufferObjectNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

# INPUT glProgramBufferParametersfvNV.params size not checked against count
glProgramBufferParametersfvNV=wrapper.wrapper(glProgramBufferParametersfvNV).setInputArraySize(
    "params", None
)
# INPUT glProgramBufferParametersIivNV.params size not checked against count
glProgramBufferParametersIivNV=wrapper.wrapper(glProgramBufferParametersIivNV).setInputArraySize(
    "params", None
)
# INPUT glProgramBufferParametersIuivNV.params size not checked against count
glProgramBufferParametersIuivNV=wrapper.wrapper(glProgramBufferParametersIuivNV).setInputArraySize(
    "params", None
)
# END AUTOGENERATED SECTION