"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_OES_point_size_array"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_OES_point_size_array",error_checker=_errors._error_checker)
GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES=_C("GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES",0x8B9F)
GL_POINT_SIZE_ARRAY_OES=_C("GL_POINT_SIZE_ARRAY_OES",0x8B9C)
GL_POINT_SIZE_ARRAY_POINTER_OES=_C("GL_POINT_SIZE_ARRAY_POINTER_OES",0x898C)
GL_POINT_SIZE_ARRAY_STRIDE_OES=_C("GL_POINT_SIZE_ARRAY_STRIDE_OES",0x898B)
GL_POINT_SIZE_ARRAY_TYPE_OES=_C("GL_POINT_SIZE_ARRAY_TYPE_OES",0x898A)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glPointSizePointerOES(type,stride,pointer):pass
