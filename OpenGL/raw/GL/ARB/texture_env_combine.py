"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_ARB_texture_env_combine"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_ARB_texture_env_combine",error_checker=_errors._error_checker)
GL_ADD_SIGNED_ARB=_C("GL_ADD_SIGNED_ARB",0x8574)
GL_COMBINE_ALPHA_ARB=_C("GL_COMBINE_ALPHA_ARB",0x8572)
GL_COMBINE_ARB=_C("GL_COMBINE_ARB",0x8570)
GL_COMBINE_RGB_ARB=_C("GL_COMBINE_RGB_ARB",0x8571)
GL_CONSTANT_ARB=_C("GL_CONSTANT_ARB",0x8576)
GL_INTERPOLATE_ARB=_C("GL_INTERPOLATE_ARB",0x8575)
GL_OPERAND0_ALPHA_ARB=_C("GL_OPERAND0_ALPHA_ARB",0x8598)
GL_OPERAND0_RGB_ARB=_C("GL_OPERAND0_RGB_ARB",0x8590)
GL_OPERAND1_ALPHA_ARB=_C("GL_OPERAND1_ALPHA_ARB",0x8599)
GL_OPERAND1_RGB_ARB=_C("GL_OPERAND1_RGB_ARB",0x8591)
GL_OPERAND2_ALPHA_ARB=_C("GL_OPERAND2_ALPHA_ARB",0x859A)
GL_OPERAND2_RGB_ARB=_C("GL_OPERAND2_RGB_ARB",0x8592)
GL_PREVIOUS_ARB=_C("GL_PREVIOUS_ARB",0x8578)
GL_PRIMARY_COLOR_ARB=_C("GL_PRIMARY_COLOR_ARB",0x8577)
GL_RGB_SCALE_ARB=_C("GL_RGB_SCALE_ARB",0x8573)
GL_SOURCE0_ALPHA_ARB=_C("GL_SOURCE0_ALPHA_ARB",0x8588)
GL_SOURCE0_RGB_ARB=_C("GL_SOURCE0_RGB_ARB",0x8580)
GL_SOURCE1_ALPHA_ARB=_C("GL_SOURCE1_ALPHA_ARB",0x8589)
GL_SOURCE1_RGB_ARB=_C("GL_SOURCE1_RGB_ARB",0x8581)
GL_SOURCE2_ALPHA_ARB=_C("GL_SOURCE2_ALPHA_ARB",0x858A)
GL_SOURCE2_RGB_ARB=_C("GL_SOURCE2_RGB_ARB",0x8582)
GL_SUBTRACT_ARB=_C("GL_SUBTRACT_ARB",0x84E7)

