"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_VERSION_GL_1_5"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_VERSION_GL_1_5",error_checker=_errors._error_checker)
GL_ARRAY_BUFFER=_C("GL_ARRAY_BUFFER",0x8892)
GL_ARRAY_BUFFER_BINDING=_C("GL_ARRAY_BUFFER_BINDING",0x8894)
GL_BUFFER_ACCESS=_C("GL_BUFFER_ACCESS",0x88BB)
GL_BUFFER_MAPPED=_C("GL_BUFFER_MAPPED",0x88BC)
GL_BUFFER_MAP_POINTER=_C("GL_BUFFER_MAP_POINTER",0x88BD)
GL_BUFFER_SIZE=_C("GL_BUFFER_SIZE",0x8764)
GL_BUFFER_USAGE=_C("GL_BUFFER_USAGE",0x8765)
GL_COLOR_ARRAY_BUFFER_BINDING=_C("GL_COLOR_ARRAY_BUFFER_BINDING",0x8898)
GL_CURRENT_FOG_COORD=_C("GL_CURRENT_FOG_COORD",0x8453)
GL_CURRENT_QUERY=_C("GL_CURRENT_QUERY",0x8865)
GL_DYNAMIC_COPY=_C("GL_DYNAMIC_COPY",0x88EA)
GL_DYNAMIC_DRAW=_C("GL_DYNAMIC_DRAW",0x88E8)
GL_DYNAMIC_READ=_C("GL_DYNAMIC_READ",0x88E9)
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING=_C("GL_EDGE_FLAG_ARRAY_BUFFER_BINDING",0x889B)
GL_ELEMENT_ARRAY_BUFFER=_C("GL_ELEMENT_ARRAY_BUFFER",0x8893)
GL_ELEMENT_ARRAY_BUFFER_BINDING=_C("GL_ELEMENT_ARRAY_BUFFER_BINDING",0x8895)
GL_FOG_COORD=_C("GL_FOG_COORD",0x8451)
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING=_C("GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING",0x889D)
GL_FOG_COORD_ARRAY=_C("GL_FOG_COORD_ARRAY",0x8457)
GL_FOG_COORD_ARRAY_BUFFER_BINDING=_C("GL_FOG_COORD_ARRAY_BUFFER_BINDING",0x889D)
GL_FOG_COORD_ARRAY_POINTER=_C("GL_FOG_COORD_ARRAY_POINTER",0x8456)
GL_FOG_COORD_ARRAY_STRIDE=_C("GL_FOG_COORD_ARRAY_STRIDE",0x8455)
GL_FOG_COORD_ARRAY_TYPE=_C("GL_FOG_COORD_ARRAY_TYPE",0x8454)
GL_FOG_COORD_SRC=_C("GL_FOG_COORD_SRC",0x8450)
GL_INDEX_ARRAY_BUFFER_BINDING=_C("GL_INDEX_ARRAY_BUFFER_BINDING",0x8899)
GL_NORMAL_ARRAY_BUFFER_BINDING=_C("GL_NORMAL_ARRAY_BUFFER_BINDING",0x8897)
GL_QUERY_COUNTER_BITS=_C("GL_QUERY_COUNTER_BITS",0x8864)
GL_QUERY_RESULT=_C("GL_QUERY_RESULT",0x8866)
GL_QUERY_RESULT_AVAILABLE=_C("GL_QUERY_RESULT_AVAILABLE",0x8867)
GL_READ_ONLY=_C("GL_READ_ONLY",0x88B8)
GL_READ_WRITE=_C("GL_READ_WRITE",0x88BA)
GL_SAMPLES_PASSED=_C("GL_SAMPLES_PASSED",0x8914)
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING=_C("GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING",0x889C)
GL_SRC0_ALPHA=_C("GL_SRC0_ALPHA",0x8588)
GL_SRC0_RGB=_C("GL_SRC0_RGB",0x8580)
GL_SRC1_ALPHA=_C("GL_SRC1_ALPHA",0x8589)
GL_SRC1_RGB=_C("GL_SRC1_RGB",0x8581)
GL_SRC2_ALPHA=_C("GL_SRC2_ALPHA",0x858A)
GL_SRC2_RGB=_C("GL_SRC2_RGB",0x8582)
GL_STATIC_COPY=_C("GL_STATIC_COPY",0x88E6)
GL_STATIC_DRAW=_C("GL_STATIC_DRAW",0x88E4)
GL_STATIC_READ=_C("GL_STATIC_READ",0x88E5)
GL_STREAM_COPY=_C("GL_STREAM_COPY",0x88E2)
GL_STREAM_DRAW=_C("GL_STREAM_DRAW",0x88E0)
GL_STREAM_READ=_C("GL_STREAM_READ",0x88E1)
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING=_C("GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING",0x889A)
GL_VERTEX_ARRAY_BUFFER_BINDING=_C("GL_VERTEX_ARRAY_BUFFER_BINDING",0x8896)
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING=_C("GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING",0x889F)
GL_WEIGHT_ARRAY_BUFFER_BINDING=_C("GL_WEIGHT_ARRAY_BUFFER_BINDING",0x889E)
GL_WRITE_ONLY=_C("GL_WRITE_ONLY",0x88B9)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBeginQuery(target,id):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindBuffer(target,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLenum)
def glBufferData(target,size,data,usage):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glBufferSubData(target,offset,size,data):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteQueries(n,ids):pass
@_f
@_p.types(None,_cs.GLenum)
def glEndQuery(target):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenQueries(n,ids):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetBufferParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLvoidpArray)
def glGetBufferPointerv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glGetBufferSubData(target,offset,size,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetQueryObjectiv(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetQueryObjectuiv(id,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetQueryiv(target,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsBuffer(buffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsQuery(id):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLenum,_cs.GLenum)
def glMapBuffer(target,access):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glUnmapBuffer(target):pass
