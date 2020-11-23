"""OpenGL extension OVR.multiview

This module customises the behaviour of the 
OpenGL.raw.GL.OVR.multiview to provide a more 
Python-friendly API

Overview (from the spec)
	
	The method of stereo rendering supported in OpenGL is currently achieved by
	rendering to the two eye buffers sequentially.  This typically incurs double
	the application and driver overhead, despite the fact that the command
	streams and render states are almost identical.
	
	This extension seeks to address the inefficiency of sequential multiview
	rendering by adding a means to render to multiple elements of a 2D texture
	array simultaneously.  In multiview rendering, draw calls are instanced into
	each corresponding element of the texture array.  The vertex program uses a
	new gl_ViewID_OVR variable to compute per-view values, typically the vertex
	position and view-dependent variables like reflection.
	
	The formulation of this extension is high level in order to allow
	implementation freedom.  On existing hardware, applications and drivers can
	realize the benefits of a single scene traversal, even if all GPU work is
	fully duplicated per-view.  But future support could enable simultaneous
	rendering via multi-GPU, tile-based architectures could sort geometry into
	tiles for multiple views in a single pass, and the implementation could even
	choose to interleave at the fragment level for better texture cache
	utilization and more coherent fragment shader branching.
	
	The most obvious use case in this model is to support two simultaneous
	views: one view for each eye.  However, we also anticipate a usage where two
	views are rendered per eye, where one has a wide field of view and the other
	has a narrow one.  The nature of wide field of view planar projection is
	that the sample density can become unacceptably low in the view direction.
	By rendering two inset eye views per eye, we can get the required sample
	density in the center of projection without wasting samples, memory, and
	time by oversampling in the periphery.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/OVR/multiview.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.OVR.multiview import *
from OpenGL.raw.GL.OVR.multiview import _EXTENSION_NAME

def glInitMultiviewOVR():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION