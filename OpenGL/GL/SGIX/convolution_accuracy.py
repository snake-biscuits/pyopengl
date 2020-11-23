"""OpenGL extension SGIX.convolution_accuracy

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.convolution_accuracy to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds an accuracy hint for convolution.  It
	allows the program to trade off precision for speed.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/SGIX/convolution_accuracy.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.convolution_accuracy import *
from OpenGL.raw.GL.SGIX.convolution_accuracy import _EXTENSION_NAME

def glInitConvolutionAccuracySGIX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION