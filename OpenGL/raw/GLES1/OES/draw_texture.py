"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_OES_draw_texture"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_OES_draw_texture",error_checker=_errors._error_checker)
GL_TEXTURE_CROP_RECT_OES=_C("GL_TEXTURE_CROP_RECT_OES",0x8B9D)
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glDrawTexfOES(x,y,z,width,height):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glDrawTexfvOES(coords):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glDrawTexiOES(x,y,z,width,height):pass
@_f
@_p.types(None,arrays.GLintArray)
def glDrawTexivOES(coords):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glDrawTexsOES(x,y,z,width,height):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glDrawTexsvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glDrawTexxOES(x,y,z,width,height):pass
@_f
@_p.types(None,arrays.GLfixedArray)
def glDrawTexxvOES(coords):pass
