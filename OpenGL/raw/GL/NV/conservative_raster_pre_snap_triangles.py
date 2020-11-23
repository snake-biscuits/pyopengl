"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_conservative_raster_pre_snap_triangles"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_conservative_raster_pre_snap_triangles",error_checker=_errors._error_checker)
GL_CONSERVATIVE_RASTER_MODE_NV=_C("GL_CONSERVATIVE_RASTER_MODE_NV",0x954D)
GL_CONSERVATIVE_RASTER_MODE_NV=_C("GL_CONSERVATIVE_RASTER_MODE_NV",0x954D)
GL_CONSERVATIVE_RASTER_MODE_POST_SNAP_NV=_C("GL_CONSERVATIVE_RASTER_MODE_POST_SNAP_NV",0x954E)
GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_TRIANGLES_NV=_C("GL_CONSERVATIVE_RASTER_MODE_PRE_SNAP_TRIANGLES_NV",0x954F)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glConservativeRasterParameteriNV(pname,param):pass
