"""OpenGL extension ARB.pipeline_statistics_query

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.pipeline_statistics_query to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces new query types that allow applications to get
	statistics information about different parts of the pipeline:
	
	  * Number of vertices and primitives issued to the GL;
	
	  * Number of times a vertex shader, tessellation evaluation shader,
	    geometry shader, fragment shader, and compute shader was invoked;
	
	  * Number of patches processed by the tessellation control shader stage;
	
	  * Number of primitives emitted by a geometry shader;
	
	  * Number of primitives that entered the primitive clipping stage;
	
	  * Number of primitives that are output by the primitive clipping stage;

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ARB/pipeline_statistics_query.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.pipeline_statistics_query import *
from OpenGL.raw.GL.ARB.pipeline_statistics_query import _EXTENSION_NAME

def glInitPipelineStatisticsQueryARB():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION