"""OpenGL extension OES.texture_view

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.texture_view to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows a texture"s data store to be "viewed" in multiple
	ways, either reinterpreting the data format/type as a different format/
	type with the same element size, or by clamping the mipmap level range
	or array slice range.
	
	The goals of this extension are to avoid having these alternate views
	become shared mutable containers of shared mutable objects, and to add
	the views to the API in a minimally invasive way.
	
	No new object types are added. Conceptually, a texture object is split
	into the following parts:
	
	    - A data store holding texel data.
	    - State describing which portions of the data store to use, and how
	      to interpret the data elements.
	    - An embedded sampler object.
	    - Various other texture parameters.
	
	With this extension, multiple textures can share a data store and have
	different state describing which portions of the data store to use and
	how to interpret the data elements. The data store is refcounted and not
	destroyed until the last texture sharing it is deleted.
	
	This extension leverages the concept of an "immutable texture".
	Views can only be created of textures created with TexStorage*.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OES/texture_view.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.texture_view import *
from OpenGL.raw.GLES2.OES.texture_view import _EXTENSION_NAME

def glInitTextureViewOES():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION