import os
import numpy as np
from ctypes import cdll, c_double, c_uint

if os.name == 'nt':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/graphing3d")

elif os.name == 'posix':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/libgraphing3d.so")

subroutine1 = graphing3d.subroutine1
_plot3d_scatter_internal = graphing3d.plot3d_scatter

def plot3d_scatter(points: np.ndarray):
    pointcount = c_uint(points.shape[0])
    points = points.flatten()
    BUFTYPE = c_double * len(points)
    buffer = BUFTYPE(*points)
    _plot3d_scatter_internal(buffer, pointcount)
