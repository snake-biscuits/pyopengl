"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_texture_shader3"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_texture_shader3",error_checker=_errors._error_checker)
GL_DEPENDENT_HILO_TEXTURE_2D_NV=_C("GL_DEPENDENT_HILO_TEXTURE_2D_NV",0x8858)
GL_DEPENDENT_RGB_TEXTURE_3D_NV=_C("GL_DEPENDENT_RGB_TEXTURE_3D_NV",0x8859)
GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV=_C("GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV",0x885A)
GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV=_C("GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV",0x885D)
GL_DOT_PRODUCT_PASS_THROUGH_NV=_C("GL_DOT_PRODUCT_PASS_THROUGH_NV",0x885B)
GL_DOT_PRODUCT_TEXTURE_1D_NV=_C("GL_DOT_PRODUCT_TEXTURE_1D_NV",0x885C)
GL_FORCE_BLUE_TO_ONE_NV=_C("GL_FORCE_BLUE_TO_ONE_NV",0x8860)
GL_HILO8_NV=_C("GL_HILO8_NV",0x885E)
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV=_C("GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV",0x8856)
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV=_C("GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV",0x8857)
GL_OFFSET_HILO_TEXTURE_2D_NV=_C("GL_OFFSET_HILO_TEXTURE_2D_NV",0x8854)
GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV=_C("GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV",0x8855)
GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV=_C("GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV",0x8850)
GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV=_C("GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV",0x8851)
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV=_C("GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV",0x8852)
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV=_C("GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV",0x8853)
GL_SIGNED_HILO8_NV=_C("GL_SIGNED_HILO8_NV",0x885F)

