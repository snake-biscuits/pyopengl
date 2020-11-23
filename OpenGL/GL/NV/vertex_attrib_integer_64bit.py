"""OpenGL extension NV.vertex_attrib_integer_64bit

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_attrib_integer_64bit to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides support for specifying vertex attributes with
	64-bit integer components, analagous to the 64-bit floating point support
	added in EXT_vertex_attrib_64bit.
	
	Additionally, it provides the VertexAttribLFormatNV entry point to specify
	bindless vertex attribute arrays with 64-bit integer or floating-point
	components in conjunction with the NV_vertex_buffer_unified_memory
	extension.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/vertex_attrib_integer_64bit.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.vertex_attrib_integer_64bit import *
from OpenGL.raw.GL.NV.vertex_attrib_integer_64bit import _EXTENSION_NAME

def glInitVertexAttribInteger64BitNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

glVertexAttribL1i64vNV=wrapper.wrapper(glVertexAttribL1i64vNV).setInputArraySize(
    "v", 1
)
glVertexAttribL2i64vNV=wrapper.wrapper(glVertexAttribL2i64vNV).setInputArraySize(
    "v", 2
)
glVertexAttribL3i64vNV=wrapper.wrapper(glVertexAttribL3i64vNV).setInputArraySize(
    "v", 3
)
glVertexAttribL4i64vNV=wrapper.wrapper(glVertexAttribL4i64vNV).setInputArraySize(
    "v", 4
)
glVertexAttribL1ui64vNV=wrapper.wrapper(glVertexAttribL1ui64vNV).setInputArraySize(
    "v", 1
)
glVertexAttribL2ui64vNV=wrapper.wrapper(glVertexAttribL2ui64vNV).setInputArraySize(
    "v", 2
)
glVertexAttribL3ui64vNV=wrapper.wrapper(glVertexAttribL3ui64vNV).setInputArraySize(
    "v", 3
)
glVertexAttribL4ui64vNV=wrapper.wrapper(glVertexAttribL4ui64vNV).setInputArraySize(
    "v", 4
)
glGetVertexAttribLi64vNV=wrapper.wrapper(glGetVertexAttribLi64vNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
glGetVertexAttribLui64vNV=wrapper.wrapper(glGetVertexAttribLui64vNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
# END AUTOGENERATED SECTION