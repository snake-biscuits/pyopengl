"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_QCOM_texture_foveated"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_QCOM_texture_foveated",error_checker=_errors._error_checker)
GL_FOVEATION_ENABLE_BIT_QCOM=_C("GL_FOVEATION_ENABLE_BIT_QCOM",0x00000001)
GL_FOVEATION_SCALED_BIN_METHOD_BIT_QCOM=_C("GL_FOVEATION_SCALED_BIN_METHOD_BIT_QCOM",0x00000002)
GL_FRAMEBUFFER_INCOMPLETE_FOVEATION_QCOM=_C("GL_FRAMEBUFFER_INCOMPLETE_FOVEATION_QCOM",0x8BFF)
GL_TEXTURE_FOVEATED_FEATURE_BITS_QCOM=_C("GL_TEXTURE_FOVEATED_FEATURE_BITS_QCOM",0x8BFB)
GL_TEXTURE_FOVEATED_FEATURE_QUERY_QCOM=_C("GL_TEXTURE_FOVEATED_FEATURE_QUERY_QCOM",0x8BFD)
GL_TEXTURE_FOVEATED_MIN_PIXEL_DENSITY_QCOM=_C("GL_TEXTURE_FOVEATED_MIN_PIXEL_DENSITY_QCOM",0x8BFC)
GL_TEXTURE_FOVEATED_NUM_FOCAL_POINTS_QUERY_QCOM=_C("GL_TEXTURE_FOVEATED_NUM_FOCAL_POINTS_QUERY_QCOM",0x8BFE)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTextureFoveationParametersQCOM(texture,layer,focalPoint,focalX,focalY,gainX,gainY,foveaArea):pass
