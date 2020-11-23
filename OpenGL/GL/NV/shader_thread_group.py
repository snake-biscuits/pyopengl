"""OpenGL extension NV.shader_thread_group

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shader_thread_group to provide a more 
Python-friendly API

Overview (from the spec)
	
	Implementations of the OpenGL Shading Language may, but are not required 
	to, run multiple shader threads for a single stage as a SIMD thread group, 
	where individual execution threads are assigned to thread groups in an 
	undefined, implementation-dependent order.  This extension provides a set 
	of new features to the OpenGL Shading Language to query thread states and 
	to share data between fragments within a 2x2 pixel quad. 
	
	More specifically the following functionalities were added:
	
	*   New uniform variables and tokens to query the number of threads in a 
	    warp, the number of warps running on a SM and the number of SMs on the 
	    GPU.
	
	*   New shader inputs to query the thread id, the warp id and the SM id.
	
	*   New shader inputs to query if a fragment shader thread is a helper
	    thread.
	
	*   New shader built-in functions to query the state of a Boolean condition
	    over all threads in a thread group.
	
	*   New shader built-in functions to query which threads are active within
	    a thread group.        
	
	*   New fragment shader built-in functions to share data between fragments 
	    within a 2x2 pixel quad.
	
	Shaders using the new functionalities provided by this extension should 
	enable this functionality via the construct
	
	    #extension GL_NV_shader_thread_group : require     (or enable)
	
	This extension also specifies some modifications to the program assembly
	language to support the thread state query and thread data sharing
	functionalities.
	
	Note that in this extension specification warp and thread group have the
	same meaning.  A warp is a group of threads that get executed in lockstep.
	Each thread in a warp executes the same instruction of a program, but on
	different data.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/shader_thread_group.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.shader_thread_group import *
from OpenGL.raw.GL.NV.shader_thread_group import _EXTENSION_NAME

def glInitShaderThreadGroupNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION