"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_texture_swizzle"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_texture_swizzle",error_checker=_errors._error_checker)
GL_TEXTURE_SWIZZLE_A=_C("GL_TEXTURE_SWIZZLE_A",0x8E45)
GL_TEXTURE_SWIZZLE_B=_C("GL_TEXTURE_SWIZZLE_B",0x8E44)
GL_TEXTURE_SWIZZLE_G=_C("GL_TEXTURE_SWIZZLE_G",0x8E43)
GL_TEXTURE_SWIZZLE_R=_C("GL_TEXTURE_SWIZZLE_R",0x8E42)
GL_TEXTURE_SWIZZLE_RGBA=_C("GL_TEXTURE_SWIZZLE_RGBA",0x8E46)

