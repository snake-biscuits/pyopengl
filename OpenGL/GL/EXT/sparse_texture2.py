"""OpenGL extension EXT.sparse_texture2

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.sparse_texture2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds on the ARB_sparse_texture extension, providing the
	following new functionality:
	
	  * New built-in GLSL texture lookup and image load functions are provided
	    that return information on whether the texels accessed for the texture
	    lookup accessed uncommitted texture memory.
	
	  * New built-in GLSL texture lookup functions are provided that specify a
	    minimum level of detail to use for lookups where the level of detail
	    is computed automatically.  This allows shaders to avoid accessing
	    unpopulated portions of high-resolution levels of detail when it knows
	    that the memory accessed is unpopulated, either from a priori
	    knowledge or from feedback provided by the return value of previously
	    executed "sparse" texture lookup functions.
	
	  * Reads of uncommitted texture memory will act as though such memory
	    were filled with zeroes; previously, the values returned by reads were
	    undefined.
	
	  * Standard implementation-independent virtual page sizes for internal
	    formats required to be supported with sparse textures. These standard
	    sizes can be requested by leaving VIRTUAL_PAGE_SIZE_INDEX_ARB at its
	    initial value (0).
	
	  * Support for creating sparse multisample and multisample array textures
	    is added.  However, the virtual page sizes for such textures remain
	    fully implementation-dependent.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/sparse_texture2.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.sparse_texture2 import *
from OpenGL.raw.GL.EXT.sparse_texture2 import _EXTENSION_NAME

def glInitSparseTexture2EXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION