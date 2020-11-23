"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_video_capture"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_video_capture",error_checker=_errors._error_checker)
GL_FAILURE_NV=_C("GL_FAILURE_NV",0x9030)
GL_FIELD_LOWER_NV=_C("GL_FIELD_LOWER_NV",0x9023)
GL_FIELD_UPPER_NV=_C("GL_FIELD_UPPER_NV",0x9022)
GL_LAST_VIDEO_CAPTURE_STATUS_NV=_C("GL_LAST_VIDEO_CAPTURE_STATUS_NV",0x9027)
GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV=_C("GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV",0x9025)
GL_NUM_VIDEO_CAPTURE_STREAMS_NV=_C("GL_NUM_VIDEO_CAPTURE_STREAMS_NV",0x9024)
GL_PARTIAL_SUCCESS_NV=_C("GL_PARTIAL_SUCCESS_NV",0x902E)
GL_SUCCESS_NV=_C("GL_SUCCESS_NV",0x902F)
GL_VIDEO_BUFFER_BINDING_NV=_C("GL_VIDEO_BUFFER_BINDING_NV",0x9021)
GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV=_C("GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV",0x902D)
GL_VIDEO_BUFFER_NV=_C("GL_VIDEO_BUFFER_NV",0x9020)
GL_VIDEO_BUFFER_PITCH_NV=_C("GL_VIDEO_BUFFER_PITCH_NV",0x9028)
GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV=_C("GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV",0x903B)
GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV=_C("GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV",0x903A)
GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV=_C("GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV",0x9039)
GL_VIDEO_CAPTURE_FRAME_WIDTH_NV=_C("GL_VIDEO_CAPTURE_FRAME_WIDTH_NV",0x9038)
GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV=_C("GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV",0x903C)
GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV=_C("GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV",0x9026)
GL_VIDEO_COLOR_CONVERSION_MATRIX_NV=_C("GL_VIDEO_COLOR_CONVERSION_MATRIX_NV",0x9029)
GL_VIDEO_COLOR_CONVERSION_MAX_NV=_C("GL_VIDEO_COLOR_CONVERSION_MAX_NV",0x902A)
GL_VIDEO_COLOR_CONVERSION_MIN_NV=_C("GL_VIDEO_COLOR_CONVERSION_MIN_NV",0x902B)
GL_VIDEO_COLOR_CONVERSION_OFFSET_NV=_C("GL_VIDEO_COLOR_CONVERSION_OFFSET_NV",0x902C)
GL_YCBAYCR8A_4224_NV=_C("GL_YCBAYCR8A_4224_NV",0x9032)
GL_YCBYCR8_422_NV=_C("GL_YCBYCR8_422_NV",0x9031)
GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV=_C("GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV",0x9036)
GL_Z4Y12Z4CB12Z4CR12_444_NV=_C("GL_Z4Y12Z4CB12Z4CR12_444_NV",0x9037)
GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV=_C("GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV",0x9035)
GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV=_C("GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV",0x9034)
GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV=_C("GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV",0x9033)
@_f
@_p.types(None,_cs.GLuint)
def glBeginVideoCaptureNV(video_capture_slot):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLintptrARB)
def glBindVideoCaptureStreamBufferNV(video_capture_slot,stream,frame_region,offset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glBindVideoCaptureStreamTextureNV(video_capture_slot,stream,frame_region,target,texture):pass
@_f
@_p.types(None,_cs.GLuint)
def glEndVideoCaptureNV(video_capture_slot):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLdoubleArray)
def glGetVideoCaptureStreamdvNV(video_capture_slot,stream,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVideoCaptureStreamfvNV(video_capture_slot,stream,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVideoCaptureStreamivNV(video_capture_slot,stream,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVideoCaptureivNV(video_capture_slot,pname,params):pass
@_f
@_p.types(_cs.GLenum,_cs.GLuint,arrays.GLuintArray,arrays.GLuint64Array)
def glVideoCaptureNV(video_capture_slot,sequence_num,capture_time):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLdoubleArray)
def glVideoCaptureStreamParameterdvNV(video_capture_slot,stream,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glVideoCaptureStreamParameterfvNV(video_capture_slot,stream,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glVideoCaptureStreamParameterivNV(video_capture_slot,stream,pname,params):pass
