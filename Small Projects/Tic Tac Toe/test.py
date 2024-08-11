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
        Welcome to Tic Tac Toe!
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
        self.board = [str(i) for i in range(1, 10)]
    
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
        for player in self.players:
            player.choose_name()
            player.choose_symbol()
    
    def play_game(self):
        pass

    def quit_game(self):
        pass


game = Game()
game.start_game()

