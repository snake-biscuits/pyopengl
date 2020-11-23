"""OpenGL extension ATI.texture_env_combine3

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.texture_env_combine3 to provide a more 
Python-friendly API

Overview (from the spec)
	
	Adds new set of operations to the texture combiner operations.
	
	MODULATE_ADD_ATI               Arg0 * Arg2 + Arg1
	MODULATE_SIGNED_ADD_ATI        Arg0 * Arg2 + Arg1 - 0.5
	MODULATE_SUBTRACT_ATI          Arg0 * Arg2 - Arg1
	
	where Arg0, Arg1 and Arg2 are derived from
	
	    PRIMARY_COLOR_ARB       primary color of incoming fragment
	    TEXTURE                 texture color of corresponding texture unit
	    CONSTANT_ARB            texture environment constant color
	    PREVIOUS_ARB            result of previous texture environment; on
	                            texture unit 0, this maps to PRIMARY_COLOR_ARB
	
	In addition, the result may be scaled by 1.0, 2.0 or 4.0.
	
	Note that in addition to providing more flexible equations new source 
	inputs have been added for zero and one.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ATI/texture_env_combine3.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ATI.texture_env_combine3 import *
from OpenGL.raw.GL.ATI.texture_env_combine3 import _EXTENSION_NAME

def glInitTextureEnvCombine3ATI():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION