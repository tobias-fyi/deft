"""
deft.format :: Deft Formatting
"""


def table_printer(array, title, left_width, right_width):
    """
    Formats list - table of contents style.
    
    Parameters
    ----------
    array : dictionary
        Dictionary to be printed as table.
    title : string
        Title of the table; appears at top.
    left_width : integer
        Width, in characters, of the left column.
    right_width : integer
        Width, in characters, of the right column.
    """

    print(f"{title}".center(left_width + right_width, "-"))

    for k, v in array.items():
        print(str(k).ljust(left_width, ".") + str(v).rjust(right_width, "."))


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
