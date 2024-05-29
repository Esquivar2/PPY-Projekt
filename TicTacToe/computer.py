import random


class Computer:

    def __init__(self, symbol, board):
        self.symbol = symbol
        self.board = board

    def make_move(self):

        if len(self.board.move_history[1]) > 2:
            self._block_oldest_move(self.board.move_history[1])

        # sprawdza, czy moze wygrac w kolejnym ruchu
        if self._try_to_win():
            return

        if len(self.board.move_history[0]) > 2:
            self._block_opponent_oldest_move()

        # sprawdza, czy przeciwnik moze wygrac w kolejnym ruchu, jezeli tak, to tam wykonuje swoj ruch
        if self._block_opponent_win():
            return

        if len(self.board.move_history[0]) > 2:
            self._unblock_opponent_oldest_move()

        # po 3 ruchu sprawdza, czy srodkowe pole jest puste, jak tak to tam wykonuje swoj ruch
        if len(self.board.move_history[1]) > 2:
            if self.board.board_state[1][1] == ' ':
                self._move_to_center()
                return

        # wykonuje losowe posuniecie
        self._make_random_move()

    def _block_oldest_move(self, move_history):
        self.board.board_state[move_history[0] // 10][move_history[0] % 10] = "blocked"

    def _unblock_oldest_move(self, move_history):
        self.board.board_state[move_history[0] // 10][move_history[0] % 10] = " "
        move_history.pop(0)

    def _block_opponent_oldest_move(self):
        self.board.board_state[self.board.move_history[0][0] // 10 - 1][
            self.board.move_history[0][0] % 10 - 1] = "blocked"

    def _unblock_opponent_oldest_move(self):
        self.board.board_state[self.board.move_history[0][0] // 10 - 1][self.board.move_history[0][0] % 10 - 1] = \
            self.board.symbol[0]

    def _save_move(self, i, j, move_history):
        if len(move_history) > 2:
            self._unblock_oldest_move(move_history)
        move_history.append(i * 10 + j)

    def _try_to_win(self):
        for i in range(3):
            for j in range(3):
                if self.board.board_state[i][j] == ' ':
                    self.board.board_state[i][j] = self.symbol
                    if self.board.check_winner(self.symbol):
                        self._save_move(i, j, self.board.move_history[1])
                        return True
                    self.board.board_state[i][j] = ' '
        return False

    def _block_opponent_win(self):
        for i in range(3):
            for j in range(3):
                if self.board.board_state[i][j] == ' ':
                    self.board.board_state[i][j] = self.board.symbol[0]
                    if self.board.check_winner(self.board.symbol[0]):
                        self.board.board_state[i][j] = self.symbol
                        self._save_move(i, j, self.board.move_history[1])
                        if len(self.board.move_history[0]) > 2:
                            self._unblock_opponent_oldest_move()
                        return True
                    self.board.board_state[i][j] = ' '
        return False

    def _move_to_center(self):
        self.board.board_state[1][1] = self.symbol
        self._unblock_oldest_move(self.board.move_history[1])
        self.board.move_history[1].append(11)

    def _make_random_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board.board_state[i][j] == ' ']
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board.board_state[i][j] = self.symbol
            self._save_move(i, j, self.board.move_history[1])
