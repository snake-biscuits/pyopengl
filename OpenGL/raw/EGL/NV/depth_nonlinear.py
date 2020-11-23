"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "EGL_NV_depth_nonlinear"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.EGL,"EGL_NV_depth_nonlinear",error_checker=_errors._error_checker)
EGL_DEPTH_ENCODING_NONE_NV=_C("EGL_DEPTH_ENCODING_NONE_NV",0)
EGL_DEPTH_ENCODING_NONLINEAR_NV=_C("EGL_DEPTH_ENCODING_NONLINEAR_NV",0x30E3)
EGL_DEPTH_ENCODING_NV=_C("EGL_DEPTH_ENCODING_NV",0x30E2)

