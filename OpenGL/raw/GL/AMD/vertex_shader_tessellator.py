"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_AMD_vertex_shader_tessellator"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_AMD_vertex_shader_tessellator",error_checker=_errors._error_checker)
GL_CONTINUOUS_AMD=_C("GL_CONTINUOUS_AMD",0x9007)
GL_DISCRETE_AMD=_C("GL_DISCRETE_AMD",0x9006)
GL_INT_SAMPLER_BUFFER_AMD=_C("GL_INT_SAMPLER_BUFFER_AMD",0x9002)
GL_SAMPLER_BUFFER_AMD=_C("GL_SAMPLER_BUFFER_AMD",0x9001)
GL_TESSELLATION_FACTOR_AMD=_C("GL_TESSELLATION_FACTOR_AMD",0x9005)
GL_TESSELLATION_MODE_AMD=_C("GL_TESSELLATION_MODE_AMD",0x9004)
GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD=_C("GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD",0x9003)
@_f
@_p.types(None,_cs.GLfloat)
def glTessellationFactorAMD(factor):pass
@_f
@_p.types(None,_cs.GLenum)
def glTessellationModeAMD(mode):pass
