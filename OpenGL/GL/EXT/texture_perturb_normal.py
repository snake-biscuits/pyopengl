"""OpenGL extension EXT.texture_perturb_normal

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_perturb_normal to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines a mechanism for using texture values to perturb
	the fragment normal vector prior to fragment lighting.  It enables a
	direct implementation of the original formulation of bump mapping by
	Blinn.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/texture_perturb_normal.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.texture_perturb_normal import *
from OpenGL.raw.GL.EXT.texture_perturb_normal import _EXTENSION_NAME

def glInitTexturePerturbNormalEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION