"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLES2_NV_mesh_shader"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLES2,"GLES2_NV_mesh_shader",error_checker=_errors._error_checker)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_MESH_SHADER_NV=_C("GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_MESH_SHADER_NV",0x959E)
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TASK_SHADER_NV=_C("GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TASK_SHADER_NV",0x959F)
GL_MAX_COMBINED_MESH_UNIFORM_COMPONENTS_NV=_C("GL_MAX_COMBINED_MESH_UNIFORM_COMPONENTS_NV",0x8E67)
GL_MAX_COMBINED_TASK_UNIFORM_COMPONENTS_NV=_C("GL_MAX_COMBINED_TASK_UNIFORM_COMPONENTS_NV",0x8E6F)
GL_MAX_DRAW_MESH_TASKS_COUNT_NV=_C("GL_MAX_DRAW_MESH_TASKS_COUNT_NV",0x953D)
GL_MAX_MESH_ATOMIC_COUNTERS_NV=_C("GL_MAX_MESH_ATOMIC_COUNTERS_NV",0x8E65)
GL_MAX_MESH_ATOMIC_COUNTER_BUFFERS_NV=_C("GL_MAX_MESH_ATOMIC_COUNTER_BUFFERS_NV",0x8E64)
GL_MAX_MESH_IMAGE_UNIFORMS_NV=_C("GL_MAX_MESH_IMAGE_UNIFORMS_NV",0x8E62)
GL_MAX_MESH_OUTPUT_PRIMITIVES_NV=_C("GL_MAX_MESH_OUTPUT_PRIMITIVES_NV",0x9539)
GL_MAX_MESH_OUTPUT_VERTICES_NV=_C("GL_MAX_MESH_OUTPUT_VERTICES_NV",0x9538)
GL_MAX_MESH_SHADER_STORAGE_BLOCKS_NV=_C("GL_MAX_MESH_SHADER_STORAGE_BLOCKS_NV",0x8E66)
GL_MAX_MESH_TEXTURE_IMAGE_UNITS_NV=_C("GL_MAX_MESH_TEXTURE_IMAGE_UNITS_NV",0x8E61)
GL_MAX_MESH_TOTAL_MEMORY_SIZE_NV=_C("GL_MAX_MESH_TOTAL_MEMORY_SIZE_NV",0x9536)
GL_MAX_MESH_UNIFORM_BLOCKS_NV=_C("GL_MAX_MESH_UNIFORM_BLOCKS_NV",0x8E60)
GL_MAX_MESH_UNIFORM_COMPONENTS_NV=_C("GL_MAX_MESH_UNIFORM_COMPONENTS_NV",0x8E63)
GL_MAX_MESH_VIEWS_NV=_C("GL_MAX_MESH_VIEWS_NV",0x9557)
GL_MAX_MESH_WORK_GROUP_INVOCATIONS_NV=_C("GL_MAX_MESH_WORK_GROUP_INVOCATIONS_NV",0x95A2)
GL_MAX_MESH_WORK_GROUP_SIZE_NV=_C("GL_MAX_MESH_WORK_GROUP_SIZE_NV",0x953B)
GL_MAX_TASK_ATOMIC_COUNTERS_NV=_C("GL_MAX_TASK_ATOMIC_COUNTERS_NV",0x8E6D)
GL_MAX_TASK_ATOMIC_COUNTER_BUFFERS_NV=_C("GL_MAX_TASK_ATOMIC_COUNTER_BUFFERS_NV",0x8E6C)
GL_MAX_TASK_IMAGE_UNIFORMS_NV=_C("GL_MAX_TASK_IMAGE_UNIFORMS_NV",0x8E6A)
GL_MAX_TASK_OUTPUT_COUNT_NV=_C("GL_MAX_TASK_OUTPUT_COUNT_NV",0x953A)
GL_MAX_TASK_SHADER_STORAGE_BLOCKS_NV=_C("GL_MAX_TASK_SHADER_STORAGE_BLOCKS_NV",0x8E6E)
GL_MAX_TASK_TEXTURE_IMAGE_UNITS_NV=_C("GL_MAX_TASK_TEXTURE_IMAGE_UNITS_NV",0x8E69)
GL_MAX_TASK_TOTAL_MEMORY_SIZE_NV=_C("GL_MAX_TASK_TOTAL_MEMORY_SIZE_NV",0x9537)
GL_MAX_TASK_UNIFORM_BLOCKS_NV=_C("GL_MAX_TASK_UNIFORM_BLOCKS_NV",0x8E68)
GL_MAX_TASK_UNIFORM_COMPONENTS_NV=_C("GL_MAX_TASK_UNIFORM_COMPONENTS_NV",0x8E6B)
GL_MAX_TASK_WORK_GROUP_INVOCATIONS_NV=_C("GL_MAX_TASK_WORK_GROUP_INVOCATIONS_NV",0x95A3)
GL_MAX_TASK_WORK_GROUP_SIZE_NV=_C("GL_MAX_TASK_WORK_GROUP_SIZE_NV",0x953C)
GL_MESH_OUTPUT_PER_PRIMITIVE_GRANULARITY_NV=_C("GL_MESH_OUTPUT_PER_PRIMITIVE_GRANULARITY_NV",0x9543)
GL_MESH_OUTPUT_PER_VERTEX_GRANULARITY_NV=_C("GL_MESH_OUTPUT_PER_VERTEX_GRANULARITY_NV",0x92DF)
GL_MESH_OUTPUT_TYPE_NV=_C("GL_MESH_OUTPUT_TYPE_NV",0x957B)
GL_MESH_PRIMITIVES_OUT_NV=_C("GL_MESH_PRIMITIVES_OUT_NV",0x957A)
GL_MESH_SHADER_BIT_NV=_C("GL_MESH_SHADER_BIT_NV",0x00000040)
GL_MESH_SHADER_NV=_C("GL_MESH_SHADER_NV",0x9559)
GL_MESH_SUBROUTINE_NV=_C("GL_MESH_SUBROUTINE_NV",0x957C)
GL_MESH_SUBROUTINE_UNIFORM_NV=_C("GL_MESH_SUBROUTINE_UNIFORM_NV",0x957E)
GL_MESH_VERTICES_OUT_NV=_C("GL_MESH_VERTICES_OUT_NV",0x9579)
GL_MESH_WORK_GROUP_SIZE_NV=_C("GL_MESH_WORK_GROUP_SIZE_NV",0x953E)
GL_REFERENCED_BY_MESH_SHADER_NV=_C("GL_REFERENCED_BY_MESH_SHADER_NV",0x95A0)
GL_REFERENCED_BY_TASK_SHADER_NV=_C("GL_REFERENCED_BY_TASK_SHADER_NV",0x95A1)
GL_TASK_SHADER_BIT_NV=_C("GL_TASK_SHADER_BIT_NV",0x00000080)
GL_TASK_SHADER_NV=_C("GL_TASK_SHADER_NV",0x955A)
GL_TASK_SUBROUTINE_NV=_C("GL_TASK_SUBROUTINE_NV",0x957D)
GL_TASK_SUBROUTINE_UNIFORM_NV=_C("GL_TASK_SUBROUTINE_UNIFORM_NV",0x957F)
GL_TASK_WORK_GROUP_SIZE_NV=_C("GL_TASK_WORK_GROUP_SIZE_NV",0x953F)
GL_UNIFORM_BLOCK_REFERENCED_BY_MESH_SHADER_NV=_C("GL_UNIFORM_BLOCK_REFERENCED_BY_MESH_SHADER_NV",0x959C)
GL_UNIFORM_BLOCK_REFERENCED_BY_TASK_SHADER_NV=_C("GL_UNIFORM_BLOCK_REFERENCED_BY_TASK_SHADER_NV",0x959D)
@_f
@_p.types(None,_cs.GLintptr)
def glDrawMeshTasksIndirectNV(indirect):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glDrawMeshTasksNV(first,count):pass
@_f
@_p.types(None,_cs.GLintptr,_cs.GLintptr,_cs.GLsizei,_cs.GLsizei)
def glMultiDrawMeshTasksIndirectCountNV(indirect,drawcount,maxdrawcount,stride):pass
@_f
@_p.types(None,_cs.GLintptr,_cs.GLsizei,_cs.GLsizei)
def glMultiDrawMeshTasksIndirectNV(indirect,drawcount,stride):pass
