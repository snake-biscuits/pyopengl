"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_EXT_texture3D"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_EXT_texture3D",error_checker=_errors._error_checker)
GL_MAX_3D_TEXTURE_SIZE_EXT=_C("GL_MAX_3D_TEXTURE_SIZE_EXT",0x8073)
GL_PACK_IMAGE_HEIGHT_EXT=_C("GL_PACK_IMAGE_HEIGHT_EXT",0x806C)
GL_PACK_SKIP_IMAGES_EXT=_C("GL_PACK_SKIP_IMAGES_EXT",0x806B)
GL_PROXY_TEXTURE_3D_EXT=_C("GL_PROXY_TEXTURE_3D_EXT",0x8070)
GL_TEXTURE_3D_EXT=_C("GL_TEXTURE_3D_EXT",0x806F)
GL_TEXTURE_DEPTH_EXT=_C("GL_TEXTURE_DEPTH_EXT",0x8071)
GL_TEXTURE_WRAP_R_EXT=_C("GL_TEXTURE_WRAP_R_EXT",0x8072)
GL_UNPACK_IMAGE_HEIGHT_EXT=_C("GL_UNPACK_IMAGE_HEIGHT_EXT",0x806E)
GL_UNPACK_SKIP_IMAGES_EXT=_C("GL_UNPACK_SKIP_IMAGES_EXT",0x806D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage3DEXT(target,level,internalformat,width,height,depth,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage3DEXT(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
