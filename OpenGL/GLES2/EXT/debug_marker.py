"""OpenGL extension EXT.debug_marker

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.debug_marker to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines a mechanism for OpenGL and OpenGL ES applications to
	annotate their command stream with markers for discrete events and groups 
	of commands using descriptive text markers. 
	
	When profiling or debugging such an application within a debugger or 
	profiler it is difficult to relate the commands within the command stream 
	to the elements of the scene or parts of the program code to which they 
	correspond. Markers help obviate this by allowing applications to specify 
	this link.
	
	The intended purpose of this is purely to improve the user experience 
	within OpenGL and OpenGL ES development tools.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/debug_marker.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.debug_marker import *
from OpenGL.raw.GLES2.EXT.debug_marker import _EXTENSION_NAME

def glInitDebugMarkerEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION