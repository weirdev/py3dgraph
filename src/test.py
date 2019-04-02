import numpy as np
import py3dgraph

def scatter():
    pointcoords = (np.random.rand(3*20) * 0.8) + 0.1
    points = pointcoords.reshape((20, 3))
    py3dgraph.plot3d_scatter(points)

if __name__ == '__main__':
    #py3dgraph.subroutine1()
    scatter()
    pass