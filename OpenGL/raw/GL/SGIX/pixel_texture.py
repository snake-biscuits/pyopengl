"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_SGIX_pixel_texture"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_SGIX_pixel_texture",error_checker=_errors._error_checker)
GL_PIXEL_TEX_GEN_MODE_SGIX=_C("GL_PIXEL_TEX_GEN_MODE_SGIX",0x832B)
GL_PIXEL_TEX_GEN_SGIX=_C("GL_PIXEL_TEX_GEN_SGIX",0x8139)
@_f
@_p.types(None,_cs.GLenum)
def glPixelTexGenSGIX(mode):pass
