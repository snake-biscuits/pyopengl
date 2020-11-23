"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_ANGLE_instanced_arrays"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_ANGLE_instanced_arrays",error_checker=_errors._error_checker)
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE=_C("GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE",0x88FE)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawArraysInstancedANGLE(mode,first,count,primcount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glDrawElementsInstancedANGLE(mode,count,type,indices,primcount):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribDivisorANGLE(index,divisor):pass
