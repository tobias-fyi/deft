"""
deftools :: Deft Data Wrangling
"""

# ====== Imports ====== #
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# ====== Code ====== #
class DeftString:
    """
    A general class for string manipulation and functions.
    """

    def __init__(self, string):
        self.string = string

    def caps_ratio(self):
        """
        Calculates the ratio of capital to lowercase letters in a given string.
        """
        cap = sum(1 for l in self.string if l.isupper())
        total = len(self.string)
        return round(cap / total, 6)


class DeftPlot:
    """
    A general glass for generating plots from Pandas DataFrames.
    """

    def __init__(self, df):
        self.df = df


def random_dataframe(pool, shape, columns):
    """
    Creates a DataFrame of random integers.

    # ============ #
    pool (tuple): define the range of numbers (min, max) from which to draw.
        ex: (0, 100) - pick numbers between 0 and 100.
    shape (tuple): define the shape of the generated DataFrame. 
        ex: (100, 4) - 100 rows, 4 columns.
    columns (list): names of the columns in the generated DataFrame.
    # ============ #
    """
    return pd.DataFrame(
        np.random.randint(pool[0], pool[1], size=shape), columns=columns
    )


class DeftDf(pd.Dataframe):
    """A class for manipulating dataframes."""

    # TODO: figure out how to use .super() effectively
    # def __init__(self, df):
    #     self.df = df

    def data_split(self, test_size=0.2, stratify=None):
        """
        Splits up a DataFrame into train and test sets.

        # ============ #
        df (pd.DataFrame): data to be split.
        stratify (pd.Series): target column or Series to use for stratification.
        # ============ #
        """
        return train_test_split(
            self, test_size=test_size, random_state=42, stratify=stratify
        )

    def date_wrangler(self, date_col):
        """
        Converts date_col to Pandas datetime and 
        splits it up into year, month, day components.
        Returns a copy of the original DataFrame 
        with the components and without the original column.

        # ============ #
        df (pd.DataFrame): DataFrame containing the column to be wrangled.
        date_col (string): name of column to be converted and split.
        # ============ #
        """
        data = self.copy()  # Create a copy of the DataFrame

        # Convert target column to datetime
        data[date_col] = pd.to_datetime(
            data[date_col], infer_datetime_format=True
        )

        # Split column into datetime components
        data[f"{date_col}_year"] = data[date_col].dt.year
        data[f"{date_col}_year"] = data[date_col].dt.month
        data[f"{date_col}_year"] = data[date_col].dt.day

        # Drop original column
        data = data.drop(columns=date_col)

        return data
