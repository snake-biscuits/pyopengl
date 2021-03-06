"""Autogenerated by xml_generate script, do not edit!"""
from OpenGL import platform as _p
from OpenGL.raw.EGL import _types as _cs
from OpenGL.raw.EGL import _errors


_EXTENSION_NAME = "EGL_ANDROID_blob_cache"


def _f(function):
    return _p.createFunction(function, _p.PLATFORM.EGL, "EGL_ANDROID_blob_cache", error_checker=_errors._error_checker)


@_f
@_p.types(None, _cs.EGLDisplay, _cs.EGLSetBlobFuncANDROID, _cs.EGLGetBlobFuncANDROID)
def eglSetBlobCacheFuncsANDROID(dpy, set, get):
    pass
