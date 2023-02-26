import tkinter as tk
from Game import Game

if __name__ == "__main__":
    # window settings
    root = tk.Tk()
    root.title('Snake the game')
    root.geometry("600x600+600+200")
    root.resizable(False, False)
    root.configure(bg='black')

    canvas = tk.Canvas(root, width=600, height=600, bg='black')
    canvas.pack()

    game = Game(canvas, root)

    root.mainloop()
