"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_EXT_texture_env_dot3"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_EXT_texture_env_dot3",error_checker=_errors._error_checker)
GL_DOT3_RGBA_EXT=_C("GL_DOT3_RGBA_EXT",0x8741)
GL_DOT3_RGB_EXT=_C("GL_DOT3_RGB_EXT",0x8740)

