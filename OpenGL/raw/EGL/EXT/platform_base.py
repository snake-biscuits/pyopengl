"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "EGL_EXT_platform_base"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.EGL,"EGL_EXT_platform_base",error_checker=_errors._error_checker)

@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,ctypes.c_void_p,arrays.GLintArray)
def eglCreatePlatformPixmapSurfaceEXT(dpy,config,native_pixmap,attrib_list):pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,ctypes.c_void_p,arrays.GLintArray)
def eglCreatePlatformWindowSurfaceEXT(dpy,config,native_window,attrib_list):pass
@_f
@_p.types(_cs.EGLDisplay,_cs.EGLenum,ctypes.c_void_p,arrays.GLintArray)
def eglGetPlatformDisplayEXT(platform,native_display,attrib_list):pass
