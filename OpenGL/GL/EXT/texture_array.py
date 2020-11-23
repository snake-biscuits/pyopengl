"""OpenGL extension EXT.texture_array

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces the notion of one- and two-dimensional array
	textures.  An array texture is a collection of one- and two-dimensional
	images of identical size and format, arranged in layers.  A
	one-dimensional array texture is specified using TexImage2D; a
	two-dimensional array texture is specified using TexImage3D.  The height
	(1D array) or depth (2D array) specify the number of layers in the image.
	
	An array texture is accessed as a single unit in a programmable shader,
	using a single coordinate vector.  A single layer is selected, and that
	layer is then accessed as though it were a one- or two-dimensional
	texture.  The layer used is specified using the "t" or "r" texture
	coordinate for 1D and 2D array textures, respectively.  The layer
	coordinate is provided as an unnormalized floating-point value in the
	range [0,<n>-1], where <n> is the number of layers in the array texture.
	Texture lookups do not filter between layers, though such filtering can be
	achieved using programmable shaders.  When mipmapping is used, each level
	of an array texture has the same number of layers as the base level; the
	number of layers is not reduced as the image size decreases.
	
	Array textures can be rendered to by binding them to a framebuffer object
	(EXT_framebuffer_object).  A single layer of an array texture can be bound
	using normal framebuffer object mechanisms, or an entire array texture can
	be bound and rendered to using the layered rendering mechanisms provided
	by NV_geometry_program4.
	
	This extension does not provide for the use of array textures with
	fixed-function fragment processing.  Such support could be added by
	providing an additional extension allowing applications to pass the new
	target enumerants (TEXTURE_1D_ARRAY_EXT and TEXTURE_2D_ARRAY_EXT) to
	Enable and Disable.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/texture_array.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.texture_array import *
from OpenGL.raw.GL.EXT.texture_array import _EXTENSION_NAME

def glInitTextureArrayEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION