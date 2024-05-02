class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'  # 'X' starts the game

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, position):
        if self.board[position] == ' ':  # Check if the position is empty
            self.board[position] = self.current_player
            if self.check_winner():
                print(f'Player {self.current_player} wins!')
                return True
            elif ' ' not in self.board:
                print('It\'s a draw!')
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
        else:
            print('That position is already taken. Try again.')
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Here's the board layout:")
        self.print_board()
        print("Each cell is represented by its position number (0-8) starting from top-left.")

        while True:
            try:
                position = int(input(f'Player {self.current_player}, enter your move (0-8): '))
                if position < 0 or position > 8:
                    raise ValueError
                if self.make_move(position):
                    break
                self.print_board()
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
