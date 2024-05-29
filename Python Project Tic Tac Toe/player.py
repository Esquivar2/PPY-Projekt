class Player:
    def __init__(self, player_index, board):
        self.player_index = player_index
        self.symbol = board.symbol[player_index]
        self.board = board

    def make_move(self):
        possible_moves = {f"{row}{col}" for row in range(1, 4) for col in range(1, 4)}
        while True:
            move = input("Enter your move: ")
            if move in possible_moves:
                move = int(move)
                if self.board.board_state[move // 10 - 1][move % 10 - 1] == " ":
                    self.board.board_state[move // 10 - 1][move % 10 - 1] = self.symbol
                    self.board.move_history[self.player_index].append(move)
                    break
                else:
                    print("This position is already occupied.")
            else:
                print("Wrong move. Try again.")

        if len(self.board.move_history[self.player_index]) > 3:
            self.board.board_state[self.board.move_history[self.player_index][0] // 10 - 1][self.board.move_history[self.player_index][0] % 10 - 1] = " "
            self.board.move_history[self.player_index].pop(0)
