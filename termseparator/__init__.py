# termseparator/__init__.py

#changed from seperator to s
def s(word=None, color="green"):
    """
    Prints a stylized separator line with a centered word, with optional color.
    If no word is provided, it prints a solid line.
    """
    
    # Define ANSI color codes
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
    
    # Get the specified color code (defaults to green if input is invalid)
    color_code = colors.get(color.lower(), colors["green"])
    
    # --- Logic for Optional Word ---
    if word:
        # If a word is provided, create the separator with the word in the center
        # We use a 20-hyphen line on each side
        separator_content = f"{'-' * 20}< {word} >{'-' * 20}"
    else:
        # If no word is provided, create a single, longer line (20 + 4 + 20 = 44 hyphens)
        separator_content = f"{'-' * 44}"
        
    # Print the line with color
    print(f"\n{color_code}{separator_content}{colors['reset']}\n")

# Make your function available when the package is imported
__all__ = ['separator']