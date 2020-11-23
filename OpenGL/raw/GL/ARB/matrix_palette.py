"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_matrix_palette"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_matrix_palette",error_checker=_errors._error_checker)
GL_CURRENT_MATRIX_INDEX_ARB=_C("GL_CURRENT_MATRIX_INDEX_ARB",0x8845)
GL_CURRENT_PALETTE_MATRIX_ARB=_C("GL_CURRENT_PALETTE_MATRIX_ARB",0x8843)
GL_MATRIX_INDEX_ARRAY_ARB=_C("GL_MATRIX_INDEX_ARRAY_ARB",0x8844)
GL_MATRIX_INDEX_ARRAY_POINTER_ARB=_C("GL_MATRIX_INDEX_ARRAY_POINTER_ARB",0x8849)
GL_MATRIX_INDEX_ARRAY_SIZE_ARB=_C("GL_MATRIX_INDEX_ARRAY_SIZE_ARB",0x8846)
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB=_C("GL_MATRIX_INDEX_ARRAY_STRIDE_ARB",0x8848)
GL_MATRIX_INDEX_ARRAY_TYPE_ARB=_C("GL_MATRIX_INDEX_ARRAY_TYPE_ARB",0x8847)
GL_MATRIX_PALETTE_ARB=_C("GL_MATRIX_PALETTE_ARB",0x8840)
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB=_C("GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB",0x8841)
GL_MAX_PALETTE_MATRICES_ARB=_C("GL_MAX_PALETTE_MATRICES_ARB",0x8842)
@_f
@_p.types(None,_cs.GLint)
def glCurrentPaletteMatrixARB(index):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glMatrixIndexPointerARB(size,type,stride,pointer):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLubyteArray)
def glMatrixIndexubvARB(size,indices):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLuintArray)
def glMatrixIndexuivARB(size,indices):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLushortArray)
def glMatrixIndexusvARB(size,indices):pass
