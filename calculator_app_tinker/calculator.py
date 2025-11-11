from tkinter import *
from tkinter import font
import ast


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        # Fonts
        self.display_font = font.Font(family="Segoe UI", size=28, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=14, weight="bold")

        # Create UI
        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Create the display entry field"""
        display_frame = Frame(self.root, bg="#1e1e1e")
        display_frame.pack(pady=20, padx=20, fill=BOTH)

        self.display = Entry(
            display_frame,
            font=self.display_font,
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify=RIGHT,
            insertbackground="#4CAF50"
        )
        self.display.pack(fill=BOTH, ipady=20, padx=5, pady=5)

    def create_buttons(self):
        """Create calculator buttons with improved layout"""
        button_frame = Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        # Button layout: [text, row, col, colspan, color_type]
        # color_type: 'num' for numbers, 'op' for operations, 'special' for special functions
        buttons = [
            ('AC', 0, 0, 1, 'special'), ('(', 0, 1, 1, 'op'), (')', 0, 2, 1, 'op'), ('←', 0, 3, 1, 'special'),
            ('7', 1, 0, 1, 'num'), ('8', 1, 1, 1, 'num'), ('9', 1, 2, 1, 'num'), ('÷', 1, 3, 1, 'op'),
            ('4', 2, 0, 1, 'num'), ('5', 2, 1, 1, 'num'), ('6', 2, 2, 1, 'num'), ('×', 2, 3, 1, 'op'),
            ('1', 3, 0, 1, 'num'), ('2', 3, 1, 1, 'num'), ('3', 3, 2, 1, 'num'), ('−', 3, 3, 1, 'op'),
            ('0', 4, 0, 1, 'num'), ('.', 4, 1, 1, 'num'), ('π', 4, 2, 1, 'op'), ('+', 4, 3, 1, 'op'),
            ('x²', 5, 0, 1, 'op'), ('^', 5, 1, 1, 'op'), ('%', 5, 2, 1, 'op'), ('=', 5, 3, 1, 'equals')
        ]

        # Color schemes
        colors = {
            'num': {'bg': '#3a3a3a', 'fg': '#ffffff', 'active': '#4a4a4a'},
            'op': {'bg': '#505050', 'fg': '#4CAF50', 'active': '#606060'},
            'special': {'bg': '#d32f2f', 'fg': '#ffffff', 'active': '#f44336'},
            'equals': {'bg': '#4CAF50', 'fg': '#ffffff', 'active': '#66BB6A'}
        }

        # Configure grid weights
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Create buttons
        for btn_text, row, col, colspan, color_type in buttons:
            cmd = self.get_button_command(btn_text)
            color = colors[color_type]

            btn = Button(
                button_frame,
                text=btn_text,
                font=self.button_font,
                bg=color['bg'],
                fg=color['fg'],
                activebackground=color['active'],
                activeforeground=color['fg'],
                bd=0,
                cursor="hand2",
                command=cmd
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=3,
                pady=3
            )

    def get_button_command(self, text):
        """Return the appropriate command for each button"""
        if text == 'AC':
            return self.clear_all
        elif text == '←':
            return self.undo
        elif text == '=':
            return self.calculate
        elif text == 'π':
            return lambda: self.insert_text('3.14159')
        elif text == 'x²':
            return lambda: self.insert_text('**2')
        elif text == '^':
            return lambda: self.insert_text('**')
        elif text == '×':
            return lambda: self.insert_text('*')
        elif text == '÷':
            return lambda: self.insert_text('/')
        elif text == '−':
            return lambda: self.insert_text('-')
        else:
            return lambda: self.insert_text(str(text))

    def insert_text(self, text):
        """Insert text at cursor position"""
        self.display.insert(INSERT, text)

    def clear_all(self):
        """Clear the display"""
        self.display.delete(0, END)

    def undo(self):
        """Remove last character"""
        current = self.display.get()
        if current:
            self.display.delete(len(current) - 1, END)

    def calculate(self):
        """Evaluate the expression"""
        expression = self.display.get()
        try:
            # Parse and evaluate safely
            node = ast.parse(expression, mode="eval")
            result = eval(compile(node, '<string>', 'eval'))

            # Format result
            if isinstance(result, float):
                # Remove trailing zeros
                result = f"{result:.10f}".rstrip('0').rstrip('.')

            self.clear_all()
            self.display.insert(0, result)
        except:
            self.clear_all()
            self.display.insert(0, "Error")


# Main application
if __name__ == "__main__":
    root = Tk()
    app = Calculator(root)
    root.mainloop()