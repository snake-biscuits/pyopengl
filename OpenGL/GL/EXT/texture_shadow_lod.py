"""OpenGL extension EXT.texture_shadow_lod

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_shadow_lod to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for various shadow sampler types with texture
	functions having interactions with the LOD of texture lookups.  Modern
	shading languages support LOD queries for shadow sampler types, but until
	now the OpenGL Shading Language Specification has excluded multiple texture
	function overloads involving LOD calculations with various shadow samplers.
	Shading languages for other APIs do support the equivalent LOD-based
	texture sampling functions for these types which has made porting between
	those shading languages to GLSL cumbersome and has required the usage of
	sub-optimal workarounds.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/texture_shadow_lod.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.texture_shadow_lod import *
from OpenGL.raw.GL.EXT.texture_shadow_lod import _EXTENSION_NAME

def glInitTextureShadowLodEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION