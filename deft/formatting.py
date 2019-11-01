"""
deft.format :: Deft Formatting
"""


# ========= FuncZone ========= #


def justify_center(content: str, width: int, symbol: str) -> str:
    """
    Centers string in symbol, width chars wide.
    
    Parameters
    ----------
    content : string
        The string (1+ lines long) to be centered.
    width : integer
        Width of the column in characters within which
        the string will be centered.
    symbol : string
        Symbol to use as filler surrounding the string.
    
    Returns
    -------
    string
        String consisting of the same number of lines as content.
    """

    # Split the content into lines
    lines = content.split("\n")

    # Loop through lines, centering each
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, symbol)

    # Rejoin the lines into single content string
    content = "\n".join(lines)

    return content
