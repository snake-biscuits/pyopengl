"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_APPLE_flush_buffer_range"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_APPLE_flush_buffer_range",error_checker=_errors._error_checker)
GL_BUFFER_FLUSHING_UNMAP_APPLE=_C("GL_BUFFER_FLUSHING_UNMAP_APPLE",0x8A13)
GL_BUFFER_SERIALIZED_MODIFY_APPLE=_C("GL_BUFFER_SERIALIZED_MODIFY_APPLE",0x8A12)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glBufferParameteriAPPLE(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedBufferRangeAPPLE(target,offset,size):pass
