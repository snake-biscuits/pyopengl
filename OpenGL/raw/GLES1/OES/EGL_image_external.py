"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_OES_EGL_image_external"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_OES_EGL_image_external",error_checker=_errors._error_checker)
GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES=_C("GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES",0x8D68)
GL_SAMPLER_EXTERNAL_OES=_C("GL_SAMPLER_EXTERNAL_OES",0x8D66)
GL_TEXTURE_BINDING_EXTERNAL_OES=_C("GL_TEXTURE_BINDING_EXTERNAL_OES",0x8D67)
GL_TEXTURE_EXTERNAL_OES=_C("GL_TEXTURE_EXTERNAL_OES",0x8D65)

