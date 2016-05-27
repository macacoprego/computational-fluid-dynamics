import numpy as np



class Vector(np.ndarray):

    def __new__(subtype, shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None, mesh=None):
        assert isinstance(shape, int), "A vector shape must be an integer"
        obj = np.ndarray.__new__(subtype, shape, dtype, buffer, offset, strides,
                                 order)
        obj.mesh = mesh
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.mesh = getattr(obj, 'mesh', None)


class Matrix(np.ndarray):
    def __new__(subtype, shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None, mesh=None):
        assert isinstance(shape, tuple) and len(shape) == 2, \
            "A matrix shape must be a 2 dimensional tuple"
        obj = np.ndarray.__new__(subtype, shape, dtype, buffer, offset, strides,
                                 order)
        obj.mesh = mesh
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.mesh = getattr(obj, 'mesh', None)