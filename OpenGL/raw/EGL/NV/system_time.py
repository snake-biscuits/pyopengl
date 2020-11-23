"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "EGL_NV_system_time"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.EGL,"EGL_NV_system_time",error_checker=_errors._error_checker)

@_f
@_p.types(_cs.EGLuint64NV,)
def eglGetSystemTimeFrequencyNV():pass
@_f
@_p.types(_cs.EGLuint64NV,)
def eglGetSystemTimeNV():pass
