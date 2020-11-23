"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_AMD_framebuffer_multisample_advanced"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_AMD_framebuffer_multisample_advanced",error_checker=_errors._error_checker)
GL_MAX_COLOR_FRAMEBUFFER_SAMPLES_AMD=_C("GL_MAX_COLOR_FRAMEBUFFER_SAMPLES_AMD",0x91B3)
GL_MAX_COLOR_FRAMEBUFFER_STORAGE_SAMPLES_AMD=_C("GL_MAX_COLOR_FRAMEBUFFER_STORAGE_SAMPLES_AMD",0x91B4)
GL_MAX_DEPTH_STENCIL_FRAMEBUFFER_SAMPLES_AMD=_C("GL_MAX_DEPTH_STENCIL_FRAMEBUFFER_SAMPLES_AMD",0x91B5)
GL_NUM_SUPPORTED_MULTISAMPLE_MODES_AMD=_C("GL_NUM_SUPPORTED_MULTISAMPLE_MODES_AMD",0x91B6)
GL_RENDERBUFFER_STORAGE_SAMPLES_AMD=_C("GL_RENDERBUFFER_STORAGE_SAMPLES_AMD",0x91B2)
GL_SUPPORTED_MULTISAMPLE_MODES_AMD=_C("GL_SUPPORTED_MULTISAMPLE_MODES_AMD",0x91B7)
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorageMultisampleAdvancedAMD(renderbuffer,samples,storageSamples,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisampleAdvancedAMD(target,samples,storageSamples,internalformat,width,height):pass
