"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES1_APPLE_sync"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES1,"GLES1_APPLE_sync",error_checker=_errors._error_checker)
GL_ALREADY_SIGNALED_APPLE=_C("GL_ALREADY_SIGNALED_APPLE",0x911A)
GL_CONDITION_SATISFIED_APPLE=_C("GL_CONDITION_SATISFIED_APPLE",0x911C)
GL_MAX_SERVER_WAIT_TIMEOUT_APPLE=_C("GL_MAX_SERVER_WAIT_TIMEOUT_APPLE",0x9111)
GL_OBJECT_TYPE_APPLE=_C("GL_OBJECT_TYPE_APPLE",0x9112)
GL_SIGNALED_APPLE=_C("GL_SIGNALED_APPLE",0x9119)
GL_SYNC_CONDITION_APPLE=_C("GL_SYNC_CONDITION_APPLE",0x9113)
GL_SYNC_FENCE_APPLE=_C("GL_SYNC_FENCE_APPLE",0x9116)
GL_SYNC_FLAGS_APPLE=_C("GL_SYNC_FLAGS_APPLE",0x9115)
GL_SYNC_FLUSH_COMMANDS_BIT_APPLE=_C("GL_SYNC_FLUSH_COMMANDS_BIT_APPLE",0x00000001)
GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE=_C("GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE",0x9117)
GL_SYNC_OBJECT_APPLE=_C("GL_SYNC_OBJECT_APPLE",0x8A53)
GL_SYNC_STATUS_APPLE=_C("GL_SYNC_STATUS_APPLE",0x9114)
GL_TIMEOUT_EXPIRED_APPLE=_C("GL_TIMEOUT_EXPIRED_APPLE",0x911B)
GL_TIMEOUT_IGNORED_APPLE=_C("GL_TIMEOUT_IGNORED_APPLE",0xFFFFFFFFFFFFFFFF)
GL_UNSIGNALED_APPLE=_C("GL_UNSIGNALED_APPLE",0x9118)
GL_WAIT_FAILED_APPLE=_C("GL_WAIT_FAILED_APPLE",0x911D)
@_f
@_p.types(_cs.GLenum,_cs.GLsync,_cs.GLbitfield,_cs.GLuint64)
def glClientWaitSyncAPPLE(sync,flags,timeout):pass
@_f
@_p.types(None,_cs.GLsync)
def glDeleteSyncAPPLE(sync):pass
@_f
@_p.types(_cs.GLsync,_cs.GLenum,_cs.GLbitfield)
def glFenceSyncAPPLE(condition,flags):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLint64Array)
def glGetInteger64vAPPLE(pname,params):pass
@_f
@_p.types(None,_cs.GLsync,_cs.GLenum,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray)
def glGetSyncivAPPLE(sync,pname,bufSize,length,values):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLsync)
def glIsSyncAPPLE(sync):pass
@_f
@_p.types(None,_cs.GLsync,_cs.GLbitfield,_cs.GLuint64)
def glWaitSyncAPPLE(sync,flags,timeout):pass
