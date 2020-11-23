"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "WGL_NV_vertex_array_range"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.WGL,"WGL_NV_vertex_array_range",error_checker=_errors._error_checker)

@_f
@_p.types(ctypes.c_void_p,_cs.GLsizei,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def wglAllocateMemoryNV(size,readfreq,writefreq,priority):pass
@_f
@_p.types(None,ctypes.c_void_p)
def wglFreeMemoryNV(pointer):pass
