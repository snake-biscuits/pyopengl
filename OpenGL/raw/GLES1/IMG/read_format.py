"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_IMG_read_format"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_IMG_read_format",error_checker=_errors._error_checker)
GL_BGRA_IMG=_C("GL_BGRA_IMG",0x80E1)
GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG=_C("GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG",0x8365)

