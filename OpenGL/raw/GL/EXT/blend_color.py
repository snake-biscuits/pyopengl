"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_EXT_blend_color"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_EXT_blend_color",error_checker=_errors._error_checker)
GL_BLEND_COLOR_EXT=_C("GL_BLEND_COLOR_EXT",0x8005)
GL_CONSTANT_ALPHA_EXT=_C("GL_CONSTANT_ALPHA_EXT",0x8003)
GL_CONSTANT_COLOR_EXT=_C("GL_CONSTANT_COLOR_EXT",0x8001)
GL_ONE_MINUS_CONSTANT_ALPHA_EXT=_C("GL_ONE_MINUS_CONSTANT_ALPHA_EXT",0x8004)
GL_ONE_MINUS_CONSTANT_COLOR_EXT=_C("GL_ONE_MINUS_CONSTANT_COLOR_EXT",0x8002)
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glBlendColorEXT(red,green,blue,alpha):pass
