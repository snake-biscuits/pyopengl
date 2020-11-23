"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ATI_texture_float"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ATI_texture_float",error_checker=_errors._error_checker)
GL_ALPHA_FLOAT16_ATI=_C("GL_ALPHA_FLOAT16_ATI",0x881C)
GL_ALPHA_FLOAT32_ATI=_C("GL_ALPHA_FLOAT32_ATI",0x8816)
GL_INTENSITY_FLOAT16_ATI=_C("GL_INTENSITY_FLOAT16_ATI",0x881D)
GL_INTENSITY_FLOAT32_ATI=_C("GL_INTENSITY_FLOAT32_ATI",0x8817)
GL_LUMINANCE_ALPHA_FLOAT16_ATI=_C("GL_LUMINANCE_ALPHA_FLOAT16_ATI",0x881F)
GL_LUMINANCE_ALPHA_FLOAT32_ATI=_C("GL_LUMINANCE_ALPHA_FLOAT32_ATI",0x8819)
GL_LUMINANCE_FLOAT16_ATI=_C("GL_LUMINANCE_FLOAT16_ATI",0x881E)
GL_LUMINANCE_FLOAT32_ATI=_C("GL_LUMINANCE_FLOAT32_ATI",0x8818)
GL_RGBA_FLOAT16_ATI=_C("GL_RGBA_FLOAT16_ATI",0x881A)
GL_RGBA_FLOAT32_ATI=_C("GL_RGBA_FLOAT32_ATI",0x8814)
GL_RGB_FLOAT16_ATI=_C("GL_RGB_FLOAT16_ATI",0x881B)
GL_RGB_FLOAT32_ATI=_C("GL_RGB_FLOAT32_ATI",0x8815)

