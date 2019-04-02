import os
import numpy as np
from ctypes import cdll, c_double, c_uint, POINTER

if os.name == 'nt':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/graphing3d")

elif os.name == 'posix':
    graphing3d = cdll.LoadLibrary(r"../graphing3dlib/libgraphing3d.so")

subroutine1 = graphing3d.subroutine1
_plot3d_scatter_internal = graphing3d.plot3d_scatter

def plot3d_scatter(points: np.ndarray):
    """Generate a scatterplot image. Note this function
    operates directly on the memory storing `points`, so 
    `points` should be copied if it is to be used after
    this call."""
    pointcount = c_uint(points.shape[0])
    # TODO: force data to be laid out in row major order
    c_double_ptr = POINTER(c_double)
    beffore_ptr = points.ctypes.data_as(c_double_ptr)
    _plot3d_scatter_internal(beffore_ptr, pointcount)
