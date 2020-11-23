"""OpenGL extension OES.compressed_paletted_texture

This module customises the behaviour of the 
OpenGL.raw.GL.OES.compressed_paletted_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	The goal of this extension is to allow direct support of palettized
	textures in OpenGL ES.
	
	Palettized textures are implemented in OpenGL ES using the
	CompressedTexImage2D call. The definition of the following parameters
	"level" and "internalformat" in the CompressedTexImage2D call have
	been extended to support paletted textures.
	
	A paletted texture is described by the following data:
	
	    palette format
	        can be R5_G6_B5, RGBA4, RGB5_A1, RGB8, or RGBA8
	
	    number of bits to represent texture data
	        can be 4 bits or 8 bits per texel.  The number of bits
	        also detemine the size of the palette.  For 4 bits/texel
	        the palette size is 16 entries and for 8 bits/texel the
	        palette size will be 256 entries.
	
	        The palette format and bits/texel are encoded in the
	        "internalformat" parameter.
	
	    palette data and texture mip-levels
	        The palette data followed by all necessary mip levels are
	        passed in "data" parameter of CompressedTexImage2D.
	
	        The size of palette is given by palette format and bits / texel.
	        A palette format of RGB_565 with 4 bits/texel imply a palette
	        size of 2 bytes/palette entry * 16 entries = 32 bytes.
	
	        The level value is used to indicate how many mip levels
	        are described.  Negative level values are used to define
	        the number of miplevels described in the "data" component.
	        A level of zero indicates a single mip-level.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OES/compressed_paletted_texture.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.OES.compressed_paletted_texture import *
from OpenGL.raw.GL.OES.compressed_paletted_texture import _EXTENSION_NAME

def glInitCompressedPalettedTextureOES():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION