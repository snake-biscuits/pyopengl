"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_VERSION_GL_1_2"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_VERSION_GL_1_2",error_checker=_errors._error_checker)
GL_ALIASED_LINE_WIDTH_RANGE=_C("GL_ALIASED_LINE_WIDTH_RANGE",0x846E)
GL_ALIASED_POINT_SIZE_RANGE=_C("GL_ALIASED_POINT_SIZE_RANGE",0x846D)
GL_BGR=_C("GL_BGR",0x80E0)
GL_BGRA=_C("GL_BGRA",0x80E1)
GL_CLAMP_TO_EDGE=_C("GL_CLAMP_TO_EDGE",0x812F)
GL_LIGHT_MODEL_COLOR_CONTROL=_C("GL_LIGHT_MODEL_COLOR_CONTROL",0x81F8)
GL_MAX_3D_TEXTURE_SIZE=_C("GL_MAX_3D_TEXTURE_SIZE",0x8073)
GL_MAX_ELEMENTS_INDICES=_C("GL_MAX_ELEMENTS_INDICES",0x80E9)
GL_MAX_ELEMENTS_VERTICES=_C("GL_MAX_ELEMENTS_VERTICES",0x80E8)
GL_PACK_IMAGE_HEIGHT=_C("GL_PACK_IMAGE_HEIGHT",0x806C)
GL_PACK_SKIP_IMAGES=_C("GL_PACK_SKIP_IMAGES",0x806B)
GL_PROXY_TEXTURE_3D=_C("GL_PROXY_TEXTURE_3D",0x8070)
GL_RESCALE_NORMAL=_C("GL_RESCALE_NORMAL",0x803A)
GL_SEPARATE_SPECULAR_COLOR=_C("GL_SEPARATE_SPECULAR_COLOR",0x81FA)
GL_SINGLE_COLOR=_C("GL_SINGLE_COLOR",0x81F9)
GL_SMOOTH_LINE_WIDTH_GRANULARITY=_C("GL_SMOOTH_LINE_WIDTH_GRANULARITY",0x0B23)
GL_SMOOTH_LINE_WIDTH_RANGE=_C("GL_SMOOTH_LINE_WIDTH_RANGE",0x0B22)
GL_SMOOTH_POINT_SIZE_GRANULARITY=_C("GL_SMOOTH_POINT_SIZE_GRANULARITY",0x0B13)
GL_SMOOTH_POINT_SIZE_RANGE=_C("GL_SMOOTH_POINT_SIZE_RANGE",0x0B12)
GL_TEXTURE_3D=_C("GL_TEXTURE_3D",0x806F)
GL_TEXTURE_BASE_LEVEL=_C("GL_TEXTURE_BASE_LEVEL",0x813C)
GL_TEXTURE_BINDING_3D=_C("GL_TEXTURE_BINDING_3D",0x806A)
GL_TEXTURE_DEPTH=_C("GL_TEXTURE_DEPTH",0x8071)
GL_TEXTURE_MAX_LEVEL=_C("GL_TEXTURE_MAX_LEVEL",0x813D)
GL_TEXTURE_MAX_LOD=_C("GL_TEXTURE_MAX_LOD",0x813B)
GL_TEXTURE_MIN_LOD=_C("GL_TEXTURE_MIN_LOD",0x813A)
GL_TEXTURE_WRAP_R=_C("GL_TEXTURE_WRAP_R",0x8072)
GL_UNPACK_IMAGE_HEIGHT=_C("GL_UNPACK_IMAGE_HEIGHT",0x806E)
GL_UNPACK_SKIP_IMAGES=_C("GL_UNPACK_SKIP_IMAGES",0x806D)
GL_UNSIGNED_BYTE_2_3_3_REV=_C("GL_UNSIGNED_BYTE_2_3_3_REV",0x8362)
GL_UNSIGNED_BYTE_3_3_2=_C("GL_UNSIGNED_BYTE_3_3_2",0x8032)
GL_UNSIGNED_INT_10_10_10_2=_C("GL_UNSIGNED_INT_10_10_10_2",0x8036)
GL_UNSIGNED_INT_2_10_10_10_REV=_C("GL_UNSIGNED_INT_2_10_10_10_REV",0x8368)
GL_UNSIGNED_INT_8_8_8_8=_C("GL_UNSIGNED_INT_8_8_8_8",0x8035)
GL_UNSIGNED_INT_8_8_8_8_REV=_C("GL_UNSIGNED_INT_8_8_8_8_REV",0x8367)
GL_UNSIGNED_SHORT_1_5_5_5_REV=_C("GL_UNSIGNED_SHORT_1_5_5_5_REV",0x8366)
GL_UNSIGNED_SHORT_4_4_4_4=_C("GL_UNSIGNED_SHORT_4_4_4_4",0x8033)
GL_UNSIGNED_SHORT_4_4_4_4_REV=_C("GL_UNSIGNED_SHORT_4_4_4_4_REV",0x8365)
GL_UNSIGNED_SHORT_5_5_5_1=_C("GL_UNSIGNED_SHORT_5_5_5_1",0x8034)
GL_UNSIGNED_SHORT_5_6_5=_C("GL_UNSIGNED_SHORT_5_6_5",0x8363)
GL_UNSIGNED_SHORT_5_6_5_REV=_C("GL_UNSIGNED_SHORT_5_6_5_REV",0x8364)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage3D(target,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawRangeElements(mode,start,end,count,type,indices):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage3D(target,level,internalformat,width,height,depth,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage3D(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
