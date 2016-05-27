import numpy as np

from ..meshes import RectangularMesh, Point2d


class TestMesh:

    def test_mesh_generation(self):
        """Tests if the mesh generation is correct."""

        mesh = RectangularMesh(shape=Point2d(4, 4),
                               origin=Point2d(0, 0),
                               sizes=Point2d(1, 2),
                               offset=Point2d(0, 0))
        np.allclose(mesh.x, [i * .25 for i in range(4)])
        np.allclose(mesh.y, [i * .5 for i in range(4)])

    def test_mesh_generation_with_offset(self):
        mesh = RectangularMesh(shape=Point2d(4, 4),
                               origin=Point2d(0, 0),
                               sizes=Point2d(1, 2),
                               offset=Point2d(0.25, 0.3))

        np.allclose(mesh.x, [i * .25 + .25 * .25 for i in range(4)])
        np.allclose(mesh.y, [i * .5 + .3 * .5 for i in range(4)])
