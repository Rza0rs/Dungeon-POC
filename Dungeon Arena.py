class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


class Game(object):

    MARKER_X = "X"
    MARKER_O = "O"
    CTRLS = [
        "left",
        None,
        "right",
        "up",
        None,
        "down",
    ]
    EXIT = "stop"
    START = [0, 0]
    DEFAULT = [["O"] * 6 for _ in range(6)]

    def __init__(self):
        self.flag = True
        self.arena = Board(Game.DEFAULT)
        self.curr_pos = Game.START[:]
        self.prev_pos = Game.START[:]
        self.move_player()

    def move_player(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (0 <= cx <= 3) and (0 <= cy <= 5):
            self.arena[py][px] = Game.MARKER_O
            self.arena[cy][cx] = Game.MARKER_X

        else:
            print("Please enter a proper direction.")
            self.curr_pos = self.prev_pos[:]
            self.move_player()
    def play(self):

        print("You are at 0,0")
        while self.flag:
            ctrl = input("Move left, right, up, down, or stop?").lower()
            if ctrl in Game.CTRLS:
                d = Game.CTRLS.index(ctrl)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
                self.move_player()
                print(self.curr_pos)
                if self.curr_pos == [1, 0]:
                  while self.flag:
                    print("You walk face first into a wall, and turn back to the center of the room")
                    self.curr_pos = self.prev_pos[:]
                    self.move_player()
                    print(self.curr_pos)
                    break
                elif self.curr_pos == [1, 1]:
                    while self.flag:
                        print("You walk face first into a wall, and turn back to the center of the room")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        print(self.curr_pos)
                        break
                elif self.curr_pos == [2, 2]:
                    while self.flag:
                        print("Congratulations! You made it out of the dungeon!,"
                              "Get Ready for the full product, THULE, coming soon!")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        self.flag = False

                        break
                elif self.curr_pos == [3, 1]:
                    while self.flag:
                        print("You walk face first into a wall, and turn back to the center of the room")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        print(self.curr_pos)
                        break
                elif self.curr_pos == [3, 2]:
                    while self.flag:
                        print("You almost slip and fall into a chasm,"
                              "You catch yourself and return to the center of the room")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        print(self.curr_pos)
                        break
                elif self.curr_pos == [1, 5]:
                    while self.flag:
                        print("Wishing to be one with the waterfall,"
                              "you almost walk off the edge of the platform,"
                              "you regain your senses and return to the center of the room")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        print(self.curr_pos)
                        break
                elif self.curr_pos == [0, 5]:
                    while self.flag:
                        print("Amazed by the gorgeous waterfall,"
                              "you almost walk off the platform you were standing on,"
                              "you catch yourself and return to the center of the room ")
                        self.curr_pos = self.prev_pos[:]
                        self.move_player()
                        print(self.curr_pos)
                        break
            elif ctrl == Game.EXIT:
                self.flag = False
            else:
                print("Please enter a proper direction.")

my_game = Game()
my_game.play()
