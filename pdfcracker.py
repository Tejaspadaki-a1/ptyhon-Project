import tkinter as tk

class ChessBoardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("600x600")  # Set window size

        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()

        self.background_image = tk.PhotoImage(file="chessboard_background.png")  # Replace with your image path
        self.canvas.create_image(300, 300, image=self.background_image)

        self.piece_images = {}  # Dictionary to store images for pieces
        self.load_piece_images()  # Load piece images

        # Example: Place a white pawn on the board
        self.place_piece("wp", 6, 0)

    def load_piece_images(self):
        # Load images for each piece
        # Example: self.piece_images["wp"] = tk.PhotoImage(file="white_pawn.png")
        pass  # Replace with your image loading code

    def place_piece(self, piece, row, col):
        # Place a piece on the board
        x = col * 75 + 37.5  # Adjust position based on square size
        y = row * 75 + 37.5
        self.canvas.create_image(x, y, image=self.piece_images[piece], anchor="c")

if __name__ == "__main__":
    app = ChessBoardGUI()
    app.mainloop()
