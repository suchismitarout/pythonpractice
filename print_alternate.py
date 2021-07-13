class Member:
    ..

class King(Member):
    ...
    def move(self):
        ..

class MemberFactory():


class ChessBoard:
        def init_members(self...):

        def change(self, member, ):
            member.move()
            board ...

class Game:
    def __init__(self):
        self.chess_board = ChessBoard(8)
        self.chess_board.init_members()

    def start(self, start_time,....):
        a = Player(1, "white")
        b = Player(2, "black")
        is_over = False
        first_player_turn = True
        while(True):
            if first_player_turn:
                a.play(..,...)
                first_player_turn = False
            else:
                b.play(..,..)
                first_player_turn = True

            if is_over:
                print("game over...")
                break




g = Game()
g.start()