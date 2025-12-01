# ts

A simple, lightweight utility function designed to print clean, stylized, and colored separator lines directly in your terminal. Perfect for organizing output in data analysis scripts, CLI tools, or development logs.

## ✨ Features

* **Simple Syntax:** One function call to print a clean line.
* **Optional Title:** Centers a word within the separator line.
* **Color Support:** Supports standard terminal colors like green, blue, red, and yellow.
* **Zero Dependencies:** Relies only on built-in Python features (ANSI colors).

## ⬇️ Installation

You can install `termseparator` globally using pip:

```bash
pip install termseparator


🚀 Usage
The function accepts an optional title word (word) and an optional color string (color).

Python

import termseparator as ts


# 1. Simple, default usage (green solid line)
ts.s()

# 2. Separator with a centered title (default green)
ts.s("DATA LOADING COMPLETE")

# 3. Separator with a different color
ts.s("PROCESSING DATA", color="blue")

# 4. Solid red line
ts.s(color="red")