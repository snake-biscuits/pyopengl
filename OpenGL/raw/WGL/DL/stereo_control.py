"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "WGL_DL_stereo_control"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.WGL,"WGL_DL_stereo_control",error_checker=_errors._error_checker)
WGL_STEREO_EMITTER_DISABLE_3DL=_C("WGL_STEREO_EMITTER_DISABLE_3DL",0x2056)
WGL_STEREO_EMITTER_ENABLE_3DL=_C("WGL_STEREO_EMITTER_ENABLE_3DL",0x2055)
WGL_STEREO_POLARITY_INVERT_3DL=_C("WGL_STEREO_POLARITY_INVERT_3DL",0x2058)
WGL_STEREO_POLARITY_NORMAL_3DL=_C("WGL_STEREO_POLARITY_NORMAL_3DL",0x2057)
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.UINT)
def wglSetStereoEmitterState3DL(hDC,uState):pass
