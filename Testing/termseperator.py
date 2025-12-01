"""
# termseparator

pip install termseparator

A simple, lightweight utility function designed to print clean, stylized, and colored separator lines directly in your terminal. Perfect for organizing output in data analysis scripts, CLI tools, or development logs.

## ✨ Features

* **Simple Syntax:** One function call to print a clean line.
* **Optional Title:** Centers a word within the separator line.
* **Color Support:** Supports standard terminal colors like green, blue, red, and yellow.
* **Zero Dependencies:** Relies only on built-in Python features (ANSI colors).
    """

import termseparator as ts

# 1. Simple, default usage (green solid line)
ts.separator()

# 2. Separator with a centered title (default green)
ts.separator("DATA LOADING COMPLETE")

# 3. Separator with a different color
ts.separator("PROCESSING DATA", color="blue")

# 4. Solid red line
ts.separator(color="red")