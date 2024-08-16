import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") 
    # cls for Windows and clear for Linux and Mac

class Player():
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, Enter your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol.")
    
class Menu():
    def display_main_menu(self):
        menu_text = """
        Welcome to Tic Tac Toe!
        1. Start Game
        2. Quit Game
        Enter your choice (1 or 2): """
        return self.validate_choice(menu_text)
    
    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        return self.validate_choice(menu_text)

    def validate_choice(self, menu_text):
        while True:
            choice = input(menu_text)
            if choice == "1" or choice == "2":
                return choice
            print("Invalid choice.")
    
class Board():
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]  # ["1","2","3","4","5","6","7","8","9"]
    
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-"*5)
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True 
        return False
    
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game():
    def __init__(self):
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for number, player in enumerate(self.players, start = 1):
            clear_screen()
            print(f"Player {number}, Enter your details:")
            player.choose_name()
            player.choose_symbol()
            
    def play_game(self):
        while True:
            clear_screen()
            self.play_turn()
            if self.check_win() or self.check_draw():
                clear_screen()
                self.board.display_board()
                if(self.check_win()):
                    print(f"Congratulations, {self.players[self.current_player_index].name} won!")
                else:
                    print("Draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            self.switch_player()
    
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice,player.symbol):
                    break
                else:
                    print("Invalid move.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    def check_win(self):
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],   # rows
            [0,3,6], [1,4,7], [2,5,8],   # columns
            [0,4,8], [2,4,6]             # diagonals
        ]
        for combo in win_combinations:
            if(self.board.board[combo[0]]==self.board.board[combo[1]]==self.board.board[combo[2]]):
                return True 
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thank you for Playing!")

game = Game()
game.start_game()
