"""OpenGL extension AMD.shader_image_load_store_lod

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.shader_image_load_store_lod to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension was developed based on the ARB_shader_image_load_store
	extension to allow implementations supporting loads and stores on
	mipmap texture images.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/AMD/shader_image_load_store_lod.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.shader_image_load_store_lod import *
from OpenGL.raw.GL.AMD.shader_image_load_store_lod import _EXTENSION_NAME

def glInitShaderImageLoadStoreLodAMD():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION