"""OpenGL extension ARB.compute_variable_group_size

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.compute_variable_group_size to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows applications to write generic compute shaders that
	operate on workgroups with arbitrary dimensions.  Instead of specifying a
	fixed workgroup size in the compute shader, an application can use a
	compute shader using the /local_size_variable/ layout qualifer to indicate
	a variable workgroup size.  When using such compute shaders, the new
	command DispatchComputeGroupSizeARB should be used to specify both a
	workgroup size and workgroup count.
	
	In this extension, compute shaders with fixed group sizes must be
	dispatched by DispatchCompute and DispatchComputeIndirect.  Compute
	shaders with variable group sizes must be dispatched via
	DispatchComputeGroupSizeARB.  No support is provided in this extension for
	indirect dispatch of compute shaders with a variable group size.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/compute_variable_group_size.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.compute_variable_group_size import *
from OpenGL.raw.GL.ARB.compute_variable_group_size import _EXTENSION_NAME

def glInitComputeVariableGroupSizeARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION