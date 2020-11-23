"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_VERSION_GL_3_1"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_VERSION_GL_3_1",error_checker=_errors._error_checker)
GL_ACTIVE_UNIFORM_BLOCKS=_C("GL_ACTIVE_UNIFORM_BLOCKS",0x8A36)
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH=_C("GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH",0x8A35)
GL_COPY_READ_BUFFER=_C("GL_COPY_READ_BUFFER",0x8F36)
GL_COPY_WRITE_BUFFER=_C("GL_COPY_WRITE_BUFFER",0x8F37)
GL_INT_SAMPLER_2D_RECT=_C("GL_INT_SAMPLER_2D_RECT",0x8DCD)
GL_INT_SAMPLER_BUFFER=_C("GL_INT_SAMPLER_BUFFER",0x8DD0)
GL_INVALID_INDEX=_C("GL_INVALID_INDEX",0xFFFFFFFF)
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS=_C("GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS",0x8A33)
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS=_C("GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS",0x8A32)
GL_MAX_COMBINED_UNIFORM_BLOCKS=_C("GL_MAX_COMBINED_UNIFORM_BLOCKS",0x8A2E)
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS=_C("GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS",0x8A31)
GL_MAX_FRAGMENT_UNIFORM_BLOCKS=_C("GL_MAX_FRAGMENT_UNIFORM_BLOCKS",0x8A2D)
GL_MAX_GEOMETRY_UNIFORM_BLOCKS=_C("GL_MAX_GEOMETRY_UNIFORM_BLOCKS",0x8A2C)
GL_MAX_RECTANGLE_TEXTURE_SIZE=_C("GL_MAX_RECTANGLE_TEXTURE_SIZE",0x84F8)
GL_MAX_TEXTURE_BUFFER_SIZE=_C("GL_MAX_TEXTURE_BUFFER_SIZE",0x8C2B)
GL_MAX_UNIFORM_BLOCK_SIZE=_C("GL_MAX_UNIFORM_BLOCK_SIZE",0x8A30)
GL_MAX_UNIFORM_BUFFER_BINDINGS=_C("GL_MAX_UNIFORM_BUFFER_BINDINGS",0x8A2F)
GL_MAX_VERTEX_UNIFORM_BLOCKS=_C("GL_MAX_VERTEX_UNIFORM_BLOCKS",0x8A2B)
GL_PRIMITIVE_RESTART=_C("GL_PRIMITIVE_RESTART",0x8F9D)
GL_PRIMITIVE_RESTART_INDEX=_C("GL_PRIMITIVE_RESTART_INDEX",0x8F9E)
GL_PROXY_TEXTURE_RECTANGLE=_C("GL_PROXY_TEXTURE_RECTANGLE",0x84F7)
GL_R16_SNORM=_C("GL_R16_SNORM",0x8F98)
GL_R8_SNORM=_C("GL_R8_SNORM",0x8F94)
GL_RG16_SNORM=_C("GL_RG16_SNORM",0x8F99)
GL_RG8_SNORM=_C("GL_RG8_SNORM",0x8F95)
GL_RGB16_SNORM=_C("GL_RGB16_SNORM",0x8F9A)
GL_RGB8_SNORM=_C("GL_RGB8_SNORM",0x8F96)
GL_RGBA16_SNORM=_C("GL_RGBA16_SNORM",0x8F9B)
GL_RGBA8_SNORM=_C("GL_RGBA8_SNORM",0x8F97)
GL_SAMPLER_2D_RECT=_C("GL_SAMPLER_2D_RECT",0x8B63)
GL_SAMPLER_2D_RECT_SHADOW=_C("GL_SAMPLER_2D_RECT_SHADOW",0x8B64)
GL_SAMPLER_BUFFER=_C("GL_SAMPLER_BUFFER",0x8DC2)
GL_SIGNED_NORMALIZED=_C("GL_SIGNED_NORMALIZED",0x8F9C)
GL_TEXTURE_BINDING_BUFFER=_C("GL_TEXTURE_BINDING_BUFFER",0x8C2C)
GL_TEXTURE_BINDING_RECTANGLE=_C("GL_TEXTURE_BINDING_RECTANGLE",0x84F6)
GL_TEXTURE_BUFFER=_C("GL_TEXTURE_BUFFER",0x8C2A)
GL_TEXTURE_BUFFER_DATA_STORE_BINDING=_C("GL_TEXTURE_BUFFER_DATA_STORE_BINDING",0x8C2D)
GL_TEXTURE_RECTANGLE=_C("GL_TEXTURE_RECTANGLE",0x84F5)
GL_UNIFORM_ARRAY_STRIDE=_C("GL_UNIFORM_ARRAY_STRIDE",0x8A3C)
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS=_C("GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS",0x8A42)
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES=_C("GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES",0x8A43)
GL_UNIFORM_BLOCK_BINDING=_C("GL_UNIFORM_BLOCK_BINDING",0x8A3F)
GL_UNIFORM_BLOCK_DATA_SIZE=_C("GL_UNIFORM_BLOCK_DATA_SIZE",0x8A40)
GL_UNIFORM_BLOCK_INDEX=_C("GL_UNIFORM_BLOCK_INDEX",0x8A3A)
GL_UNIFORM_BLOCK_NAME_LENGTH=_C("GL_UNIFORM_BLOCK_NAME_LENGTH",0x8A41)
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER=_C("GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER",0x8A46)
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER=_C("GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER",0x8A45)
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER=_C("GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER",0x8A44)
GL_UNIFORM_BUFFER=_C("GL_UNIFORM_BUFFER",0x8A11)
GL_UNIFORM_BUFFER_BINDING=_C("GL_UNIFORM_BUFFER_BINDING",0x8A28)
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT=_C("GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT",0x8A34)
GL_UNIFORM_BUFFER_SIZE=_C("GL_UNIFORM_BUFFER_SIZE",0x8A2A)
GL_UNIFORM_BUFFER_START=_C("GL_UNIFORM_BUFFER_START",0x8A29)
GL_UNIFORM_IS_ROW_MAJOR=_C("GL_UNIFORM_IS_ROW_MAJOR",0x8A3E)
GL_UNIFORM_MATRIX_STRIDE=_C("GL_UNIFORM_MATRIX_STRIDE",0x8A3D)
GL_UNIFORM_NAME_LENGTH=_C("GL_UNIFORM_NAME_LENGTH",0x8A39)
GL_UNIFORM_OFFSET=_C("GL_UNIFORM_OFFSET",0x8A3B)
GL_UNIFORM_SIZE=_C("GL_UNIFORM_SIZE",0x8A38)
GL_UNIFORM_TYPE=_C("GL_UNIFORM_TYPE",0x8A37)
GL_UNSIGNED_INT_SAMPLER_2D_RECT=_C("GL_UNSIGNED_INT_SAMPLER_2D_RECT",0x8DD5)
GL_UNSIGNED_INT_SAMPLER_BUFFER=_C("GL_UNSIGNED_INT_SAMPLER_BUFFER",0x8DD8)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBase(target,index,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRange(target,index,buffer,offset,size):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glCopyBufferSubData(readTarget,writeTarget,readOffset,writeOffset,size):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawArraysInstanced(mode,first,count,instancecount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glDrawElementsInstanced(mode,count,type,indices,instancecount):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetActiveUniformBlockName(program,uniformBlockIndex,bufSize,length,uniformBlockName):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetActiveUniformBlockiv(program,uniformBlockIndex,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetActiveUniformName(program,uniformIndex,bufSize,length,uniformName):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,_cs.GLenum,arrays.GLintArray)
def glGetActiveUniformsiv(program,uniformCount,uniformIndices,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetIntegeri_v(target,index,data):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glGetUniformBlockIndex(program,uniformBlockName):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER(ctypes.POINTER(_cs.GLchar)),arrays.GLuintArray)
def glGetUniformIndices(program,uniformCount,uniformNames,uniformIndices):pass
@_f
@_p.types(None,_cs.GLuint)
def glPrimitiveRestartIndex(index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glTexBuffer(target,internalformat,buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniformBlockBinding(program,uniformBlockIndex,uniformBlockBinding):pass
