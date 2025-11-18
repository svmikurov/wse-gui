"""Text hyphenation UseCase."""

from typing import override

from . import TextHyphenationABC


class TextHyphenation(TextHyphenationABC):
    """Text hyphenation."""

    MAX_STRING_LENGTH: int = 21
    LINE_BREAK = '\r\n'

    @override
    @classmethod
    def adapt(cls, text: str) -> str:
        """Adapt text for screen."""
        if len(text) < cls.MAX_STRING_LENGTH:
            return text

        adapted_text = cls._add_line_break(text, cls.MAX_STRING_LENGTH)
        return adapted_text

    @classmethod
    def _add_line_break(cls, text: str, max_string_length: int) -> str:
        """Add line breaks to text."""
        line: list[str] = []
        lines: list[str] = []
        space_length = 1
        counter = 0
        words = text.split(' ')

        while words:
            word = words.pop(0)
            counter += len(word)

            if counter >= max_string_length:
                snippet: str = ' '.join(line)
                lines.append(snippet)
                line = []
                counter = len(word)

            counter += space_length
            line.append(word)

        snippet = ' '.join(line)
        lines.append(snippet)
        paragraph: str = cls.LINE_BREAK.join(lines)
        return paragraph
