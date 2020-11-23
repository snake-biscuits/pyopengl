"""OpenGL extension INTEL.fragment_shader_ordering

This module customises the behaviour of the 
OpenGL.raw.GL.INTEL.fragment_shader_ordering to provide a more 
Python-friendly API

Overview (from the spec)
	
	Graphics devices may execute in parallel fragment shaders referring to the
	same window xy coordinates. Framebuffer writes are guaranteed to be
	processed in primitive rasterization order, but there is no order guarantee
	for other instructions and image or buffer object accesses in
	particular.
	
	The extension introduces a new GLSL built-in function, 
	beginFragmentShaderOrderingINTEL(), which blocks execution of a fragment 
	shader invocation until invocations from previous primitives that map to 
	the same xy window coordinates (and same sample when per-sample shading
	is active) complete their execution. All memory transactions from previous 
	fragment shader invocations are made visible to the fragment shader 
	invocation that called beginFragmentShaderOrderingINTEL() when the function 
	returns. 
	
	Including the following line in a shader can be used to control the
	language features described in this extension:
	
	  #extension GL_INTEL_fragment_shader_ordering : <behavior>
	
	where <behavior> is as specified in section 3.3.
	
	New preprocessor #defines are added to the OpenGL Shading Language:
	
	  #define GL_INTEL_fragment_shader_ordering 1

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/INTEL/fragment_shader_ordering.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.INTEL.fragment_shader_ordering import *
from OpenGL.raw.GL.INTEL.fragment_shader_ordering import _EXTENSION_NAME

def glInitFragmentShaderOrderingINTEL():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION