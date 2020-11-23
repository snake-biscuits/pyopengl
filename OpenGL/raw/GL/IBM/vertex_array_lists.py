"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_IBM_vertex_array_lists"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_IBM_vertex_array_lists",error_checker=_errors._error_checker)
GL_COLOR_ARRAY_LIST_IBM=_C("GL_COLOR_ARRAY_LIST_IBM",103072)
GL_COLOR_ARRAY_LIST_STRIDE_IBM=_C("GL_COLOR_ARRAY_LIST_STRIDE_IBM",103082)
GL_EDGE_FLAG_ARRAY_LIST_IBM=_C("GL_EDGE_FLAG_ARRAY_LIST_IBM",103075)
GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM=_C("GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM",103085)
GL_FOG_COORDINATE_ARRAY_LIST_IBM=_C("GL_FOG_COORDINATE_ARRAY_LIST_IBM",103076)
GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM=_C("GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM",103086)
GL_INDEX_ARRAY_LIST_IBM=_C("GL_INDEX_ARRAY_LIST_IBM",103073)
GL_INDEX_ARRAY_LIST_STRIDE_IBM=_C("GL_INDEX_ARRAY_LIST_STRIDE_IBM",103083)
GL_NORMAL_ARRAY_LIST_IBM=_C("GL_NORMAL_ARRAY_LIST_IBM",103071)
GL_NORMAL_ARRAY_LIST_STRIDE_IBM=_C("GL_NORMAL_ARRAY_LIST_STRIDE_IBM",103081)
GL_SECONDARY_COLOR_ARRAY_LIST_IBM=_C("GL_SECONDARY_COLOR_ARRAY_LIST_IBM",103077)
GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM=_C("GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM",103087)
GL_TEXTURE_COORD_ARRAY_LIST_IBM=_C("GL_TEXTURE_COORD_ARRAY_LIST_IBM",103074)
GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM=_C("GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM",103084)
GL_VERTEX_ARRAY_LIST_IBM=_C("GL_VERTEX_ARRAY_LIST_IBM",103070)
GL_VERTEX_ARRAY_LIST_STRIDE_IBM=_C("GL_VERTEX_ARRAY_LIST_STRIDE_IBM",103080)
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glColorPointerListIBM(size,type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLbooleanArray,_cs.GLint)
def glEdgeFlagPointerListIBM(stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glFogCoordPointerListIBM(type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glIndexPointerListIBM(type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glNormalPointerListIBM(type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glSecondaryColorPointerListIBM(size,type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glTexCoordPointerListIBM(size,type,stride,pointer,ptrstride):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLint,arrays.GLvoidpArray,_cs.GLint)
def glVertexPointerListIBM(size,type,stride,pointer,ptrstride):pass
