"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_EXT_buffer_storage"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_EXT_buffer_storage",error_checker=_errors._error_checker)
GL_BUFFER_IMMUTABLE_STORAGE_EXT=_C("GL_BUFFER_IMMUTABLE_STORAGE_EXT",0x821F)
GL_BUFFER_STORAGE_FLAGS_EXT=_C("GL_BUFFER_STORAGE_FLAGS_EXT",0x8220)
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT=_C("GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT",0x00004000)
GL_CLIENT_STORAGE_BIT_EXT=_C("GL_CLIENT_STORAGE_BIT_EXT",0x0200)
GL_DYNAMIC_STORAGE_BIT_EXT=_C("GL_DYNAMIC_STORAGE_BIT_EXT",0x0100)
GL_MAP_COHERENT_BIT_EXT=_C("GL_MAP_COHERENT_BIT_EXT",0x0080)
GL_MAP_PERSISTENT_BIT_EXT=_C("GL_MAP_PERSISTENT_BIT_EXT",0x0040)
GL_MAP_READ_BIT=_C("GL_MAP_READ_BIT",0x0001)
GL_MAP_WRITE_BIT=_C("GL_MAP_WRITE_BIT",0x0002)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLbitfield)
def glBufferStorageEXT(target,size,data,flags):pass
