from board import Board
from player import Player
from computer import Computer


def print_tic_tac_toe():
    logo = """
 _|_|_|_|_|   _|_|_|     _|_|_|       _|_|_|_|_|     _|_|       _|_|_|       _|_|_|_|_|     _|_|     _|_|_|_|  
     _|         _|     _|                 _|       _|    _|   _|                 _|       _|    _|   _|        
     _|         _|     _|                 _|       _|_|_|_|   _|                 _|       _|    _|   _|_|_|    
     _|         _|     _|                 _|       _|    _|   _|                 _|       _|    _|   _|        
     _|       _|_|_|     _|_|_|           _|       _|    _|     _|_|_|           _|         _|_|     _|_|_|_|
    """
    print(logo)


def show_menu():
    print("\n\nMenu:")
    print("-" * 40)
    print("\t1 - Start game")
    print("\t2 - Game rules")
    print("\t3 - Set player symbols")
    print("\t4 - Exit")
    print("_" * 40)


def show_game_rules():
    print("\n\n" + "-" * 40)
    print("Rules:\n")
    print("\t1. Each player takes turns to place their symbol on an empty space on the board.\n")
    print("\t2. The first player to get three of their symbols in a row, column, or diagonal wins the game.\n")
    print("\t3. Each player can have a maximum of 3 symbols on the board. With each subsequent move, the earliest\n"
          "\t   placed symbol is removed. The disappearing symbol is underlined, and the player cannot place their symbol\n"
          "\t   in the same position in the turn when it disappears. However, in the next turns, the position becomes\n"
          "\t   available for placing symbols.\n")
    print("Controls:\n")
    print("\tThe board is a 3x3 grid, where positions are specified using numbers such as 11, 12, 13, 21, 22, 23, 31, "
          "32, 33.")
    print("\tThe first digit indicates the row number, and the second digit indicates the column number.")
    print("-" * 40)



def get_user_input(choices):
    min_choice = min(choices)
    max_choice = max(choices)
    while True:
        user_input = input(f"Choose an option ({min_choice}-{max_choice}): ")
        if user_input in choices:
            return user_input
        print("Invalid input.")


def set_player_symbol(other_symbol):
    while True:
        symbol = input("Set symbol (only one character): ")
        if len(symbol) == 1 and symbol != other_symbol:
            return symbol
        print("Invalid input. Make sure the symbol is one character and not the same as the other player's symbol.")


def start_game(board):
    def player_vs_computer():
        computer = Computer(board.symbol[1], board)
        player = Player(0, board)

        print("\n\n" + "-" * 40)
        print("Do you want to start the game or play second?")
        print("\t1 - Start")
        print("\t2 - Play Second")
        print("_" * 40)
        starting_choice = get_user_input(["1", "2"])

        starting_player = player if starting_choice == '1' else computer
        alternate_turns(player, computer, starting_player)

    def player_vs_player():
        player1 = Player(0, board)
        player2 = Player(1, board)
        alternate_turns(player1, player2, player1)

    def alternate_turns(player1, player2, starting_player):
        current_player = starting_player
        while True:
            if current_player.__class__.__name__ == "Player":
                board.show_board(current_player.player_index)
            current_player.make_move()
            if board.check_winner(current_player.symbol):
                board.show_board(0)
                winner = "Player 1" if current_player == player1 else \
                    ("Player 2" if current_player.__class__.__name__ == "Player" else "Computer")
                print(winner, "wins!")
                break
            current_player = player2 if current_player == player1 else player1

    while True:
        board.reset_board()
        print("\n\n" + "-" * 40)
        print("\t1 - Player vs Computer")
        print("\t2 - Player vs Player")
        print("\t3 - Back to menu")
        print("_" * 40)
        choice = get_user_input(["1", "2", "3"])

        if choice == '1':
            player_vs_computer()
        elif choice == '2':
            player_vs_player()
        elif choice == '3':
            break


def set_player_symbols(board):
    while True:
        print("\n\n" + "-" * 40)
        print(f"\t1 - First player (current symbol: {board.symbol[0]})")
        print(f"\t2 - Second player/Computer (current symbol: {board.symbol[1]})")
        print("\t3 - Back to menu")
        print("_" * 40)
        choice = get_user_input(["1", "2", "3"])
        if choice == '1':
            board.symbol[0] = set_player_symbol(board.symbol[1])
        elif choice == '2':
            board.symbol[1] = set_player_symbol(board.symbol[0])
        elif choice == '3':
            break


def main():
    print_tic_tac_toe()
    menu = True
    board = Board()

    while menu:
        show_menu()
        choice = get_user_input(["1", "2", "3", "4"])

        if choice == '1':
            start_game(board)
        elif choice == '2':
            show_game_rules()
        elif choice == '3':
            set_player_symbols(board)
        elif choice == '4':
            print("Exiting the game.")
            menu = False


if __name__ == "__main__":
    main()
