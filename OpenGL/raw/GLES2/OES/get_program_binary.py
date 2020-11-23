"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_OES_get_program_binary"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_OES_get_program_binary",error_checker=_errors._error_checker)
GL_NUM_PROGRAM_BINARY_FORMATS_OES=_C("GL_NUM_PROGRAM_BINARY_FORMATS_OES",0x87FE)
GL_PROGRAM_BINARY_FORMATS_OES=_C("GL_PROGRAM_BINARY_FORMATS_OES",0x87FF)
GL_PROGRAM_BINARY_LENGTH_OES=_C("GL_PROGRAM_BINARY_LENGTH_OES",0x8741)
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLuintArray,ctypes.c_void_p)
def glGetProgramBinaryOES(program,bufSize,length,binaryFormat,binary):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glProgramBinaryOES(program,binaryFormat,binary,length):pass
