"""OpenGL extension NV.shader_subgroup_partitioned

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shader_subgroup_partitioned to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables support for the NV_shader_subgroup_partitioned
	shading language extension in OpenGL and OpenGL ES.
	
	This extension adds a new SUBGROUP_FEATURE_PARTITIONED_BIT_NV feature bit
	that is returned by queryies for SUBGROUP_SUPPORTED_FEATURES_KHR.
	
	In OpenGL implementations supporting SPIR-V, this extension enables
	support for the SPV_NV_shader_subgroup_partitioned extension.
	
	In OpenGL ES implementations, this extension does NOT add support for
	SPIR-V or for any of the built-in shading language functions (8.18)
	that have genDType (double) prototypes.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/shader_subgroup_partitioned.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.shader_subgroup_partitioned import *
from OpenGL.raw.GL.NV.shader_subgroup_partitioned import _EXTENSION_NAME

def glInitShaderSubgroupPartitionedNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION