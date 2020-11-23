"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "EGL_MESA_image_dma_buf_export"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.EGL,"EGL_MESA_image_dma_buf_export",error_checker=_errors._error_checker)

@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLImageKHR,ctypes.POINTER(_cs.c_int),arrays.GLintArray,arrays.GLintArray)
def eglExportDMABUFImageMESA(dpy,image,fds,strides,offsets):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLImageKHR,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.c_int),arrays.GLuint64Array)
def eglExportDMABUFImageQueryMESA(dpy,image,fourcc,num_planes,modifiers):pass
