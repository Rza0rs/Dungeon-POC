def play(self):
    print("You are: \nX")
    while self.flag:
        print(str(self.arena))
        ctrl = input("Move left, right, up, down, or stop?").lower()
        if ctrl in Game.CTRLS:
            d = Game.CTRLS.index(ctrl)
            self.prev_pos = self.curr_pos[:]
            self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
            self.move_player()
        elif ctrl == Game.EXIT:
            self.flag = False
        else:
            print("Please enter a proper direction.")

my_game.play()