"""OpenGL extension OES.compressed_ETC1_RGB8_texture

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.compressed_ETC1_RGB8_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	The goal of this extension is to allow direct support of
	compressed textures in the Ericsson Texture Compression (ETC)
	formats in OpenGL ES.
	
	ETC-compressed textures are handled in OpenGL ES using the
	CompressedTexImage2D call.
	
	The definition of the "internalformat" parameter in the
	CompressedTexImage2D call has been extended to support
	ETC-compressed textures. 
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OES/compressed_ETC1_RGB8_texture.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.compressed_ETC1_RGB8_texture import *
from OpenGL.raw.GLES2.OES.compressed_ETC1_RGB8_texture import _EXTENSION_NAME

def glInitCompressedEtc1Rgb8TextureOES():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION