"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_get_texture_sub_image"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_get_texture_sub_image",error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glGetCompressedTextureSubImage(texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glGetTextureSubImage(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,pixels):pass
