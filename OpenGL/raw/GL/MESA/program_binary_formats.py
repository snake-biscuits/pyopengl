"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_MESA_program_binary_formats"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_MESA_program_binary_formats",error_checker=_errors._error_checker)
GL_PROGRAM_BINARY_FORMAT_MESA=_C("GL_PROGRAM_BINARY_FORMAT_MESA",0x875F)

