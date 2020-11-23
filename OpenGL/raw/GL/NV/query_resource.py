"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_query_resource"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_query_resource",error_checker=_errors._error_checker)
GL_QUERY_RESOURCE_BUFFEROBJECT_NV=_C("GL_QUERY_RESOURCE_BUFFEROBJECT_NV",0x9547)
GL_QUERY_RESOURCE_MEMTYPE_VIDMEM_NV=_C("GL_QUERY_RESOURCE_MEMTYPE_VIDMEM_NV",0x9542)
GL_QUERY_RESOURCE_RENDERBUFFER_NV=_C("GL_QUERY_RESOURCE_RENDERBUFFER_NV",0x9546)
GL_QUERY_RESOURCE_SYS_RESERVED_NV=_C("GL_QUERY_RESOURCE_SYS_RESERVED_NV",0x9544)
GL_QUERY_RESOURCE_TEXTURE_NV=_C("GL_QUERY_RESOURCE_TEXTURE_NV",0x9545)
GL_QUERY_RESOURCE_TYPE_VIDMEM_ALLOC_NV=_C("GL_QUERY_RESOURCE_TYPE_VIDMEM_ALLOC_NV",0x9540)
@_f
@_p.types(_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLuint,arrays.GLintArray)
def glQueryResourceNV(queryType,tagId,bufSize,buffer):pass
