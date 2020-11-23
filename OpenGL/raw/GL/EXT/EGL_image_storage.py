"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_EXT_EGL_image_storage"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_EXT_EGL_image_storage",error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,_cs.GLeglImageOES,arrays.GLintArray)
def glEGLImageTargetTexStorageEXT(target,image,attrib_list):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLeglImageOES,arrays.GLintArray)
def glEGLImageTargetTextureStorageEXT(texture,image,attrib_list):pass
