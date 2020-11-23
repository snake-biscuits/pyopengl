"""OpenGL extension S3.s3tc

This module customises the behaviour of the 
OpenGL.raw.GL.S3.s3tc to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows specifying texture data in compressed S3TC
	format.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/S3/s3tc.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.S3.s3tc import *
from OpenGL.raw.GL.S3.s3tc import _EXTENSION_NAME

def glInitS3TcS3():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION