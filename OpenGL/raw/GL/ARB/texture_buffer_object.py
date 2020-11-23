"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_texture_buffer_object"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_texture_buffer_object",error_checker=_errors._error_checker)
GL_MAX_TEXTURE_BUFFER_SIZE_ARB=_C("GL_MAX_TEXTURE_BUFFER_SIZE_ARB",0x8C2B)
GL_TEXTURE_BINDING_BUFFER_ARB=_C("GL_TEXTURE_BINDING_BUFFER_ARB",0x8C2C)
GL_TEXTURE_BUFFER_ARB=_C("GL_TEXTURE_BUFFER_ARB",0x8C2A)
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB=_C("GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB",0x8C2D)
GL_TEXTURE_BUFFER_FORMAT_ARB=_C("GL_TEXTURE_BUFFER_FORMAT_ARB",0x8C2E)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glTexBufferARB(target,internalformat,buffer):pass
