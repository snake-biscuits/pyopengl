"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_evaluators"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_evaluators",error_checker=_errors._error_checker)
GL_EVAL_2D_NV=_C("GL_EVAL_2D_NV",0x86C0)
GL_EVAL_FRACTIONAL_TESSELLATION_NV=_C("GL_EVAL_FRACTIONAL_TESSELLATION_NV",0x86C5)
GL_EVAL_TRIANGULAR_2D_NV=_C("GL_EVAL_TRIANGULAR_2D_NV",0x86C1)
GL_EVAL_VERTEX_ATTRIB0_NV=_C("GL_EVAL_VERTEX_ATTRIB0_NV",0x86C6)
GL_EVAL_VERTEX_ATTRIB10_NV=_C("GL_EVAL_VERTEX_ATTRIB10_NV",0x86D0)
GL_EVAL_VERTEX_ATTRIB11_NV=_C("GL_EVAL_VERTEX_ATTRIB11_NV",0x86D1)
GL_EVAL_VERTEX_ATTRIB12_NV=_C("GL_EVAL_VERTEX_ATTRIB12_NV",0x86D2)
GL_EVAL_VERTEX_ATTRIB13_NV=_C("GL_EVAL_VERTEX_ATTRIB13_NV",0x86D3)
GL_EVAL_VERTEX_ATTRIB14_NV=_C("GL_EVAL_VERTEX_ATTRIB14_NV",0x86D4)
GL_EVAL_VERTEX_ATTRIB15_NV=_C("GL_EVAL_VERTEX_ATTRIB15_NV",0x86D5)
GL_EVAL_VERTEX_ATTRIB1_NV=_C("GL_EVAL_VERTEX_ATTRIB1_NV",0x86C7)
GL_EVAL_VERTEX_ATTRIB2_NV=_C("GL_EVAL_VERTEX_ATTRIB2_NV",0x86C8)
GL_EVAL_VERTEX_ATTRIB3_NV=_C("GL_EVAL_VERTEX_ATTRIB3_NV",0x86C9)
GL_EVAL_VERTEX_ATTRIB4_NV=_C("GL_EVAL_VERTEX_ATTRIB4_NV",0x86CA)
GL_EVAL_VERTEX_ATTRIB5_NV=_C("GL_EVAL_VERTEX_ATTRIB5_NV",0x86CB)
GL_EVAL_VERTEX_ATTRIB6_NV=_C("GL_EVAL_VERTEX_ATTRIB6_NV",0x86CC)
GL_EVAL_VERTEX_ATTRIB7_NV=_C("GL_EVAL_VERTEX_ATTRIB7_NV",0x86CD)
GL_EVAL_VERTEX_ATTRIB8_NV=_C("GL_EVAL_VERTEX_ATTRIB8_NV",0x86CE)
GL_EVAL_VERTEX_ATTRIB9_NV=_C("GL_EVAL_VERTEX_ATTRIB9_NV",0x86CF)
GL_MAP_ATTRIB_U_ORDER_NV=_C("GL_MAP_ATTRIB_U_ORDER_NV",0x86C3)
GL_MAP_ATTRIB_V_ORDER_NV=_C("GL_MAP_ATTRIB_V_ORDER_NV",0x86C4)
GL_MAP_TESSELLATION_NV=_C("GL_MAP_TESSELLATION_NV",0x86C2)
GL_MAX_MAP_TESSELLATION_NV=_C("GL_MAX_MAP_TESSELLATION_NV",0x86D6)
GL_MAX_RATIONAL_EVAL_ORDER_NV=_C("GL_MAX_RATIONAL_EVAL_ORDER_NV",0x86D7)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glEvalMapsNV(target,mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetMapAttribParameterfvNV(target,index,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetMapAttribParameterivNV(target,index,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean,ctypes.c_void_p)
def glGetMapControlPointsNV(target,index,type,ustride,vstride,packed,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMapParameterfvNV(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMapParameterivNV(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLint,_cs.GLboolean,ctypes.c_void_p)
def glMapControlPointsNV(target,index,type,ustride,vstride,uorder,vorder,packed,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMapParameterfvNV(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMapParameterivNV(target,pname,params):pass
