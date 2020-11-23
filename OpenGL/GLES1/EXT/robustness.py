"""OpenGL extension EXT.robustness

This module customises the behaviour of the 
OpenGL.raw.GLES1.EXT.robustness to provide a more 
Python-friendly API

Overview (from the spec)
	
	Several recent trends in how OpenGL integrates into modern computer
	systems have created new requirements for robustness and security
	for OpenGL rendering contexts.
	
	Additionally GPU architectures now support hardware fault detection;
	for example, video memory supporting ECC (error correcting codes)
	and error detection.  OpenGL contexts should be capable of recovering
	from hardware faults such as uncorrectable memory errors.  Along with
	recovery from such hardware faults, the recovery mechanism can
	also allow recovery from video memory access exceptions and system
	software failures.  System software failures can be due to device
	changes or driver failures.
	
	OpenGL queries that that return (write) some number of bytes to a
	buffer indicated by a pointer parameter introduce risk of buffer
	overflows that might be exploitable by malware. To address this,
	queries with return value sizes that are not expressed directly by
	the parameters to the query itself are given additional API
	functions with an additional parameter that specifies the number of
	bytes in the buffer and never writing bytes beyond that limit. This
	is particularly useful for multi-threaded usage of OpenGL contexts
	in a "share group" where one context can change objects in ways that
	can cause buffer overflows for another context"s OpenGL queries.
	
	The original ARB_vertex_buffer_object extension includes an issue
	that explicitly states program termination is allowed when
	out-of-bounds vertex buffer object fetches occur. Modern graphics
	hardware is capable well-defined behavior in the case of out-of-
	bounds vertex buffer object fetches. Older hardware may require
	extra checks to enforce well-defined (and termination free)
	behavior, but this expense is warranted when processing potentially
	untrusted content.
	
	The intent of this extension is to address some specific robustness
	goals:
	
	*   For all existing OpenGL queries, provide additional "safe" APIs 
	    that limit data written to user pointers to a buffer size in 
	    bytes that is an explicit additional parameter of the query.
	
	*   Provide a mechanism for an OpenGL application to learn about
	    graphics resets that affect the context.  When a graphics reset
	    occurs, the OpenGL context becomes unusable and the application
	    must create a new context to continue operation. Detecting a
	    graphics reset happens through an inexpensive query.
	
	*   Provide an enable to guarantee that out-of-bounds buffer object
	    accesses by the GPU will have deterministic behavior and preclude
	    application instability or termination due to an incorrect buffer
	    access.  Such accesses include vertex buffer fetches of
	    attributes and indices, and indexed reads of uniforms or
	    parameters from buffers.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/robustness.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.EXT.robustness import *
from OpenGL.raw.GLES1.EXT.robustness import _EXTENSION_NAME

def glInitRobustnessEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

# INPUT glReadnPixelsEXT.data size not checked against bufSize
glReadnPixelsEXT=wrapper.wrapper(glReadnPixelsEXT).setInputArraySize(
    "data", None
)
# INPUT glGetnUniformfvEXT.params size not checked against bufSize
glGetnUniformfvEXT=wrapper.wrapper(glGetnUniformfvEXT).setInputArraySize(
    "params", None
)
# INPUT glGetnUniformivEXT.params size not checked against bufSize
glGetnUniformivEXT=wrapper.wrapper(glGetnUniformivEXT).setInputArraySize(
    "params", None
)
# END AUTOGENERATED SECTION