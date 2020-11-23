"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_NV_half_float"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_NV_half_float",error_checker=_errors._error_checker)
GL_HALF_FLOAT_NV=_C("GL_HALF_FLOAT_NV",0x140B)
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glColor3hNV(red,green,blue):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glColor3hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glColor4hNV(red,green,blue,alpha):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glColor4hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV)
def glFogCoordhNV(fog):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glFogCoordhvNV(fog):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLhalfNV)
def glMultiTexCoord1hNV(target,s):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLushortArray)
def glMultiTexCoord1hvNV(target,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLhalfNV,_cs.GLhalfNV)
def glMultiTexCoord2hNV(target,s,t):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLushortArray)
def glMultiTexCoord2hvNV(target,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glMultiTexCoord3hNV(target,s,t,r):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLushortArray)
def glMultiTexCoord3hvNV(target,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glMultiTexCoord4hNV(target,s,t,r,q):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLushortArray)
def glMultiTexCoord4hvNV(target,v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glNormal3hNV(nx,ny,nz):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glNormal3hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glSecondaryColor3hNV(red,green,blue):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glSecondaryColor3hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV)
def glTexCoord1hNV(s):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glTexCoord1hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV)
def glTexCoord2hNV(s,t):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glTexCoord2hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glTexCoord3hNV(s,t,r):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glTexCoord3hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glTexCoord4hNV(s,t,r,q):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glTexCoord4hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertex2hNV(x,y):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glVertex2hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertex3hNV(x,y,z):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glVertex3hvNV(v):pass
@_f
@_p.types(None,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertex4hNV(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glVertex4hvNV(v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLhalfNV)
def glVertexAttrib1hNV(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib1hvNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertexAttrib2hNV(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib2hvNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertexAttrib3hNV(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib3hvNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV,_cs.GLhalfNV)
def glVertexAttrib4hNV(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib4hvNV(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLushortArray)
def glVertexAttribs1hvNV(index,n,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLushortArray)
def glVertexAttribs2hvNV(index,n,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLushortArray)
def glVertexAttribs3hvNV(index,n,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLushortArray)
def glVertexAttribs4hvNV(index,n,v):pass
@_f
@_p.types(None,_cs.GLhalfNV)
def glVertexWeighthNV(weight):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glVertexWeighthvNV(weight):pass
