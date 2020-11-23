"""OpenGL extension ARB.shader_precision

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_precision to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension more clearly restricts the precision requirements of 
	implementations of the GLSL specification.  These include precision of 
	arithmetic operations (operators "+", "/", ...), transcendentals (log, exp, 
	pow, reciprocal sqrt, ...), when NaNs (not a number) and INFs (infinities) will
	be supported and generated, and denorm flushing behavior.  Trigonometric 
	built-ins and some other categories of built-ins are not addressed.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/shader_precision.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shader_precision import *
from OpenGL.raw.GL.ARB.shader_precision import _EXTENSION_NAME

def glInitShaderPrecisionARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION