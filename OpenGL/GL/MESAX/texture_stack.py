"""OpenGL extension MESAX.texture_stack

This module customises the behaviour of the 
OpenGL.raw.GL.MESAX.texture_stack to provide a more 
Python-friendly API

Overview (from the spec)
	
	There are a number of circumstances where an application may wish to
	blend two textures out of a larger set of textures.  Moreover, in some
	cases the selected textures may vary on a per-fragment basis within
	a polygon.  Several examples include:
	
	   1. High dynamic range textures.  The application stores several
	   different "exposures" of an image as different textures.  On a
	   per-fragment basis, the application selects which exposures are
	   used.
	
	   2. A terrain engine where the altitude of a point determines the
	   texture applied to it.  If the transition is from beach sand to
	   grass to rocks to snow, the application will store each texture
	   in a different texture map, and dynamically select which two
	   textures to blend at run-time.
	
	   3. Storing short video clips in textures.  Each depth slice is a
	   single frame of video.
	
	Several solutions to this problem have been proposed, but they either
	involve using a separate texture unit for each texture map or using 3D
	textures without mipmaps.  Both of these options have major drawbacks.
	
	This extension provides a third alternative that eliminates the major
	drawbacks of both previous methods.  A new texture target,
	TEXTURE_2D_STACK, is added that functions identically to TEXTURE_3D in
	all aspects except the sizes of the non-base level images.  In
	traditional 3D texturing, the size of the N+1 LOD is half the size
	of the N LOD in all three dimensions.  For the TEXTURE_2D_STACK target,
	the height and width of the N+1 LOD is halved, but the depth is the
	same for all levels of detail. The texture then becomes a "stack" of
	2D textures.  The per-fragment texel is selected by the R texture
	coordinate.
	
	References:
	
	    https://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=011557
	    https://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=000516
	    https://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=011903
	    https://www.delphi3d.net/articles/viewarticle.php?article=terraintex.htm

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/MESAX/texture_stack.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.MESAX.texture_stack import *
from OpenGL.raw.GL.MESAX.texture_stack import _EXTENSION_NAME

def glInitTextureStackMESAX():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION