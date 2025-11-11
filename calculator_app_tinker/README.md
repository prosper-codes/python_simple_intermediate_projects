# 🧮 Python Tkinter Calculator

A functional calculator application built with Python and Tkinter, featuring basic arithmetic operations and advanced mathematical functions.

## ✨ Features

- ➕ **Basic Arithmetic** - Addition, subtraction, multiplication, and division
- 🔢 **Number Pad** - Easy-to-use 0-9 number buttons
- 🔬 **Advanced Operations** - Power (x²), exponentiation (**), modulo (%)
- 🥧 **Pi Constant** - Quick access to π (3.14)
- 🧮 **Parentheses Support** - For complex mathematical expressions
- 🔙 **Undo Button** - Backspace functionality to correct mistakes
- 🗑️ **Clear All (AC)** - Reset the calculator instantly
- ⚠️ **Error Handling** - Displays "Error" for invalid expressions

## 📸 Screenshot

```
┌──────────────────────────────┐
│  Display: [____________]     │
├──────────────────────────────┤
│  1  │  2  │  3  │  +  │  %  │
│  4  │  5  │  6  │  -  │  (  │
│  7  │  8  │  9  │  *  │ **  │
│ AC  │  0  │  =  │  /  │  )  │
│     │     │     │ 3.14│ **2 │
│     │     │  <- │     │     │
└──────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Tkinter (included with most Python installations)

### Installation & Running

1. **Download the script**
   ```bash
   # Save the calculator.py file to your computer
   ```

2. **Run the calculator**
   ```bash
   python calculator.py
   ```

That's it! The calculator window should open immediately.

## 💻 How to Use

### Basic Operations
1. Click number buttons (1-9, 0) to enter numbers
2. Click operation buttons (+, -, *, /) for calculations
3. Press **=** to calculate the result
4. Use **AC** to clear everything
5. Use **<-** to delete the last character

### Advanced Functions
- **( )** - Use parentheses for order of operations: `(2+3)*4`
- **%** - Modulo operator for remainders: `10%3 = 1`
- **\*\*** - Power operator: `2**3 = 8`
- **\*\*2** - Square a number: `5**2 = 25`
- **3.14** - Insert Pi constant

### Example Calculations
```
Basic: 25 + 17 = 42
Division: 100 / 4 = 25
Power: 2**10 = 1024
Complex: (5+3)*2 = 16
Modulo: 17%5 = 2
```

## 🔧 Technical Implementation

### Key Components

**Libraries Used:**
- `tkinter` - GUI framework
- `sqlalchemy` - Imported but not used (can be removed)
- `ast` - Safe expression parsing and evaluation

**Main Functions:**
- `get_number(num)` - Inserts numbers into display
- `get_operation(operator)` - Inserts operators into display
- `calculate()` - Evaluates the expression using AST
- `clear_all()` - Clears the display
- `undo()` - Removes last character

### Safety Features
- Uses `ast.parse()` for safe expression evaluation
- Avoids dangerous `eval()` with raw user input
- Exception handling for invalid expressions

## 📝 Code Structure

```python
# Global variable for cursor position
i = 0

# Main window setup
root = Tk()

# Core functions
get_number()      # Insert numbers
get_operation()   # Insert operators
calculate()       # Evaluate expression
clear_all()       # Clear display
undo()           # Backspace

# GUI Layout
- Entry widget for display
- 3x3 grid for numbers 1-9
- Operation buttons in columns
- Special function buttons
```

## 🎯 Button Layout

| Position | Button | Function |
|----------|--------|----------|
| Row 2-4, Col 0-2 | 1-9 | Number input |
| Row 5, Col 1 | 0 | Zero |
| Row 2-4, Col 3-6 | +,-,*,/,etc | Operations |
| Row 5, Col 0 | AC | Clear all |
| Row 5, Col 2 | = | Calculate |
| Row 5, Col 4 | <- | Undo/Backspace |

## 🐛 Known Limitations

- Global variable `i` tracks cursor position (could be improved with Tkinter's cursor methods)
- `sqlalchemy` import is unused
- Fixed button sizes may look different on various screen resolutions
- No keyboard input support
- Basic visual styling

## 🚀 Future Improvements

Potential enhancements for this calculator:
- [ ] Add keyboard support
- [ ] Improve UI with better colors and styling
- [ ] Add calculation history
- [ ] Implement scientific functions (sin, cos, tan, log)
- [ ] Make responsive design for different screen sizes
- [ ] Add memory functions (M+, M-, MR, MC)
- [ ] Show intermediate calculations

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a learning project to explore Python GUI development with Tkinter.

## 🙏 Acknowledgments

- Built with Python's standard Tkinter library
- Uses AST module for safe expression evaluation
- Inspired by standard calculator applications

---

**Note:** This is a basic implementation perfect for learning Tkinter and GUI programming. For production use, consider adding more features and improving the code structure.

⭐ If you found this helpful, please star the repository!
