"""Utility functions."""

LINE_BREAK = '\r\n'


def add_line_break(text: str, max_string_length: int) -> str:
    """Add line breaks to text."""
    line, lines = [], []
    space_length = 1
    counter = 0
    words = text.split(' ')

    while words:
        word = words.pop(0)
        counter += len(word)

        if counter >= max_string_length:
            snippet = ' '.join(line)
            lines.append(snippet)
            line = []
            counter = len(word)

        counter += space_length
        line.append(word)

    snippet = ' '.join(line)
    lines.append(snippet)
    paragraph = LINE_BREAK.join(lines)
    return paragraph
