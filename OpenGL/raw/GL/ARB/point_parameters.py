"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_point_parameters"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_point_parameters",error_checker=_errors._error_checker)
GL_POINT_DISTANCE_ATTENUATION_ARB=_C("GL_POINT_DISTANCE_ATTENUATION_ARB",0x8129)
GL_POINT_FADE_THRESHOLD_SIZE_ARB=_C("GL_POINT_FADE_THRESHOLD_SIZE_ARB",0x8128)
GL_POINT_SIZE_MAX_ARB=_C("GL_POINT_SIZE_MAX_ARB",0x8127)
GL_POINT_SIZE_MIN_ARB=_C("GL_POINT_SIZE_MIN_ARB",0x8126)
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPointParameterfARB(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPointParameterfvARB(pname,params):pass
