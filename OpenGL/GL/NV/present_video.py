"""OpenGL extension NV.present_video

This module customises the behaviour of the 
OpenGL.raw.GL.NV.present_video to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism for displaying textures and
	renderbuffers on auxiliary video output devices.  It allows an
	application to specify separate buffers for the individual
	fields used with interlaced output.  It also provides a way
	to present frames or field pairs simultaneously in two separate
	video streams.  It also allows an application to request when images
	should be displayed, and to obtain feedback on exactly when images
	are actually first displayed.
	
	This specification attempts to avoid language that would tie it to
	any particular hardware or vendor.  However, it should be noted that
	it has been designed specifically for use with NVIDIA SDI products
	and the features and limitations of the spec compliment those of
	NVIDIA"s line of SDI video output devices.

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/NV/present_video.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.present_video import *
from OpenGL.raw.GL.NV.present_video import _EXTENSION_NAME

def glInitPresentVideoNV():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)

glGetVideoivNV=wrapper.wrapper(glGetVideoivNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
glGetVideouivNV=wrapper.wrapper(glGetVideouivNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
glGetVideoi64vNV=wrapper.wrapper(glGetVideoi64vNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
glGetVideoui64vNV=wrapper.wrapper(glGetVideoui64vNV).setOutput(
    "params",size=_glgets._glget_size_mapping,pnameArg="pname",orPassIn=True
)
# END AUTOGENERATED SECTION