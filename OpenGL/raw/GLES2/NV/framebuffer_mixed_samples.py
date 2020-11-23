"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_NV_framebuffer_mixed_samples"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_NV_framebuffer_mixed_samples",error_checker=_errors._error_checker)
GL_COLOR_SAMPLES_NV=_C("GL_COLOR_SAMPLES_NV",0x8E20)
GL_COVERAGE_MODULATION_NV=_C("GL_COVERAGE_MODULATION_NV",0x9332)
GL_COVERAGE_MODULATION_TABLE_NV=_C("GL_COVERAGE_MODULATION_TABLE_NV",0x9331)
GL_COVERAGE_MODULATION_TABLE_SIZE_NV=_C("GL_COVERAGE_MODULATION_TABLE_SIZE_NV",0x9333)
GL_DEPTH_SAMPLES_NV=_C("GL_DEPTH_SAMPLES_NV",0x932D)
GL_EFFECTIVE_RASTER_SAMPLES_EXT=_C("GL_EFFECTIVE_RASTER_SAMPLES_EXT",0x932C)
GL_MAX_RASTER_SAMPLES_EXT=_C("GL_MAX_RASTER_SAMPLES_EXT",0x9329)
GL_MIXED_DEPTH_SAMPLES_SUPPORTED_NV=_C("GL_MIXED_DEPTH_SAMPLES_SUPPORTED_NV",0x932F)
GL_MIXED_STENCIL_SAMPLES_SUPPORTED_NV=_C("GL_MIXED_STENCIL_SAMPLES_SUPPORTED_NV",0x9330)
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT=_C("GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT",0x932B)
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT=_C("GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT",0x932A)
GL_RASTER_MULTISAMPLE_EXT=_C("GL_RASTER_MULTISAMPLE_EXT",0x9327)
GL_RASTER_SAMPLES_EXT=_C("GL_RASTER_SAMPLES_EXT",0x9328)
GL_STENCIL_SAMPLES_NV=_C("GL_STENCIL_SAMPLES_NV",0x932E)
@_f
@_p.types(None,_cs.GLenum)
def glCoverageModulationNV(components):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLfloatArray)
def glCoverageModulationTableNV(n,v):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLfloatArray)
def glGetCoverageModulationTableNV(bufsize,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean)
def glRasterSamplesEXT(samples,fixedsamplelocations):pass
