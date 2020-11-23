"""OpenGL extension EXT.image_dma_buf_import

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.image_dma_buf_import to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/image_dma_buf_import.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.image_dma_buf_import import *
from OpenGL.raw.EGL.EXT.image_dma_buf_import import _EXTENSION_NAME

def glInitImageDmaBufImportEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION