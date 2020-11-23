"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_NV_shading_rate_image"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_NV_shading_rate_image",error_checker=_errors._error_checker)
GL_MAX_COARSE_FRAGMENT_SAMPLES_NV=_C("GL_MAX_COARSE_FRAGMENT_SAMPLES_NV",0x955F)
GL_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV=_C("GL_SHADING_RATE_16_INVOCATIONS_PER_PIXEL_NV",0x956F)
GL_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_1X2_PIXELS_NV",0x9566)
GL_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_2X1_PIXELS_NV",0x9567)
GL_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_2X2_PIXELS_NV",0x9568)
GL_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_2X4_PIXELS_NV",0x9569)
GL_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_4X2_PIXELS_NV",0x956A)
GL_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_4X4_PIXELS_NV",0x956B)
GL_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV=_C("GL_SHADING_RATE_1_INVOCATION_PER_PIXEL_NV",0x9565)
GL_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV=_C("GL_SHADING_RATE_2_INVOCATIONS_PER_PIXEL_NV",0x956C)
GL_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV=_C("GL_SHADING_RATE_4_INVOCATIONS_PER_PIXEL_NV",0x956D)
GL_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV=_C("GL_SHADING_RATE_8_INVOCATIONS_PER_PIXEL_NV",0x956E)
GL_SHADING_RATE_IMAGE_BINDING_NV=_C("GL_SHADING_RATE_IMAGE_BINDING_NV",0x955B)
GL_SHADING_RATE_IMAGE_NV=_C("GL_SHADING_RATE_IMAGE_NV",0x9563)
GL_SHADING_RATE_IMAGE_PALETTE_SIZE_NV=_C("GL_SHADING_RATE_IMAGE_PALETTE_SIZE_NV",0x955E)
GL_SHADING_RATE_IMAGE_TEXEL_HEIGHT_NV=_C("GL_SHADING_RATE_IMAGE_TEXEL_HEIGHT_NV",0x955D)
GL_SHADING_RATE_IMAGE_TEXEL_WIDTH_NV=_C("GL_SHADING_RATE_IMAGE_TEXEL_WIDTH_NV",0x955C)
GL_SHADING_RATE_NO_INVOCATIONS_NV=_C("GL_SHADING_RATE_NO_INVOCATIONS_NV",0x9564)
GL_SHADING_RATE_SAMPLE_ORDER_DEFAULT_NV=_C("GL_SHADING_RATE_SAMPLE_ORDER_DEFAULT_NV",0x95AE)
GL_SHADING_RATE_SAMPLE_ORDER_PIXEL_MAJOR_NV=_C("GL_SHADING_RATE_SAMPLE_ORDER_PIXEL_MAJOR_NV",0x95AF)
GL_SHADING_RATE_SAMPLE_ORDER_SAMPLE_MAJOR_NV=_C("GL_SHADING_RATE_SAMPLE_ORDER_SAMPLE_MAJOR_NV",0x95B0)
@_f
@_p.types(None,_cs.GLuint)
def glBindShadingRateImageNV(texture):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLuintArray)
def glGetShadingRateImagePaletteNV(viewport,entry,rate):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,arrays.GLintArray)
def glGetShadingRateSampleLocationivNV(rate,samples,index,location):pass
@_f
@_p.types(None,_cs.GLboolean)
def glShadingRateImageBarrierNV(synchronize):pass
@_f
@_p.types(None,_cs.GLboolean)
def glShadingRateImageBarrierNV(synchronize):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glShadingRateImagePaletteNV(viewport,first,count,rates):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glShadingRateSampleOrderCustomNV(rate,samples,locations):pass
@_f
@_p.types(None,_cs.GLenum)
def glShadingRateSampleOrderNV(order):pass
