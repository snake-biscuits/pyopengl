"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_SGIS_fog_function"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_SGIS_fog_function",error_checker=_errors._error_checker)
GL_FOG_FUNC_POINTS_SGIS=_C("GL_FOG_FUNC_POINTS_SGIS",0x812B)
GL_FOG_FUNC_SGIS=_C("GL_FOG_FUNC_SGIS",0x812A)
GL_MAX_FOG_FUNC_POINTS_SGIS=_C("GL_MAX_FOG_FUNC_POINTS_SGIS",0x812C)
@_f
@_p.types(None,_cs.GLsizei,arrays.GLfloatArray)
def glFogFuncSGIS(n,points):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glGetFogFuncSGIS(points):pass
