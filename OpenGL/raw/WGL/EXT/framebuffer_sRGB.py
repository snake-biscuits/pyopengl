"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "WGL_EXT_framebuffer_sRGB"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.WGL,"WGL_EXT_framebuffer_sRGB",error_checker=_errors._error_checker)
WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT=_C("WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT",0x20A9)

