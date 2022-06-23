class Cube:
    def __init__(self, white, orange, green, red, blue, yellow):
        self.white = white
        self.orange = orange
        self.green = green
        self.red = red
        self.blue = blue
        self.yellow = yellow

        if len(white) != 9 or len(orange) != 9 or len(green) != 9 or len(red) != 9 or len(blue) != 9 or len(yellow) != 9:
            raise Exception("Every side must have 9 colors.")

        if white[4] != "w" or orange[4] != "o" or green[4] != "g" or red[4] != "r" or blue[4] != "b" or yellow[4] != "y":
            raise Exception("The center of every side must be its own color.")

        self.key_map = {"wbo": 1,
                   "wb": 2,
                   "wrb": 3,
                   "wo": 4,
                   "w": 5,
                   "wr": 6,
                   "wog": 7,
                   "wg": 8,
                   "wgr": 9,
                   "owb": 10,
                   "ow": 11,
                   "ogw": 12,
                   "ob": 13,
                   "o": 14,
                   "og": 15,
                   "oby": 16,
                   "oy": 17,
                   "oyg": 18,
                   "gwo": 19,
                   "gw": 20,
                   "grw": 21,
                   "go": 22,
                   "g": 23,
                   "gr": 24,
                   "goy": 25,
                   "gy": 26,
                   "gyr": 27,
                   "rwg": 28,
                   "rw": 29,
                   "rbw": 30,
                   "rg": 31,
                   "r": 32,
                   "rb": 33,
                   "rgy": 34,
                   "ry": 35,
                   "ryb": 36,
                   "bwr": 37,
                   "bw": 38,
                   "bow": 39,
                   "br": 40,
                   "b": 41,
                   "bo": 42,
                   "bry": 43,
                   "by": 44,
                   "byo": 45,
                   "ygo": 46,
                   "yg": 47,
                   "yrg": 48,
                   "yo": 49,
                   "y": 50,
                   "yr": 51,
                   "yob": 52,
                   "yb": 53,
                   "ybr": 54
                   }
        self.location_map = {1 : self.key_map[white[0] + blue[2] + orange[0]],
                        2 : self.key_map.pop(white[1] + blue[1]),
                        3: self.key_map.pop(white[2] + red[2] + blue[0]),
                        4: self.key_map.pop(white[3] + orange[1]),
                        5: self.key_map.pop(white[4]),
                        6: self.key_map.pop(white[5] + red[1]),
                        7: self.key_map.pop(white[6] + orange[2] + green[0]),
                        8: self.key_map.pop(white[7] + green[1]),
                        9: self.key_map.pop(white[8] + green[2] + red[0]),
                        10: self.key_map.pop(orange[0] + white[0] + blue[2]),
                        11: self.key_map.pop(orange[1] + white[3]),
                        12: self.key_map.pop(orange[2] + green[0] + white[6]),
                        13: self.key_map.pop(orange[3] + blue[5]),
                        14: self.key_map.pop(orange[4]),
                        15: self.key_map.pop(orange[5] + green[3]),
                        16: self.key_map.pop(orange[6] + blue[8] + yellow[6]),
                        17: self.key_map.pop(orange[7] + yellow[3]),
                        18: self.key_map.pop(orange[8] + yellow[0] + green[6]),
                        19: self.key_map.pop(green[0] + white[6] + orange[2]),
                        20: self.key_map.pop(green[1] + white[7]),
                        21: self.key_map.pop(green[2] + red[0] + white[8]),
                        22: self.key_map.pop(green[3] + orange[5]),
                        23: self.key_map.pop(green[4]),
                        24: self.key_map.pop(green[5] + red[3]),
                        25: self.key_map.pop(green[6] + orange[8] + yellow[0]),
                        26: self.key_map.pop(green[7] + yellow[1]),
                        27: self.key_map.pop(green[8] + yellow[2] + red[6]),
                        28: self.key_map.pop(red[0] + white[8] + green[2]),
                        29: self.key_map.pop(red[1] + white[5]),
                        30: self.key_map.pop(red[2] + blue[0] + white[2]),
                        31: self.key_map.pop(red[3] + green[5]),
                        32: self.key_map.pop(red[4]),
                        33: self.key_map.pop(red[5] + blue[3]),
                        34: self.key_map.pop(red[6] + green[8] + yellow[2]),
                        35: self.key_map.pop(red[7] + yellow[5]),
                        36: self.key_map.pop(red[8] + yellow[8] + blue[6]),
                        37: self.key_map.pop(blue[0] + white[2] + red[2]),
                        38: self.key_map.pop(blue[1] + white[1]),
                        39: self.key_map.pop(blue[2] + orange[0] + white[0]),
                        40: self.key_map.pop(blue[3] + red[5]),
                        41: self.key_map.pop(blue[4]),
                        42: self.key_map.pop(blue[5] + orange[3]),
                        43: self.key_map.pop(blue[6] + red[8] + yellow[8]),
                        44: self.key_map.pop(blue[7] + yellow[7]),
                        45: self.key_map.pop(blue[8] + yellow[6] + orange[6]),
                        46: self.key_map.pop(yellow[0] + green[6] + orange[8]),
                        47: self.key_map.pop(yellow[1] + green[7]),
                        48: self.key_map.pop(yellow[2] + red[6] + green[8]),
                        49: self.key_map.pop(yellow[3] + orange[7]),
                        50: self.key_map.pop(yellow[4]),
                        51: self.key_map.pop(yellow[5] + red[7]),
                        52: self.key_map.pop(yellow[6] + orange[6] + blue[8]),
                        53: self.key_map.pop(yellow[7] + blue[7]),
                        54: self.key_map.pop(yellow[8] + blue[6] + red[8])
                        }

        self.piece_map = {v: k for k, v in self.location_map.items()}


    def get_location(self, location_num):
        return self.location_map[location_num]

    def get_piece(self, piece_num):
        return self.piece_map[piece_num]

    def move(self, piece, new_location):
        self.location_map[new_location] = piece
        self.piece_map[piece] = new_location

    def rotate(self, number):
        """The number should be the first number of the side to rotate minus one."""
        temp = self.get_location(1 + number)
        self.move(self.get_location(7 + number), 1 + number)
        self.move(self.get_location(9 + number), 7 + number)
        self.move(self.get_location(3 + number), 9 + number)
        self.move(temp, 3 + number)
        temp = self.get_location(2 + number)
        self.move(self.get_location(4 + number), 2 + number)
        self.move(self.get_location(8 + number), 4 + number)
        self.move(self.get_location(6 + number), 8 + number)
        self.move(temp, 6 + number)

    def u(self):
        self.rotate(0)
        temp = self.get_location(19)
        self.move(self.get_location(28), 19)
        self.move(self.get_location(37), 28)
        self.move(self.get_location(10), 37)
        self.move(temp, 10)

        temp = self.get_location(21)
        self.move(self.get_location(30), 21)
        self.move(self.get_location(39), 30)
        self.move(self.get_location(12), 39)
        self.move(temp, 12)

        temp = self.get_location(20)
        self.move(self.get_location(29), 20)
        self.move(self.get_location(38), 29)
        self.move(self.get_location(11), 38)
        self.move(temp, 11)

    def u2(self):
        self.u()
        self.u()

    def uprime(self):
        self.u2()
        self.u()

    def r(self):
        self.rotate(27)
        temp = self.get_location(21)
        self.move(self.get_location(48), 21)
        self.move(self.get_location(43), 48)
        self.move(self.get_location(3), 43)
        self.move(temp, 3)

        temp = self.get_location(27)
        self.move(self.get_location(54), 27)
        self.move(self.get_location(37), 54)
        self.move(self.get_location(9), 37)
        self.move(temp, 9)

        temp = self.get_location(24)
        self.move(self.get_location(51), 24)
        self.move(self.get_location(40), 51)
        self.move(self.get_location(6), 40)
        self.move(temp, 6)

    def r2(self):
        self.r()
        self.r()

    def rprime(self):
        self.r2()
        self.r()

    def l(self):
        self.rotate(9)
        temp = self.get_location(19)
        self.move(self.get_location(1), 19)
        self.move(self.get_location(45), 1)
        self.move(self.get_location(46), 45)
        self.move(temp, 46)

        temp = self.get_location(25)
        self.move(self.get_location(7), 25)
        self.move(self.get_location(39), 7)
        self.move(self.get_location(52), 39)
        self.move(temp, 52)

        temp = self.get_location(22)
        self.move(self.get_location(4), 22)
        self.move(self.get_location(42), 4)
        self.move(self.get_location(49), 42)
        self.move(temp, 49)

    def l2(self):
        self.l()
        self.l()

    def lprime(self):
        self.l2()
        self.l()

    def d(self):
        self.rotate(45)
        temp = self.get_location(25)
        self.move(self.get_location(16), 25)
        self.move(self.get_location(43), 16)
        self.move(self.get_location(34), 43)
        self.move(temp, 34)

        temp = self.get_location(27)
        self.move(self.get_location(18), 27)
        self.move(self.get_location(45), 18)
        self.move(self.get_location(36), 45)
        self.move(temp, 36)

        temp = self.get_location(26)
        self.move(self.get_location(17), 26)
        self.move(self.get_location(44), 17)
        self.move(self.get_location(35), 44)
        self.move(temp, 35)

    def d2(self):
        self.d()
        self.d()

    def dprime(self):
        self.d2()
        self.d()

    def f(self):
        self.rotate(18)
        temp = self.get_location(7)
        self.move(self.get_location(18), 7)
        self.move(self.get_location(48), 18)
        self.move(self.get_location(28), 48)
        self.move(temp, 28)

        temp = self.get_location(8)
        self.move(self.get_location(15), 8)
        self.move(self.get_location(47), 15)
        self.move(self.get_location(31), 47)
        self.move(temp, 31)

        temp = self.get_location(9)
        self.move(self.get_location(12), 9)
        self.move(self.get_location(46), 12)
        self.move(self.get_location(34), 46)
        self.move(temp, 34)

    def f2(self):
        self.f()
        self.f()

    def fprime(self):
        self.f2()
        self.f()

    def b(self):
        self.rotate(36)
        temp = self.get_location(3)
        self.move(self.get_location(36), 3)
        self.move(self.get_location(52), 36)
        self.move(self.get_location(10), 52)
        self.move(temp, 10)

        temp = self.get_location(2)
        self.move(self.get_location(33), 2)
        self.move(self.get_location(53), 33)
        self.move(self.get_location(13), 53)
        self.move(temp, 13)

        temp = self.get_location(1)
        self.move(self.get_location(30), 1)
        self.move(self.get_location(54), 30)
        self.move(self.get_location(16), 54)
        self.move(temp, 16)


    def b2(self):
        self.b()
        self.b()

    def bprime(self):
        self.b2()
        self.b()

    def color_at(self, number):
        piece = self.get_location(number)
        if piece in range(1, 10):
            return "white"
        elif piece in range(10, 19):
            return "orange"
        elif piece in range(19, 28):
            return "green"
        elif piece in range(28, 37):
            return "red"
        elif piece in range(37, 46):
            return "blue"
        else:
            return "yellow"

    def algorithm(self, sequence):
        print(sequence.replace(":", "\'").upper())
        moves = sequence.split()
        for move in moves:
            if move == "u":
                self.u()
            elif move == "u:":
                self.uprime()
            elif move == "u2":
                self.u2()
            elif move == "r":
                self.r()
            elif move == "r:":
                self.rprime()
            elif move == "r2":
                self.r2()
            elif move == "l":
                self.l()
            elif move == "l:":
                self.lprime()
            elif move == "l2":
                self.l2()
            elif move == "d":
                self.d()
            elif move == "d:":
                self.dprime()
            elif move == "d2":
                self.d2()
            elif move == "f":
                self.f()
            elif move == "f:":
                self.fprime()
            elif move == "f2":
                self.f2()
            elif move == "b":
                self.b()
            elif move == "b:":
                self.bprime()
            elif move == "b2":
                self.b2()

    def is_solved(self):
        for number in range(1, 55):
            if self.get_location(number) != number:
                return False
        return True

    def corners_solvable(self):
        odd_or_even_counter = 0
        for number in range(10, 38, 9):
            if self.color_at(number) == "yellow" or self.color_at(number) == "white":
                odd_or_even_counter = odd_or_even_counter - 1
        for number in range(12, 40, 9):
            if self.color_at(number) == "yellow" or self.color_at(number) == "white":
                odd_or_even_counter = odd_or_even_counter + 1
        for number in range(16, 44, 9):
            if self.color_at(number) == "yellow" or self.color_at(number) == "white":
                odd_or_even_counter = odd_or_even_counter + 1
        for number in range(18, 46, 9):
            if self.color_at(number) == "yellow" or self.color_at(number) == "white":
                odd_or_even_counter = odd_or_even_counter - 1
        return odd_or_even_counter % 3 == 0

    def edges_solvable(self):
        good_edges = 0
        main_color = [2, 4, 6, 8, 22, 24, 40, 42, 47, 49, 51, 53]
        other_color = [38, 11, 29, 20, 15, 31, 33, 13, 26, 17, 35, 44]
        for number in range(0, 12):
            if self.color_at(main_color[number]) == "yellow" or \
                    self.color_at(main_color[number]) == "white":
                good_edges = good_edges + 1
            elif (self.color_at(main_color[number]) == "green" or
                  self.color_at(main_color[number]) == "blue") and \
                    (self.color_at(other_color[number]) != "yellow" and
                     self.color_at(other_color[number]) != "white"):
                good_edges = good_edges + 1
        return good_edges % 2 == 0

    def pieces_permutable(self):
        main_color = [4, 6, 8, 22, 24, 40, 42, 47, 49, 51, 53]
        other_color = [11, 29, 20, 15, 31, 33, 13, 26, 17, 35, 44]
        for number in reversed(main_color):
            if self.get_location(number) == number:
                index = main_color.index(number)
                main_color.pop(index)
                other_color.pop(index)
        edges = self.edge_helper(main_color, other_color, 0, self.get_location(2))

        main_color = [3, 7, 9, 54, 46, 48, 52]
        other_color = [30, 12, 21, 43, 25, 34, 16]
        final_color = [37, 19, 28, 36, 18, 27, 45]
        for number in reversed(main_color):
            if self.get_location(number) == number:
                index = main_color.index(number)
                main_color.pop(index)
                other_color.pop(index)
                final_color.pop(index)
        corners = self.corner_helper(main_color, other_color, final_color, 0, self.get_location(1))
        return (edges + corners) % 2 == 0

    def edge_helper(self, main_list, other_list, swaps, current_piece):
        if current_piece != 2 and current_piece != 38 and len(main_list) != 0 and (current_piece in main_list or current_piece in other_list):
            try:
                index = main_list.index(current_piece)
            except ValueError:
                index = other_list.index(current_piece)
            main_list.pop(index)
            other_list.pop(index)
            current_piece = self.get_location(current_piece)
            return self.edge_helper(main_list, other_list, swaps + 1, current_piece)
        elif len(main_list) != 0:
            current_piece = self.get_location(main_list[0])
            return self.edge_helper(main_list, other_list, swaps + 1, current_piece)
        else:
            return swaps

    def corner_helper(self, main_list, other_list, final_list, swaps, current_piece):
        if current_piece != 1 and current_piece != 39 and current_piece != 10 and len(main_list) != 0:
            try:
                index = main_list.index(current_piece)
            except ValueError:
                try:
                    index = other_list.index(current_piece)
                except ValueError:
                    index = final_list.index(current_piece)
            main_list.pop(index)
            other_list.pop(index)
            final_list.pop(index)
            current_piece = self.get_location(current_piece)
            return self.corner_helper(main_list, other_list, final_list, swaps + 1, current_piece)
        elif len(main_list) != 0:
            current_piece = self.get_location(main_list[0])
            return self.corner_helper(main_list, other_list, final_list, swaps + 1, current_piece)
        else:
            return swaps

    def solvable(self):
        if not self.corners_solvable():
            raise Exception("Corners have an odd orientation.")
        if not self.edges_solvable():
            raise Exception("Edges have an odd orientation.")
        if not self.pieces_permutable():
            raise Exception("Pieces have an odd permutation.")
