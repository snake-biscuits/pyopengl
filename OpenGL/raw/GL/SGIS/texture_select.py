"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_SGIS_texture_select"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_SGIS_texture_select",error_checker=_errors._error_checker)
GL_DUAL_ALPHA12_SGIS=_C("GL_DUAL_ALPHA12_SGIS",0x8112)
GL_DUAL_ALPHA16_SGIS=_C("GL_DUAL_ALPHA16_SGIS",0x8113)
GL_DUAL_ALPHA4_SGIS=_C("GL_DUAL_ALPHA4_SGIS",0x8110)
GL_DUAL_ALPHA8_SGIS=_C("GL_DUAL_ALPHA8_SGIS",0x8111)
GL_DUAL_INTENSITY12_SGIS=_C("GL_DUAL_INTENSITY12_SGIS",0x811A)
GL_DUAL_INTENSITY16_SGIS=_C("GL_DUAL_INTENSITY16_SGIS",0x811B)
GL_DUAL_INTENSITY4_SGIS=_C("GL_DUAL_INTENSITY4_SGIS",0x8118)
GL_DUAL_INTENSITY8_SGIS=_C("GL_DUAL_INTENSITY8_SGIS",0x8119)
GL_DUAL_LUMINANCE12_SGIS=_C("GL_DUAL_LUMINANCE12_SGIS",0x8116)
GL_DUAL_LUMINANCE16_SGIS=_C("GL_DUAL_LUMINANCE16_SGIS",0x8117)
GL_DUAL_LUMINANCE4_SGIS=_C("GL_DUAL_LUMINANCE4_SGIS",0x8114)
GL_DUAL_LUMINANCE8_SGIS=_C("GL_DUAL_LUMINANCE8_SGIS",0x8115)
GL_DUAL_LUMINANCE_ALPHA4_SGIS=_C("GL_DUAL_LUMINANCE_ALPHA4_SGIS",0x811C)
GL_DUAL_LUMINANCE_ALPHA8_SGIS=_C("GL_DUAL_LUMINANCE_ALPHA8_SGIS",0x811D)
GL_DUAL_TEXTURE_SELECT_SGIS=_C("GL_DUAL_TEXTURE_SELECT_SGIS",0x8124)
GL_QUAD_ALPHA4_SGIS=_C("GL_QUAD_ALPHA4_SGIS",0x811E)
GL_QUAD_ALPHA8_SGIS=_C("GL_QUAD_ALPHA8_SGIS",0x811F)
GL_QUAD_INTENSITY4_SGIS=_C("GL_QUAD_INTENSITY4_SGIS",0x8122)
GL_QUAD_INTENSITY8_SGIS=_C("GL_QUAD_INTENSITY8_SGIS",0x8123)
GL_QUAD_LUMINANCE4_SGIS=_C("GL_QUAD_LUMINANCE4_SGIS",0x8120)
GL_QUAD_LUMINANCE8_SGIS=_C("GL_QUAD_LUMINANCE8_SGIS",0x8121)
GL_QUAD_TEXTURE_SELECT_SGIS=_C("GL_QUAD_TEXTURE_SELECT_SGIS",0x8125)

