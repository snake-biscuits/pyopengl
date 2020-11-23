"""OpenGL extension ANGLE.d3d_share_handle_client_buffer

This module customises the behaviour of the 
OpenGL.raw.EGL.ANGLE.d3d_share_handle_client_buffer to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ANGLE/d3d_share_handle_client_buffer.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.ANGLE.d3d_share_handle_client_buffer import *
from OpenGL.raw.EGL.ANGLE.d3d_share_handle_client_buffer import _EXTENSION_NAME

def glInitD3DShareHandleClientBufferANGLE():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION