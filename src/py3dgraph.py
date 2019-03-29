import os
from ctypes import cdll

if os.name == 'nt':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/graphing3d")

elif os.name == 'posix':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/libgraphing3d.so")

subroutine1 = graphing3d.subroutine1
