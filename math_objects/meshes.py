import numpy as np

from .tensors import Vector


class Point2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    @staticmethod
    def _raise_unsupported_type(method_name, obj):
        class UnsupportedType(Exception):
            def __str__(self):
                return "{} not implemented for type {}"\
                    .format(method_name, type(obj))
        raise UnsupportedType()

    def __floordiv__(self, other):
        if isinstance(other, Point2d):
            return Point2d(self.x // other.x, self.y // other.y)
        if isinstance(other, (int, float)):
            return Point2d(self.x // other, self.y // other)
        self._raise_unsupported_type("Division", other)

    def __truediv__(self, other):
        if isinstance(other, Point2d):
            return Point2d(self.x / float(other.x), self.y / float(other.y))
        if isinstance(other, (int, float)):
            return Point2d(self.x / float(other), self.y / float(other))
        raise NotImplementedError("Division not implemented for type ",
                                  type(other))
        self._raise_unsupported_type("Division", other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point2d(self.x * other, self.y * other)
        if isinstance(other, Point2d):
            return Point2d(self.x * other.x, self.y * other.y)
        self._raise_unsupported_type("Multiplication", other)

    __rmul__ = __mul__

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Point2d(self.x + other, self.y + other)
        if isinstance(other, Point2d):
            return Point2d(self.x + other.x, self.y + other.y)
        self._raise_unsupported_type("Addition", other)

    def as_tuple(self):
        return self.x, self.y


class RectangularMesh:

    def __init__(self, shape, origin, sizes, offset=(0, 0)):

        """A rectangular mesh is a collection of points, evenly spaced on a
        given axis, that span a collection of rectangular cells that generate
        a rectangle in 2 dimensional space.

        shape: Point2d with the number of points in the x and y axis

        origin: Point2d with the (x,y) coordinates of the origin

        sizes: Point2d with the sizes for the x and y axis.

        offset: Point2d with values between 0 and 1, containing the
        displacement of the cell point.
        By default, the generated mesh points will be put on the bottom-left
        corner of it's containing cell.
        By providing an offset, you can move where the points will be
        positioned within the cells.
        For example:
        (0, 0): the cell point will be in the bottom-left corner of the cell
        (0.5, 0.5): the point will be in the center of the cell
        (1, 0.5): the point will be in the center of the right segment of the
        cell.

        Example:
            RectangularMesh(Point2d(4,4), Point2d(0,1), Point2d(1,1))
            will generate a Mesh that represents the rectangle that has the
            bottom-left corner at (0,1), and upper-right corner at (1,2),
            with 4 points evenly spaced along the x and y axis.
        """
        for arg in [shape, origin, sizes, offset]:
            assert isinstance(arg, Point2d)

        self.shape = shape
        self.origin = origin
        self.sizes = sizes
        self.offset = offset
        self.h = (self.sizes / self.shape)  # distance between grid points

        actual_offset = (self.h * offset)

        new_origin = origin + actual_offset

        self._x = np.linspace(new_origin.x,
                              new_origin.x + sizes.x,
                              shape.x + 1)[:-1]

        self._y = np.linspace(new_origin.y,
                              new_origin.y + sizes.y,
                              shape.y + 1)[:-1]

        self._xv, self._yv = np.meshgrid(self._x, self._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def as_arrays(self):
        """Return two 2-dimensional arrays with the x's and y's coordinates."""
        return self._xv, self._yv
