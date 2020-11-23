"""OpenGL extension NV.fragment_coverage_to_color

This module customises the behaviour of the 
OpenGL.raw.GL.NV.fragment_coverage_to_color to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows the fragment coverage value, represented as an
	integer bitfield, to be substituted for a color output being written to a
	single-component color buffer with integer components (e.g., R8UI).  The
	capability provided by this extension is different from simply writing the
	gl_SampleMask fragment shader output in that the coverage value written to
	the framebuffer is taken after alpha test, stencil test, and depth test,
	as well as after the multisample fragment operations such as
	alpha-to-coverage.
	
	This functionality may be useful for deferred rendering algorithms, where
	the second pass needs to know which samples belong to which original 
	fragments.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/fragment_coverage_to_color.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.fragment_coverage_to_color import *
from OpenGL.raw.GL.NV.fragment_coverage_to_color import _EXTENSION_NAME

def glInitFragmentCoverageToColorNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION