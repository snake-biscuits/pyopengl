"""OpenGL extension KHR.texture_compression_astc_sliced_3d

This module customises the behaviour of the 
OpenGL.raw.GLES2.KHR.texture_compression_astc_sliced_3d to provide a more 
Python-friendly API

Overview (from the spec)
	
	Adaptive Scalable Texture Compression (ASTC) is a new texture
	compression technology that offers unprecendented flexibility, while
	producing better or comparable results than existing texture
	compressions at all bit rates. It includes support for 2D and
	slice-based 3D textures, with low and high dynamic range, at bitrates
	from below 1 bit/pixel up to 8 bits/pixel in fine steps.
	
	This extension extends the functionality of
	GL_KHR_texture_compression_astc_ldr to include slice-based 3D textures
	for textures using the LDR profile in the same way as the HDR profile
	allows slice-based 3D textures.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/KHR/texture_compression_astc_sliced_3d.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.KHR.texture_compression_astc_sliced_3d import *
from OpenGL.raw.GLES2.KHR.texture_compression_astc_sliced_3d import _EXTENSION_NAME

def glInitTextureCompressionAstcSliced3DKHR():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION