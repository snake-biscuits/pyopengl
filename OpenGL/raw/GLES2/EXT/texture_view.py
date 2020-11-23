"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_EXT_texture_view"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_EXT_texture_view",error_checker=_errors._error_checker)
GL_TEXTURE_IMMUTABLE_LEVELS=_C("GL_TEXTURE_IMMUTABLE_LEVELS",0x82DF)
GL_TEXTURE_VIEW_MIN_LAYER_EXT=_C("GL_TEXTURE_VIEW_MIN_LAYER_EXT",0x82DD)
GL_TEXTURE_VIEW_MIN_LEVEL_EXT=_C("GL_TEXTURE_VIEW_MIN_LEVEL_EXT",0x82DB)
GL_TEXTURE_VIEW_NUM_LAYERS_EXT=_C("GL_TEXTURE_VIEW_NUM_LAYERS_EXT",0x82DE)
GL_TEXTURE_VIEW_NUM_LEVELS_EXT=_C("GL_TEXTURE_VIEW_NUM_LEVELS_EXT",0x82DC)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glTextureViewEXT(texture,target,origtexture,internalformat,minlevel,numlevels,minlayer,numlayers):pass
