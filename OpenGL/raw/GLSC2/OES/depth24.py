"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLSC2 import _types as _cs
# End users want this...
from OpenGL.raw.GLSC2._types import *
from OpenGL.raw.GLSC2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLSC2_OES_depth24"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLSC2,"GLSC2_OES_depth24",error_checker=_errors._error_checker)
GL_DEPTH_COMPONENT24_OES=_C("GL_DEPTH_COMPONENT24_OES",0x81A6)

