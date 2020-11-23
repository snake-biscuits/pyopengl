"""OpenGL extension NV.shadow_samplers_cube

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.shadow_samplers_cube to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension expands the shadow map capability described in
	EXT_shadow_samplers to include support for shadow samplers of cube
	map textures.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/shadow_samplers_cube.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.shadow_samplers_cube import *
from OpenGL.raw.GLES2.NV.shadow_samplers_cube import _EXTENSION_NAME

def glInitShadowSamplersCubeNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION