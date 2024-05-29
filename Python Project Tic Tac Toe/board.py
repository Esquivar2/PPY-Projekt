class Board:
    def __init__(self):
        self.board_state = [[" "] * 3 for _ in range(3)]
        self.move_history = [[], []]
        self.symbol = ["O", "X"]
        self.underline = '\033[4m'
        self.end = '\033[0m'

    def show_board(self, player_index):

        if len(self.move_history[player_index]) == 3:
            self.board_state[self.move_history[player_index][0] // 10 - 1][self.move_history[player_index][0] % 10 - 1] = self.underline + self.symbol[player_index] + self.end

        print("┌───────────┐")
        for row in range(3):
            print("| " +  self.board_state[row][0] + " | " +  self.board_state[row][1] + " | " +  self.board_state[row][2] + " |")
        print("└───────────┘")

        if len(self.move_history[player_index]) == 3:
            self.board_state[self.move_history[player_index][0] // 10 - 1][self.move_history[player_index][0] % 10 - 1] = self.symbol[player_index]

    def reset_board(self):
        self.board_state = [[" "] * 3 for _ in range(3)]
        self.move_history = [[], []]


    def check_winner(self, last_player_move_symbol):
        for i in range(3):
            if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] == last_player_move_symbol:
                return True
            if self.board_state[i][0] == self.board_state[i][1] == self.board_state[i][2] == last_player_move_symbol:
                return True

        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] == last_player_move_symbol:
            return True
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] == last_player_move_symbol:
            return True
        return False
