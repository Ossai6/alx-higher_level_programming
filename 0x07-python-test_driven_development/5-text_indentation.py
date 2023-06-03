#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    lines = []
    current_line = ""

    for char in text:
        if char in [".", "?", ":"]:
            current_line += char
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""
        else:
            current_line += char

    if current_line:
        lines.append(current_line.strip())

    output = "\n".join(lines)
    print(output, end="")
