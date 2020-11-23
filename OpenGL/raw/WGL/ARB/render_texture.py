"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "WGL_ARB_render_texture"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.WGL,"WGL_ARB_render_texture",error_checker=_errors._error_checker)
WGL_AUX0_ARB=_C("WGL_AUX0_ARB",0x2087)
WGL_AUX1_ARB=_C("WGL_AUX1_ARB",0x2088)
WGL_AUX2_ARB=_C("WGL_AUX2_ARB",0x2089)
WGL_AUX3_ARB=_C("WGL_AUX3_ARB",0x208A)
WGL_AUX4_ARB=_C("WGL_AUX4_ARB",0x208B)
WGL_AUX5_ARB=_C("WGL_AUX5_ARB",0x208C)
WGL_AUX6_ARB=_C("WGL_AUX6_ARB",0x208D)
WGL_AUX7_ARB=_C("WGL_AUX7_ARB",0x208E)
WGL_AUX8_ARB=_C("WGL_AUX8_ARB",0x208F)
WGL_AUX9_ARB=_C("WGL_AUX9_ARB",0x2090)
WGL_BACK_LEFT_ARB=_C("WGL_BACK_LEFT_ARB",0x2085)
WGL_BACK_RIGHT_ARB=_C("WGL_BACK_RIGHT_ARB",0x2086)
WGL_BIND_TO_TEXTURE_RGBA_ARB=_C("WGL_BIND_TO_TEXTURE_RGBA_ARB",0x2071)
WGL_BIND_TO_TEXTURE_RGB_ARB=_C("WGL_BIND_TO_TEXTURE_RGB_ARB",0x2070)
WGL_CUBE_MAP_FACE_ARB=_C("WGL_CUBE_MAP_FACE_ARB",0x207C)
WGL_FRONT_LEFT_ARB=_C("WGL_FRONT_LEFT_ARB",0x2083)
WGL_FRONT_RIGHT_ARB=_C("WGL_FRONT_RIGHT_ARB",0x2084)
WGL_MIPMAP_LEVEL_ARB=_C("WGL_MIPMAP_LEVEL_ARB",0x207B)
WGL_MIPMAP_TEXTURE_ARB=_C("WGL_MIPMAP_TEXTURE_ARB",0x2074)
WGL_NO_TEXTURE_ARB=_C("WGL_NO_TEXTURE_ARB",0x2077)
WGL_TEXTURE_1D_ARB=_C("WGL_TEXTURE_1D_ARB",0x2079)
WGL_TEXTURE_2D_ARB=_C("WGL_TEXTURE_2D_ARB",0x207A)
WGL_TEXTURE_CUBE_MAP_ARB=_C("WGL_TEXTURE_CUBE_MAP_ARB",0x2078)
WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB=_C("WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB",0x207E)
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB=_C("WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB",0x2080)
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB=_C("WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB",0x2082)
WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB=_C("WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB",0x207D)
WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB=_C("WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB",0x207F)
WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB=_C("WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB",0x2081)
WGL_TEXTURE_FORMAT_ARB=_C("WGL_TEXTURE_FORMAT_ARB",0x2072)
WGL_TEXTURE_RGBA_ARB=_C("WGL_TEXTURE_RGBA_ARB",0x2076)
WGL_TEXTURE_RGB_ARB=_C("WGL_TEXTURE_RGB_ARB",0x2075)
WGL_TEXTURE_TARGET_ARB=_C("WGL_TEXTURE_TARGET_ARB",0x2073)
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,_cs.c_int)
def wglBindTexImageARB(hPbuffer,iBuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,_cs.c_int)
def wglReleaseTexImageARB(hPbuffer,iBuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,ctypes.POINTER(_cs.c_int))
def wglSetPbufferAttribARB(hPbuffer,piAttribList):pass
