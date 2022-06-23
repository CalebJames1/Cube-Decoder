import unittest

from Cube import Cube
from Solver import Solver


class RubiksCubeTest(unittest.TestCase):
    def test_cube_solved(self):
        white = "gywywgogo"
        orange = "royoorbbo"
        green = "gogbgbyrg"
        red = "wrborwwyb"
        blue = "ogygbwybw"
        yellow = "bwrwyrryr"
        cube = Cube(white, orange, green, red, blue, yellow)
        solver = Solver(cube)
        solver.solve_cube()
        self.assertTrue(cube.is_solved())  # add assertion here

    def test_edge_thing(self):
        white = "wogwwryry"
        orange = "rrgooybbr"
        green = "ogbrgbygb"
        red = "rbworwoww"
        blue = "ogggbyoow"
        yellow = "gyyyybrwb"
        cube = Cube(white, orange, green, red, blue, yellow)
        self.assertFalse(cube.pieces_permutable())

    def test_edge_orientation(self):
        white = "gbwwwgobb"
        orange = "rryooorgo"
        green = "gywwgwwyy"
        red = "robgrorbo"
        blue = "orybbyygw"
        yellow = "grbrywgyb"
        cube = Cube(white, orange, green, red, blue, yellow)
        self.assertFalse(cube.edges_solvable())

    def test_corner_orientation(self):
        white = "yywywrwwg"
        orange = "rbgwoobbw"
        green = "rooggggbb"
        red = "ywrrryoyg"
        blue = "bgbrbgrbo"
        yellow = "orywyowoy"
        cube = Cube(white, orange, green, red, blue, yellow)
        self.assertFalse(cube.corners_solvable())

    def test_corner_thing(self):
        white = "groywogwr"
        orange = "orrgobryg"
        green = "wrbogorbb"
        red = "wwygrrwyb"
        blue = "gbwgbwoby"
        yellow = "yyogyobwy"
        cube = Cube(white, orange, green, red, blue, yellow)
        self.assertFalse(cube.pieces_permutable())


if __name__ == '__main__':
    unittest.main()
