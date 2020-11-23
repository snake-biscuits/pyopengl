"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_vertex_buffer_unified_memory"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_vertex_buffer_unified_memory",error_checker=_errors._error_checker)
GL_COLOR_ARRAY_ADDRESS_NV=_C("GL_COLOR_ARRAY_ADDRESS_NV",0x8F23)
GL_COLOR_ARRAY_LENGTH_NV=_C("GL_COLOR_ARRAY_LENGTH_NV",0x8F2D)
GL_DRAW_INDIRECT_ADDRESS_NV=_C("GL_DRAW_INDIRECT_ADDRESS_NV",0x8F41)
GL_DRAW_INDIRECT_LENGTH_NV=_C("GL_DRAW_INDIRECT_LENGTH_NV",0x8F42)
GL_DRAW_INDIRECT_UNIFIED_NV=_C("GL_DRAW_INDIRECT_UNIFIED_NV",0x8F40)
GL_EDGE_FLAG_ARRAY_ADDRESS_NV=_C("GL_EDGE_FLAG_ARRAY_ADDRESS_NV",0x8F26)
GL_EDGE_FLAG_ARRAY_LENGTH_NV=_C("GL_EDGE_FLAG_ARRAY_LENGTH_NV",0x8F30)
GL_ELEMENT_ARRAY_ADDRESS_NV=_C("GL_ELEMENT_ARRAY_ADDRESS_NV",0x8F29)
GL_ELEMENT_ARRAY_LENGTH_NV=_C("GL_ELEMENT_ARRAY_LENGTH_NV",0x8F33)
GL_ELEMENT_ARRAY_UNIFIED_NV=_C("GL_ELEMENT_ARRAY_UNIFIED_NV",0x8F1F)
GL_FOG_COORD_ARRAY_ADDRESS_NV=_C("GL_FOG_COORD_ARRAY_ADDRESS_NV",0x8F28)
GL_FOG_COORD_ARRAY_LENGTH_NV=_C("GL_FOG_COORD_ARRAY_LENGTH_NV",0x8F32)
GL_INDEX_ARRAY_ADDRESS_NV=_C("GL_INDEX_ARRAY_ADDRESS_NV",0x8F24)
GL_INDEX_ARRAY_LENGTH_NV=_C("GL_INDEX_ARRAY_LENGTH_NV",0x8F2E)
GL_NORMAL_ARRAY_ADDRESS_NV=_C("GL_NORMAL_ARRAY_ADDRESS_NV",0x8F22)
GL_NORMAL_ARRAY_LENGTH_NV=_C("GL_NORMAL_ARRAY_LENGTH_NV",0x8F2C)
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV=_C("GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV",0x8F27)
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV=_C("GL_SECONDARY_COLOR_ARRAY_LENGTH_NV",0x8F31)
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV=_C("GL_TEXTURE_COORD_ARRAY_ADDRESS_NV",0x8F25)
GL_TEXTURE_COORD_ARRAY_LENGTH_NV=_C("GL_TEXTURE_COORD_ARRAY_LENGTH_NV",0x8F2F)
GL_VERTEX_ARRAY_ADDRESS_NV=_C("GL_VERTEX_ARRAY_ADDRESS_NV",0x8F21)
GL_VERTEX_ARRAY_LENGTH_NV=_C("GL_VERTEX_ARRAY_LENGTH_NV",0x8F2B)
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV=_C("GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV",0x8F20)
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV=_C("GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV",0x8F2A)
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV=_C("GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV",0x8F1E)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint64EXT,_cs.GLsizeiptr)
def glBufferAddressRangeNV(pname,index,address,length):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glColorFormatNV(size,type,stride):pass
@_f
@_p.types(None,_cs.GLsizei)
def glEdgeFlagFormatNV(stride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei)
def glFogCoordFormatNV(type,stride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLuint64Array)
def glGetIntegerui64i_vNV(value,index,result):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei)
def glIndexFormatNV(type,stride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei)
def glNormalFormatNV(type,stride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glSecondaryColorFormatNV(size,type,stride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glTexCoordFormatNV(size,type,stride):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLsizei)
def glVertexAttribFormatNV(index,size,type,normalized,stride):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glVertexAttribIFormatNV(index,size,type,stride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glVertexFormatNV(size,type,stride):pass
