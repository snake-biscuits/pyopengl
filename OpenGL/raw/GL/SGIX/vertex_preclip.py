"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_SGIX_vertex_preclip"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_SGIX_vertex_preclip",error_checker=_errors._error_checker)
GL_VERTEX_PRECLIP_HINT_SGIX=_C("GL_VERTEX_PRECLIP_HINT_SGIX",0x83EF)
GL_VERTEX_PRECLIP_SGIX=_C("GL_VERTEX_PRECLIP_SGIX",0x83EE)

