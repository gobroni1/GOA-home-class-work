import tkinter as tk
import keyboard
import threading

class OnScreenKeyboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("On-Screen Keyboard")
        self.geometry("1200x400")
        self.keys = [
            ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['CapsLock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Menu', 'Ctrl']
        ]
        self.buttons = {}
        self.create_keyboard()

        # Bind key press and release events
        for key in self.buttons.keys():
            keyboard.on_press_key(key.lower(), self.on_key_press)
            keyboard.on_release_key(key.lower(), self.on_key_release)

    def create_keyboard(self):
        key_positions = [
            [(0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13)],  # Function keys
            [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13)],  # Number row
            [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13)],  # QWERTY row
            [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12)],  # ASDF row
            [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11)],  # ZXCV row
            [(5, 0), (5, 1), (5, 2), (5, 4), (5, 6), (5, 7), (5, 9)]  # Bottom row
        ]

        key_widths = {
            'Backspace': 10, 'Tab': 6, 'CapsLock': 7, 'Enter': 10,
            'Shift': 10, 'Ctrl': 6, 'Win': 5, 'Alt': 5, 'Space': 40,
            'Menu': 5
        }

        for row_index, row in enumerate(self.keys):
            for col_index, key in enumerate(row):
                width = key_widths.get(key, 4)
                button = tk.Button(self, text=key, width=width, height=2, bg="white")
                position = key_positions[row_index][col_index]
                button.grid(row=position[0], column=position[1], padx=2, pady=2, columnspan=1 if key != 'Space' else 4)
                self.buttons[key.upper()] = button

    def on_key_press(self, event):
        key = event.name.upper()
        if key in self.buttons:
            self.buttons[key].configure(bg="red")

    def on_key_release(self, event):
        key = event.name.upper()
        if key in self.buttons:
            threading.Timer(1.0, lambda: self.buttons[key].configure(bg="white")).start()

if __name__ == "__main__":
    app = OnScreenKeyboard()
    app.mainloop()
