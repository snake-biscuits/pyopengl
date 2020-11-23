"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_EXT_geometry_shader"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_EXT_geometry_shader",error_checker=_errors._error_checker)
GL_FIRST_VERTEX_CONVENTION_EXT=_C("GL_FIRST_VERTEX_CONVENTION_EXT",0x8E4D)
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT=_C("GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT",0x8DA7)
GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT=_C("GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT",0x9312)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT=_C("GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT",0x8DA8)
GL_GEOMETRY_LINKED_INPUT_TYPE_EXT=_C("GL_GEOMETRY_LINKED_INPUT_TYPE_EXT",0x8917)
GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT=_C("GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT",0x8918)
GL_GEOMETRY_LINKED_VERTICES_OUT_EXT=_C("GL_GEOMETRY_LINKED_VERTICES_OUT_EXT",0x8916)
GL_GEOMETRY_SHADER_BIT_EXT=_C("GL_GEOMETRY_SHADER_BIT_EXT",0x00000004)
GL_GEOMETRY_SHADER_EXT=_C("GL_GEOMETRY_SHADER_EXT",0x8DD9)
GL_GEOMETRY_SHADER_INVOCATIONS_EXT=_C("GL_GEOMETRY_SHADER_INVOCATIONS_EXT",0x887F)
GL_LAST_VERTEX_CONVENTION_EXT=_C("GL_LAST_VERTEX_CONVENTION_EXT",0x8E4E)
GL_LAYER_PROVOKING_VERTEX_EXT=_C("GL_LAYER_PROVOKING_VERTEX_EXT",0x825E)
GL_LINES_ADJACENCY_EXT=_C("GL_LINES_ADJACENCY_EXT",0x000A)
GL_LINE_STRIP_ADJACENCY_EXT=_C("GL_LINE_STRIP_ADJACENCY_EXT",0x000B)
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT=_C("GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT",0x8A32)
GL_MAX_FRAMEBUFFER_LAYERS_EXT=_C("GL_MAX_FRAMEBUFFER_LAYERS_EXT",0x9317)
GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT=_C("GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT",0x92D5)
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT=_C("GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT",0x92CF)
GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT=_C("GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT",0x90CD)
GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT=_C("GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT",0x9123)
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT=_C("GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT",0x9124)
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT=_C("GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT",0x8DE0)
GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT=_C("GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT",0x8E5A)
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT=_C("GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT",0x90D7)
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT=_C("GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT",0x8C29)
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT=_C("GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT",0x8DE1)
GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT=_C("GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT",0x8A2C)
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT=_C("GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT",0x8DDF)
GL_PRIMITIVES_GENERATED_EXT=_C("GL_PRIMITIVES_GENERATED_EXT",0x8C87)
GL_REFERENCED_BY_GEOMETRY_SHADER_EXT=_C("GL_REFERENCED_BY_GEOMETRY_SHADER_EXT",0x9309)
GL_TRIANGLES_ADJACENCY_EXT=_C("GL_TRIANGLES_ADJACENCY_EXT",0x000C)
GL_TRIANGLE_STRIP_ADJACENCY_EXT=_C("GL_TRIANGLE_STRIP_ADJACENCY_EXT",0x000D)
GL_UNDEFINED_VERTEX_EXT=_C("GL_UNDEFINED_VERTEX_EXT",0x8260)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTextureEXT(target,attachment,texture,level):pass
