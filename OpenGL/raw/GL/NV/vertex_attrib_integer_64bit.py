"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_vertex_attrib_integer_64bit"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_vertex_attrib_integer_64bit",error_checker=_errors._error_checker)
GL_INT64_NV=_C("GL_INT64_NV",0x140E)
GL_UNSIGNED_INT64_NV=_C("GL_UNSIGNED_INT64_NV",0x140F)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetVertexAttribLi64vNV(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetVertexAttribLui64vNV(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint64EXT)
def glVertexAttribL1i64NV(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLint64Array)
def glVertexAttribL1i64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT)
def glVertexAttribL1ui64NV(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuint64Array)
def glVertexAttribL1ui64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint64EXT,_cs.GLint64EXT)
def glVertexAttribL2i64NV(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLint64Array)
def glVertexAttribL2i64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glVertexAttribL2ui64NV(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuint64Array)
def glVertexAttribL2ui64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glVertexAttribL3i64NV(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLint64Array)
def glVertexAttribL3i64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glVertexAttribL3ui64NV(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuint64Array)
def glVertexAttribL3ui64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glVertexAttribL4i64NV(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLint64Array)
def glVertexAttribL4i64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glVertexAttribL4ui64NV(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuint64Array)
def glVertexAttribL4ui64vNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei)
def glVertexAttribLFormatNV(index,size,type,stride):pass
