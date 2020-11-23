"""OpenGL extension VERSION.GL_1_4

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_4 to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/VERSION/GL_1_4.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.VERSION.GL_1_4 import *
from OpenGL.raw.GL.VERSION.GL_1_4 import _EXTENSION_NAME

def glInitGl14VERSION():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

# INPUT glMultiDrawArrays.count size not checked against "drawcount"
# INPUT glMultiDrawArrays.first size not checked against "count"
glMultiDrawArrays=wrapper.wrapper(glMultiDrawArrays).setInputArraySize(
    "count", None
).setInputArraySize(
    "first", None
)
# INPUT glMultiDrawElements.count size not checked against "drawcount"
# INPUT glMultiDrawElements.indices size not checked against "drawcount"
glMultiDrawElements=wrapper.wrapper(glMultiDrawElements).setInputArraySize(
    "count", None
).setInputArraySize(
    "indices", None
)
# INPUT glPointParameterfv.params size not checked against "pname"
glPointParameterfv=wrapper.wrapper(glPointParameterfv).setInputArraySize(
    "params", None
)
# INPUT glPointParameteriv.params size not checked against "pname"
glPointParameteriv=wrapper.wrapper(glPointParameteriv).setInputArraySize(
    "params", None
)
glFogCoordfv=wrapper.wrapper(glFogCoordfv).setInputArraySize(
    "coord", 1
)
glFogCoorddv=wrapper.wrapper(glFogCoorddv).setInputArraySize(
    "coord", 1
)
# INPUT glFogCoordPointer.pointer size not checked against "type,stride"
glFogCoordPointer=wrapper.wrapper(glFogCoordPointer).setInputArraySize(
    "pointer", None
)
glSecondaryColor3bv=wrapper.wrapper(glSecondaryColor3bv).setInputArraySize(
    "v", 3
)
glSecondaryColor3dv=wrapper.wrapper(glSecondaryColor3dv).setInputArraySize(
    "v", 3
)
glSecondaryColor3fv=wrapper.wrapper(glSecondaryColor3fv).setInputArraySize(
    "v", 3
)
glSecondaryColor3iv=wrapper.wrapper(glSecondaryColor3iv).setInputArraySize(
    "v", 3
)
glSecondaryColor3sv=wrapper.wrapper(glSecondaryColor3sv).setInputArraySize(
    "v", 3
)
glSecondaryColor3ubv=wrapper.wrapper(glSecondaryColor3ubv).setInputArraySize(
    "v", 3
)
glSecondaryColor3uiv=wrapper.wrapper(glSecondaryColor3uiv).setInputArraySize(
    "v", 3
)
glSecondaryColor3usv=wrapper.wrapper(glSecondaryColor3usv).setInputArraySize(
    "v", 3
)
# INPUT glSecondaryColorPointer.pointer size not checked against "size,type,stride"
glSecondaryColorPointer=wrapper.wrapper(glSecondaryColorPointer).setInputArraySize(
    "pointer", None
)
glWindowPos2dv=wrapper.wrapper(glWindowPos2dv).setInputArraySize(
    "v", 2
)
glWindowPos2fv=wrapper.wrapper(glWindowPos2fv).setInputArraySize(
    "v", 2
)
glWindowPos2iv=wrapper.wrapper(glWindowPos2iv).setInputArraySize(
    "v", 2
)
glWindowPos2sv=wrapper.wrapper(glWindowPos2sv).setInputArraySize(
    "v", 2
)
glWindowPos3dv=wrapper.wrapper(glWindowPos3dv).setInputArraySize(
    "v", 3
)
glWindowPos3fv=wrapper.wrapper(glWindowPos3fv).setInputArraySize(
    "v", 3
)
glWindowPos3iv=wrapper.wrapper(glWindowPos3iv).setInputArraySize(
    "v", 3
)
glWindowPos3sv=wrapper.wrapper(glWindowPos3sv).setInputArraySize(
    "v", 3
)
# END AUTOGENERATED SECTION
GL_CURRENT_FOG_COORD = GL_CURRENT_FOG_COORDINATE # alias
GL_FOG_COORD = GL_FOG_COORDINATE # alias
GL_FOG_COORD_ARRAY = GL_FOG_COORDINATE_ARRAY # alias
GL_FOG_COORD_ARRAY_POINTER = GL_FOG_COORDINATE_ARRAY_POINTER # alias
GL_FOG_COORD_ARRAY_STRIDE = GL_FOG_COORDINATE_ARRAY_STRIDE # alias
GL_FOG_COORD_ARRAY_TYPE = GL_FOG_COORDINATE_ARRAY_TYPE # alias
GL_FOG_COORD_SRC = GL_FOG_COORDINATE_SOURCE # alias
