from typing import *
import pandas as pd
import polars as pl
import datatable as dt
import pandas as pd
from typing import Union, List
import numpy as np

# Define my own types

Scalar_Numpy = Union[np.number, np.bool_, np.object_, np.string_]
Scalar_BuiltIn = Union[int, float, str, bool, complex]

Scaler = Union[Scalar_BuiltIn,Scalar_Numpy]

def to_first_col(df: pd.DataFrame, cols: Union[str, List[str]], inplace: bool = True) -> Union[pd.DataFrame, None]:
    """
    Reorder the columns of a dataframe by moving some columns to the front while preserving dtypes.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to reorder.
    cols : str or list of str
        The column name or names to move to the front.
    inplace : bool, optional
        Whether to modify the original dataframe or return a new one. Default is True.

    Returns
    -------
    pandas.DataFrame or None
        The reordered dataframe if inplace is False, otherwise None.

    Examples
    --------
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    >>> df
       A  B  C
    0  1  4  7
    1  2  5  8
    2  3  6  9
    >>> to_first_col(df, 'C')
    >>> df
       C  A  B
    0  7  1  4
    1  8  2  5
    2  9  3  6
    >>> result = to_first_col(df, ['B', 'C'], inplace=False)
    >>> result
       B  C  A
    0  4  7  1
    1  5  8  2
    2  6  9  3
    """
    
    # Convert cols to a list if it is a string
    if isinstance(cols, str):
        cols = [cols]
    
    # Ensure all specified columns exist in the DataFrame
    non_existent = set(cols) - set(df.columns)
    if non_existent:
        raise ValueError(f"Columns {non_existent} do not exist in the DataFrame")
    
    # Create a list of the remaining columns
    cols_remain = [x for x in df.columns if x not in cols]
    
    # Create the new column order
    new_order = cols + cols_remain
    
    if inplace:
        # Reorder the columns in-place
        df.sort_index(axis=1, key=lambda x: pd.Index([new_order.index(c) if c in new_order else len(df.columns) for c in x]), inplace=True)
        return None
    else:
        # Create a new DataFrame with the new order
        return df.reindex(columns=new_order)
   
# def to_first_col(df:Union[pd.DataFrame], cols, inplace=True):
#     """
#     old code
#     based on pd version == 2.1.3
    
#     Reorder the columns of a dataframe by moving some columns to the front.

#     Parameters
#     ----------
#     df : pandas.DataFrame
#         The dataframe to reorder.
#     cols : str or list of str
#         The column name or names to move to the front.
#     inplace : bool, optional
#         Whether to modify the original dataframe or return a new one. Default is True.

#     Returns
#     -------
#     pandas.DataFrame or None
#         The reordered dataframe if inplace is False, otherwise None.

#     Examples
#     --------
#     >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
#     >>> df
#        A  B  C
#     0  1  4  7
#     1  2  5  8
#     2  3  6  9

#     >>> pd_move_col_front(df, 'C')
#     >>> df
#        C  A  B
#     0  7  1  4
#     1  8  2  5
#     2  9  3  6

#     >>> pd_move_col_front(df, ['B', 'C'], inplace=False)
#        B  C  A
#     0  4  7  1
#     1  5  8  2
#     """
    
#     # Convert cols to a list if it is a string
#     if isinstance(cols, str):
#         cols = [cols]

#     # Create a list of the remaining columns
#     cols_remain = [x for x in df.columns if x not in cols]

#     # Reorder the columns by concatenating the two lists
#     df_new = df[cols + cols_remain]

#     # Modify the original dataframe or return a new one depending on inplace parameter
#     if inplace:
#         df.columns = df_new.columns
#         df[:] = df_new
#         # return None
#     else:
#         return df_new

# def move_col_front(df, cols, inplace=True):
#     """
#     from Claude 3(solo)
#     # based on pd version == 2.1.3

#     Reorder the columns of a dataframe by moving some columns to the front.

#     Parameters
#     ----------
#     df : pandas.DataFrame
#         The dataframe to reorder.
#     cols : str or list of str
#         The column name or names to move to the front.
#     inplace : bool, optional
#         Whether to modify the original dataframe or return a new one. Default is True.

#     Returns
#     -------
#     pandas.DataFrame or None
#         The reordered dataframe if inplace is False, otherwise None.

#     Examples
#     --------
#     >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
#     >>> df
#        A  B  C
#     0  1  4  7
#     1  2  5  8
#     2  3  6  9

#     >>> pd_move_col_front(df, 'C')
#     >>> df
#        C  A  B
#     0  7  1  4
#     1  8  2  5
#     2  9  3  6

#     >>> pd_move_col_front(df, ['B', 'C'], inplace=False)
#        B  C  A
#     0  4  7  1
#     1  5  8  2
#     2  6  9  3
#     """
#     # Convert cols to a list if it is a string
#     if isinstance(cols, str):
#         cols = [cols]

#     # Create a list of the remaining columns
#     cols_remain = [x for x in df.columns if x not in cols]

#     # Get the original data types of the columns
#     dtypes = {col: df[col].dtypes for col in df.columns}

#     # Reorder the columns by concatenating the two lists
#     df_new = df[cols + cols_remain]

#     # Modify the original dataframe or return a new one depending on inplace parameter
#     if inplace:
#         # Replace the data in the original DataFrame with the reordered data
#         df[:] = df_new

#         # Restore the original data types of the columns
#         for col in df.columns:
#             df[col] = df[col].astype(dtypes[col])
#         # return None
#     else:
#         return df_new