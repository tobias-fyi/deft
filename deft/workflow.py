"""
deftools.workflow :: Deft Workflow Configuration
"""

# ====== Imports ====== #
import pandas as pd
import numpy as np


# ====== Code ====== #


def max_columns(num_cols: int) -> None:
    """Shortcut for pd.set_option.display.max_columns."""
    pd.set_option("display.max_columns", num_cols)


def max_rows(num_rows: int) -> None:
    """Shortcut for pd.set_option.display.max_rows."""
    pd.set_option("display.max_rows", num_rows)

