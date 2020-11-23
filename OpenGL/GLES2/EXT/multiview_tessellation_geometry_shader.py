"""OpenGL extension EXT.multiview_tessellation_geometry_shader

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.multiview_tessellation_geometry_shader to provide a more 
Python-friendly API

Overview (from the spec)
	
	OVR_multiview introduced multiview rendering to OpenGL and OpenGL ES.
	
	This extension removes one of the limitations of the OVR_multiview 
	extension by allowing the use of tessellation control, tessellation 
	evaluation, and geometry shaders during multiview rendering. 
	OVR_multiview by itself forbids the use of any of these shader types.
	
	When using tessellation control, tessellation evaluation, and geometry 
	shaders during multiview rendering, any such shader must use the 
	"num_views" layout qualifier provided by the matching shading language 
	extension to specify a view count. The view count specified in these 
	shaders must match the count specified in the vertex shader. Additionally, 
	the shading language extension allows these shaders to use the 
	gl_ViewID_OVR built-in to handle tessellation or geometry shader processing 
	differently for each view.
	
	OVR_multiview2 extends OVR_multiview by allowing view-dependent values
	for any vertex attributes instead of just the position. This new extension
	does not imply the availability of OVR_multiview2, but if both are available,
	view-dependent values for any vertex attributes are also allowed in 
	tessellation control, tessellation evaluation, and geometry shaders.
	

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/multiview_tessellation_geometry_shader.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.multiview_tessellation_geometry_shader import *
from OpenGL.raw.GLES2.EXT.multiview_tessellation_geometry_shader import _EXTENSION_NAME

def glInitMultiviewTessellationGeometryShaderEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION