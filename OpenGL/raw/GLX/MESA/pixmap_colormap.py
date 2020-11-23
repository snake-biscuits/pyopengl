"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = "GLX_MESA_pixmap_colormap"
def _f(function):
    return _p.createFunction(function,_p.PLATFORM.GLX,"GLX_MESA_pixmap_colormap",error_checker=_errors._error_checker)

@_f
@_p.types(_cs.GLXPixmap,ctypes.POINTER(_cs.Display),ctypes.POINTER(_cs.XVisualInfo),_cs.Pixmap,_cs.Colormap)
def glXCreateGLXPixmapMESA(dpy,visual,pixmap,cmap):pass
