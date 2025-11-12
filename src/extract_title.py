def extract_title(markdown: str) -> str:
    """
    Extracts the first H1 (#) title from markdown text.
    Example: "# Hello" → "Hello"
    Raises ValueError if no H1 header found.
    """
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown.")
