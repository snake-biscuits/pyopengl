"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GL_PGI_vertex_hints"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GL,"GL_PGI_vertex_hints",error_checker=_errors._error_checker)
GL_COLOR3_BIT_PGI=_C("GL_COLOR3_BIT_PGI",0x00010000)
GL_COLOR4_BIT_PGI=_C("GL_COLOR4_BIT_PGI",0x00020000)
GL_EDGEFLAG_BIT_PGI=_C("GL_EDGEFLAG_BIT_PGI",0x00040000)
GL_INDEX_BIT_PGI=_C("GL_INDEX_BIT_PGI",0x00080000)
GL_MATERIAL_SIDE_HINT_PGI=_C("GL_MATERIAL_SIDE_HINT_PGI",0x1A22C)
GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI=_C("GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI",0x00200000)
GL_MAT_AMBIENT_BIT_PGI=_C("GL_MAT_AMBIENT_BIT_PGI",0x00100000)
GL_MAT_COLOR_INDEXES_BIT_PGI=_C("GL_MAT_COLOR_INDEXES_BIT_PGI",0x01000000)
GL_MAT_DIFFUSE_BIT_PGI=_C("GL_MAT_DIFFUSE_BIT_PGI",0x00400000)
GL_MAT_EMISSION_BIT_PGI=_C("GL_MAT_EMISSION_BIT_PGI",0x00800000)
GL_MAT_SHININESS_BIT_PGI=_C("GL_MAT_SHININESS_BIT_PGI",0x02000000)
GL_MAT_SPECULAR_BIT_PGI=_C("GL_MAT_SPECULAR_BIT_PGI",0x04000000)
GL_MAX_VERTEX_HINT_PGI=_C("GL_MAX_VERTEX_HINT_PGI",0x1A22D)
GL_NORMAL_BIT_PGI=_C("GL_NORMAL_BIT_PGI",0x08000000)
GL_TEXCOORD1_BIT_PGI=_C("GL_TEXCOORD1_BIT_PGI",0x10000000)
GL_TEXCOORD2_BIT_PGI=_C("GL_TEXCOORD2_BIT_PGI",0x20000000)
GL_TEXCOORD3_BIT_PGI=_C("GL_TEXCOORD3_BIT_PGI",0x40000000)
GL_TEXCOORD4_BIT_PGI=_C("GL_TEXCOORD4_BIT_PGI",0x80000000)
GL_VERTEX23_BIT_PGI=_C("GL_VERTEX23_BIT_PGI",0x00000004)
GL_VERTEX4_BIT_PGI=_C("GL_VERTEX4_BIT_PGI",0x00000008)
GL_VERTEX_CONSISTENT_HINT_PGI=_C("GL_VERTEX_CONSISTENT_HINT_PGI",0x1A22B)
GL_VERTEX_DATA_HINT_PGI=_C("GL_VERTEX_DATA_HINT_PGI",0x1A22A)

