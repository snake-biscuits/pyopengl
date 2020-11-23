"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_clip_control"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_clip_control",error_checker=_errors._error_checker)
GL_CLIP_DEPTH_MODE=_C("GL_CLIP_DEPTH_MODE",0x935D)
GL_CLIP_ORIGIN=_C("GL_CLIP_ORIGIN",0x935C)
GL_LOWER_LEFT=_C("GL_LOWER_LEFT",0x8CA1)
GL_NEGATIVE_ONE_TO_ONE=_C("GL_NEGATIVE_ONE_TO_ONE",0x935E)
GL_UPPER_LEFT=_C("GL_UPPER_LEFT",0x8CA2)
GL_ZERO_TO_ONE=_C("GL_ZERO_TO_ONE",0x935F)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glClipControl(origin,depth):pass
