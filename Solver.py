from Cube import Cube
from Side import Side


class Solver:
    def __init__(self, *args):
        if len(args) == 0:
            white = input("Enter the colors of the white side: ")
            orange = input("Enter the colors of the orange side: ")
            green = input("Enter the colors of the green side: ")
            red = input("Enter the colors of the red side: ")
            blue = input("Enter the colors of the blue side: ")
            yellow = input("Enter the colors of the yellow side: ")
            self.cube = Cube(white, orange, green, red, blue, yellow)
            self.cube.solvable()
        else:
            self.cube = args[0]
            self.cube.solvable()

    def solve_cross(self):
        if self.cube.get_location(47) != 47 or self.cube.get_location(51) != 51 or self.cube.get_location(53) != 53 \
        or self.cube.get_location(49) != 49:
            print("Solving the cross:")
            #df edge
            if self.cube.get_location(47) != 47:
                print("First edge:")
                move_map = {2: "u2 f2",
                            4: "u: f2",
                            6: "u f2",
                            8: "f2",
                            11: "l f:",
                            13: "l2 f:",
                            15: "f:",
                            17: "l: f:",
                            20: "u: r: f",
                            22: "r: d",
                            24: "r: d:",
                            26: "f: d r: d:",
                            29: "r: f",
                            31: "f",
                            33: "r2 f",
                            35: "r f",
                            38: "u r: f",
                            40: "r d:",
                            42: "l: d",
                            44: "b r d:",
                            49: "d",
                            51: "d:",
                            53: "d2",
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(47)])
            if self.cube.get_location(51) != 51:
                print("Second edge:")
                move_map = {2: "u r2",
                            4: "u2 r2",
                            6: "r2",
                            8: "u: r2",
                            11: "u: f r: f:",
                            13: "l2 d: f: d",
                            15: "d: f: d",
                            17: "l: d: f: d",
                            20: "f r: f:",
                            22: "d2 l d2",
                            24: "r:",
                            29: "u f r:",
                            31: "d: f d",
                            33: "d b: d:",
                            35: "r d: f d",
                            38: "b: r",
                            40: "r",
                            42: "d2 l: d2",
                            44: "b r",
                            49: "l: d2 l d2",
                            53: "f: d: f",
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(51)])
            if self.cube.get_location(53) != 53:
                print("Third edge:")
                move_map = {2: "b2",
                            4: "u b2",
                            6: "u: b2",
                            8: "u2 b2",
                            11: "l: b",
                            13: "b",
                            15: "l2 b",
                            17: "l b",
                            20: "u l: b",
                            22: "d l d:",
                            24: "d: r: d",
                            29: "r b: r:",
                            31: "d2 f d2",
                            33: "b:",
                            38: "u: l: b",
                            40: "d: r d",
                            42: "d l: d:",
                            44: "b d: r d",
                            49: "l2 u b2",
                            }

                self.cube.algorithm(move_map[self.cube.get_piece(53)])
            if self.cube.get_location(49) != 49:
                print("Fourth edge:")
                move_map = {2: "u: l2",
                            4: "l2",
                            6: "u2 l2",
                            8: "u l2",
                            11: "u: f: l f",
                            13: "d: b d",
                            15: "d f: d:",
                            17: "l: d f: d:",
                            20: "f: l f",
                            22: "l",
                            24: "d2 r: d2",
                            29: "u f: l f",
                            31: "d f d:",
                            33: "d: b: d",
                            38: "b l: b:",
                            40: "d2 r d2",
                            42: "l:",
                            }

                self.cube.algorithm(move_map[self.cube.get_piece(49)])
        print("Cross solved\n")

    def solve_first_layer_corners(self):
        if self.cube.get_location(46) != 46 or self.cube.get_location(48) != 48 or self.cube.get_location(52) != 52 \
        or self.cube.get_location(54) != 54:
            print("Solving the first layer corners:")
            if self.cube.get_location(48) != 48:
                print("First corner:")
                move_map = {1: "l u: l: r u r:",
                            3: "r: u r2 u: r:",
                            7: "u: r u2 r: u: r u r:",
                            9: "r u2 r: u: r u r:",
                            10: "u2 r u r:",
                            12: "r u: r:",
                            16: "l u l: u r u r:",
                            18: "l: u: l u r u: r:",
                            19: "u: r u r:",
                            21: "u r u: r:",
                            25: "l: u l u: r u r:",
                            27: "r u: r: u r u: r:",
                            28: "r u r:",
                            30: "u2 r u: r:",
                            34: "r u r: u: r u r:",
                            36: "r: u2 r2 u: r:",
                            37: "u r u r:",
                            39: "r u2 r:",
                            43: "r: u r u r u r:",
                            45: "l u: l: r u2 r:",
                            46: "l: u: l r u r:",
                            52: "l u: l: u2 r u r:",
                            54: "r: u2 r u: r u r:"
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(48)])
            if self.cube.get_location(54) != 54:
                print("Second corner:")
                move_map = {1: "l u: l: u r: u2 r",
                            3: "r: u2 r u r: u: r",
                            7: "l: u l r: u: r",
                            9: "u l: u l r: u: r",
                            10: "r: u r",
                            12: "u2 r: u: r",
                            16: "l u l: u: r: u r",
                            18: "l: u: l u: r: u: r",
                            19: "r: u2 r",
                            21: "u: r: u: r",
                            25: "l: u l r: u2 r",
                            28: "u r: u2 r",
                            30: "r: u: r",
                            36: "r: u: r u r: u: r",
                            37: "u: r: u r",
                            39: "u r: u: r",
                            43: "r: u r u: r: u r",
                            45: "l u: l: u r: u: r",
                            46: "l: u: l u r: u2 r",
                            52: "l u l: r: u: r",
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(54)])
            if self.cube.get_location(52) != 52:
                print("Third corner:")
                move_map = {1: "l u2 l: u: l u l:",
                            3: "u2 l: u l2 u: l:",
                            7: "l: u l2 u: l:",
                            9: "u l: u l2 u: l:",
                            10: "l u l:",
                            12: "u2 l u: l:",
                            16: "l u l: u: l u l:",
                            18: "l: u: l2 u2 l:",
                            19: "u l u l:",
                            21: "l u2 l:",
                            25: "l: u l u l u l:",
                            28: "u2 l u l:",
                            30: "l u: l:",
                            37: "u: l u l:",
                            39: "u l u: l:",
                            45: "l u: l: u l u: l:",
                            46: "l: u l u2 l u: l:",
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(52)])
            if self.cube.get_location(46) != 46:
                print("Fourth corner:")
                move_map = {1: "u: l: u2 l u l: u: l",
                            3: "u2 l: u2 l u l: u: l",
                            7: "l: u2 l u l: u: l",
                            9: "u l: u2 l u l: u: l",
                            10: "u2 l: u l",
                            12: "l: u: l",
                            18: "l: u: l u l: u: l",
                            19: "u: l: u l",
                            21: "u l: u: l",
                            25: "l: u l u: l: u l",
                            28: "l: u l",
                            30: "u2 l: u: l",
                            37: "l: u2 l",
                            39: "u: l: u: l",
                            }
                self.cube.algorithm(move_map[self.cube.get_piece(46)])
        print("First layer solved\n")

    def solve_second_layer(self):
        print("Solving second layer:")
        edges_of_concern = [24, 31, 40, 33, 42, 13, 22, 15]
        while self.cube.get_location(24) != 24 or self.cube.get_location(40) != 40 or \
        self.cube.get_location(42) != 42 or self.cube.get_location(22) != 22:
            for number in range(2, 10, 2):
                if self.cube.get_location(number) in edges_of_concern:
                    self.solve_edge(self.cube.get_location(number))
                    break
            else:
                if self.cube.get_location(24) != 24:
                    self.cube.algorithm("r u: r: u: f: u f")
                elif self.cube.get_location(22) != 22:
                    self.cube.algorithm("l: u l u f u: f:")
                elif self.cube.get_location(33) != 33:
                    self.cube.algorithm("b u: b: u: r: u r")
                else:
                    self.cube.algorithm("b: u2 b u2 l u l:")
        print("Second layer solved\n")


    def solve_edge(self, edge_num):
        if edge_num == 24 or edge_num == 31:
            move_map = {2: "f: u: f u r u r:",
                        4: "u f: u f u r u: r:",
                        6: "u: f: u f u r u: r:",
                        8: "f: u2 f u2 r u r:",
                        11: "r u r: u: f: u: f",
                        20: "u r u: r: u: f: u f",
                        29: "r u2 r: u2 f: u: f",
                        38: "u: r u: r: u: f: u f"
                        }
            self.cube.algorithm(move_map[self.cube.get_piece(24)])
            print("Front right edge solved")
        elif edge_num == 40 or edge_num == 33:
            move_map = {2: "b u2 b: u2 r: u: r",
                        4: "u: b u: b: u: r: u r",
                        6: "u b u: b: u: r: u r",
                        8: "b u: b: u: r: u r",
                        11: "r: u: r u b u b:",
                        20: "u r: u: r u b u b:",
                        29: "r: u2 r u2 b u b:",
                        38: "u: r: u r u b u: b:"
                        }
            self.cube.algorithm(move_map[self.cube.get_piece(40)])
            print("Back right edge solved")
        elif edge_num == 42 or edge_num == 13:
            move_map = {2: "b: u2 b u2 l u l:",
                        4: "u: b: u b u l u: l:",
                        6: "u b: u b u l u: l:",
                        8: "b: u: b u l u l:",
                        11: "l u2 l: u2 b: u: b",
                        20: "u: l u: l: u: b: u b",
                        29: "l u l: u: b: u: b",
                        38: "u l u: l: u: b: u b"
                        }
            self.cube.algorithm(move_map[self.cube.get_piece(42)])
            print("Back left edge solved")
        elif edge_num == 22 or edge_num == 15:
            move_map = {2: "f u f: u: l: u: l",
                        4: "u f u: f: u: l: u l",
                        6: "u: f u f: u: l: u: l",
                        8: "f u2 f: u2 l: u: l",
                        11: "l: u2 l u2 f u f:",
                        20: "u: l: u l u f u: f:",
                        29: "l: u: l u f u f:",
                        38: "u l: u: l u f u f:"
                        }
            self.cube.algorithm(move_map[self.cube.get_piece(22)])
            print("Front left edge solved")

    def solve_third_layer(self):
        if self.cube.color_at(2) != "white" or self.cube.color_at(4) != "white" \
        or self.cube.color_at(6) != "white" or self.cube.color_at(8) != "white":
            print("Orienting last layer cross:")
            if self.cube.color_at(2) == "white":
                if self.cube.color_at(4) == "white":
                    self.cube.algorithm("f u r u: r: f:")
                elif self.cube.color_at(6) == "white":
                    self.cube.algorithm("u: f u r u: r: f:")
                else:
                    self.cube.algorithm("u f r u r: u: f:")
            elif self.cube.color_at(8) == "white":
                if self.cube.color_at(4) == "white":
                    self.cube.algorithm("u f u r u: r: f:")
                else:
                    self.cube.algorithm("u2 f u r u: r: f:")
            elif self.cube.color_at(4) == "white":
                self.cube.algorithm("f r u r: u: f:")
            else:
                self.cube.algorithm("f r u r: u: f: u2 f u r u: r: f:")
            print("Last layer cross oriented\n")
        if self.cube.color_at(1) != "white" or self.cube.color_at(3) != "white" \
                or self.cube.color_at(7) != "white" or self.cube.color_at(9) != "white":
            print("Orienting last layer corners")
            while self.cube.color_at(1) != "white" or self.cube.color_at(3) != "white" \
                    or self.cube.color_at(7) != "white" or self.cube.color_at(9) != "white":
                if self.cube.color_at(9) != "white":
                    self.orient_corner("", 28)
                elif self.cube.color_at(3) != "white":
                    self.orient_corner("u ", 37)
                elif self.cube.color_at(7) != "white":
                    self.orient_corner("u: ", 19)
                else:
                    self.orient_corner("u2 ", 10)
            print("Last layer corners oriented\n")
        if self.cube.color_at(19) != self.cube.color_at(21) or self.cube.color_at(28) != self.cube.color_at(30):
            print("Permuting last layer corners:")
            if self.cube.color_at(19) == self.cube.color_at(21):
                self.cube.algorithm("u r u r: u: r: f r2 u: r: u: r u r: f:")
            elif self.cube.color_at(28) == self.cube.color_at(30):
                self.cube.algorithm("u2 r u r: u: r: f r2 u: r: u: r u r: f:")
            elif self.cube.color_at(37) == self.cube.color_at(39):
                self.cube.algorithm("u: r u r: u: r: f r2 u: r: u: r u r: f:")
            elif self.cube.color_at(10) == self.cube.color_at(12):
                self.cube.algorithm("r u r: u: r: f r2 u: r: u: r u r: f:")
            else:
                self.cube.algorithm("f r u: r: u: r u r: f: r u r: u: r: f r f:")
            print("Last layer corners permuted\n")
        if self.cube.color_at(19) != self.cube.color_at(20) or self.cube.color_at(28) != self.cube.color_at(29) \
                or self.cube.color_at(19) != self.cube.color_at(25):
            print("Permuting last layer edges:")
            if self.cube.color_at(19) != self.cube.color_at(20) or self.cube.color_at(28) != self.cube.color_at(29):
                if self.cube.color_at(19) == self.cube.color_at(20):
                    self.cube.u2()
                    print("U2 ", end="")
                elif self.cube.color_at(10) == self.cube.color_at(11):
                    self.cube.u()
                    print("U ", end="")
                elif self.cube.color_at(28) == self.cube.color_at(29):
                    self.cube.uprime()
                    print("U' ", end="")
                if self.cube.color_at(37) == self.cube.color_at(38):
                    if self.cube.color_at(19) == self.cube.color_at(29):
                        self.cube.algorithm("r2 u r u r: u: r: u: r: u r:")
                    else:
                        self.cube.algorithm("r u: r u r u r u: r: u: r2")
                elif self.cube.color_at(10) == self.cube.color_at(29):
                    self.cube.algorithm("r2 u2 r u2 r2 u2 r2 u2 r u2 r2")
                else:
                    if self.cube.color_at(12) != self.cube.color_at(20):
                        self.cube.u()
                        print("U ", end="")
                    self.cube.algorithm("r: u: r u: r u r u: r: u r u r2 u: r:")
            if self.cube.color_at(10) == self.cube.color_at(23):
                self.cube.algorithm("u:")
            elif self.cube.color_at(28) == self.cube.color_at(23):
                self.cube.algorithm("u")
            elif self.cube.color_at(37) == self.cube.color_at(23):
                self.cube.algorithm("u2")
            print("The last layer is permuted\n")


    def orient_corner(self, auf, corner):
        if self.cube.color_at(corner) == "white":
            self.cube.algorithm(auf + "r: d: r d r: d: r d")
        else:
            self.cube.algorithm(auf + "d: r: d r d: r: d r")

    def solve_cube(self):
        self.solve_cross()
        self.solve_first_layer_corners()
        self.solve_second_layer()
        self.solve_third_layer()





if __name__ == "__main__":
    cube = Solver()
    cube.solve_cross()
    cube.solve_first_layer_corners()
    cube.solve_second_layer()
    cube.solve_third_layer()
    print("The cube is solved!!!!")