"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_IMG_multisampled_render_to_texture"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_IMG_multisampled_render_to_texture",error_checker=_errors._error_checker)
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG=_C("GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG",0x9134)
GL_MAX_SAMPLES_IMG=_C("GL_MAX_SAMPLES_IMG",0x9135)
GL_RENDERBUFFER_SAMPLES_IMG=_C("GL_RENDERBUFFER_SAMPLES_IMG",0x9133)
GL_TEXTURE_SAMPLES_IMG=_C("GL_TEXTURE_SAMPLES_IMG",0x9136)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLsizei)
def glFramebufferTexture2DMultisampleIMG(target,attachment,textarget,texture,level,samples):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisampleIMG(target,samples,internalformat,width,height):pass
