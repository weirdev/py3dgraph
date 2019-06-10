import os
import numpy as np
from ctypes import cdll, c_double, c_uint, c_ubyte, POINTER, Structure, c_double

parentdir = os.path.dirname(os.path.abspath(__file__))
if os.name == 'nt':
    graphing3d = cdll.LoadLibrary(os.path.join(parentdir, r"../graphing3dlib/graphing3d"))

elif os.name == 'posix':
    graphing3d = cdll.LoadLibrary(os.path.join(parentdir, r"../graphing3dlib/libgraphing3d.so"))

subroutine1 = graphing3d.subroutine1
_plot3d_scatter_internal = graphing3d.plot3d_scatter

class RgbaStruct(Structure):
    _fields_ = [("r", c_ubyte),
                ("g", c_ubyte),
                ("b", c_ubyte),
                ("a", c_ubyte)]

# Tait–Bryan angle vector in radians (x, y, z)
class TbaStruct(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double)]

def plot3d_scatter(points: np.ndarray, color: (int, int, int, int), axes_rotation=(0.0, 0.0, 0.0)):
    """Generate a scatterplot image. Note this function
    operates directly on the memory storing `points`, so 
    `points` should be copied if it is to be used after
    this call."""
    pointcount = c_uint(points.shape[0])
    # TODO: force data to be laid out in row major order
    c_double_ptr = POINTER(c_double)
    beffore_ptr = points.ctypes.data_as(c_double_ptr)
    color_struct = RgbaStruct(*color)
    rotation_struct = TbaStruct(*axes_rotation)
    _plot3d_scatter_internal(beffore_ptr, pointcount, color_struct, rotation_struct)
