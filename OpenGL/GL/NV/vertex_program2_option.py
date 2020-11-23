"""OpenGL extension NV.vertex_program2_option

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_program2_option to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides additional vertex program functionality
	to extend the standard ARB_vertex_program language and execution
	environment.  ARB programs wishing to use this added functionality
	need only add:
	
	    OPTION NV_vertex_program2;
	
	to the beginning of their vertex programs.
	
	The functionality provided by this extension, which is roughly
	equivalent to that provided by the NV_vertex_program2 extension,
	includes:
	
	  * general purpose dynamic branching,
	
	  * subroutine calls,
	
	  * data-dependent conditional write masks,
	
	  * programmable user clip distances,
	
	  * address registers with four components (instead of just one),
	
	  * absolute value operator on scalar and swizzled operand loads,
	
	  * rudimentary address register math,
	
	  * SIN and COS trigonometry instructions, and
	
	  * fully orthogonal "set on" instructions, including a "set sign"
	    instruction.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/vertex_program2_option.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.vertex_program2_option import *
from OpenGL.raw.GL.NV.vertex_program2_option import _EXTENSION_NAME

def glInitVertexProgram2OptionNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION