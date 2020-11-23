"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_SUN_mesh_array"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_SUN_mesh_array",error_checker=_errors._error_checker)
GL_QUAD_MESH_SUN=_C("GL_QUAD_MESH_SUN",0x8614)
GL_TRIANGLE_MESH_SUN=_C("GL_TRIANGLE_MESH_SUN",0x8615)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawMeshArraysSUN(mode,first,count,width):pass
