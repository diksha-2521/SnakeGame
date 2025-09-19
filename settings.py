import tkinter as tk

class GameSettings:
    def __init__(self):
        self.has_walls = False
        self.game_is_on = False
    def get_game_mode(self):
        """Opens a small window to ask for gameplay settings."""
        def set_walls():
            self.has_walls = True
            self.game_is_on = True
            root.destroy()
            print(self.game_is_on)

        def set_no_walls():
            self.has_walls = False
            self.game_is_on = True
            root.destroy()


        root = tk.Tk()
        root.title("Snake Game - Settings")
        root.geometry("300x150")
        root.configure(bg="black")

        label = tk.Label(root, text="Choose Game Mode:", font=("Courier", 12), fg="white", bg="black")
        label.pack(pady=15)

        button1 = tk.Button(root, text="Walls", font=("Courier", 12), width=12, command=set_walls)
        button1.pack(pady=5)

        button2 = tk.Button(root, text="Infinite", font=("Courier", 12), width=12, command=set_no_walls)
        button2.pack(pady=5)


        root.mainloop()
        return self.game_is_on, self.has_walls