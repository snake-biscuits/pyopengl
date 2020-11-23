"""OpenGL extension ARM.shader_framebuffer_fetch

This module customises the behaviour of the 
OpenGL.raw.GLES2.ARM.shader_framebuffer_fetch to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables fragment shaders to read existing framebuffer
	data as input. This permits use-cases such as programmable blending,
	and other operations that may not be possible to implement with
	fixed-function blending.
	
	This extension also adds the ability to indicate that a shader should
	be run once per sample instead of once per pixel.
	
	Reading framebuffer data as input in combination with multiple render
	targets (MRT) may not be supported by all implementations. This
	extension allows applications to query for this capability.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARM/shader_framebuffer_fetch.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.ARM.shader_framebuffer_fetch import *
from OpenGL.raw.GLES2.ARM.shader_framebuffer_fetch import _EXTENSION_NAME

def glInitShaderFramebufferFetchARM():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION