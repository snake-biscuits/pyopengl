"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_AMD_depth_clamp_separate"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_AMD_depth_clamp_separate",error_checker=_errors._error_checker)
GL_DEPTH_CLAMP_FAR_AMD=_C("GL_DEPTH_CLAMP_FAR_AMD",0x901F)
GL_DEPTH_CLAMP_NEAR_AMD=_C("GL_DEPTH_CLAMP_NEAR_AMD",0x901E)

