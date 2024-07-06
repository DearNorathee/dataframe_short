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
    # 1 shot from Claude 3.5, July 6, 24
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


def to_last_col(df: pd.DataFrame, cols: Union[str, List[str]], inplace: bool = True) -> Union[pd.DataFrame, None]:
    # 1 shot from Claude 3.5, July 6, 24
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
    new_order = cols_remain + cols
    
    if inplace:
        # Reorder the columns in-place
        df.sort_index(axis=1, key=lambda x: pd.Index([new_order.index(c) if c in new_order else len(df.columns) for c in x]), inplace=True)
        return None
    else:
        # Create a new DataFrame with the new order
        return df.reindex(columns=new_order)
    


# def to_front_of(df: pd.DataFrame, col_ref: Union[str, int], cols_to_move: Union[str, List[str]], inplace: bool = True) -> Union[pd.DataFrame, None]:
    # from Claude
#     """
#     Reorder the columns of a dataframe by moving specified columns in front of a reference column while preserving dtypes.

#     Parameters
#     ----------
#     df : pandas.DataFrame
#         The dataframe to reorder.
#     col_ref : str or int
#         The reference column name (str) or index (int) to move the columns in front of.
#     cols_to_move : str or list of str
#         The column name or names to move.
#     inplace : bool, optional
#         Whether to modify the original dataframe or return a new one. Default is True.

#     Returns
#     -------
#     pandas.DataFrame or None
#         The reordered dataframe if inplace is False, otherwise None.

#     Examples
#     --------
#     >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
#     >>> df
#        A  B  C   D
#     0  1  4  7  10
#     1  2  5  8  11
#     2  3  6  9  12
#     >>> to_front_of(df, 'C', ['A', 'D'])
#     >>> df
#        A   D  C  B
#     0  1  10  7  4
#     1  2  11  8  5
#     2  3  12  9  6
#     >>> result = to_front_of(df, 1, 'D', inplace=False)
#     >>> result
#        A  D  B  C
#     0  1 10  4  7
#     1  2 11  5  8
#     2  3 12  6  9
#     """
    
#     # Convert cols_to_move to a list if it is a string
#     if isinstance(cols_to_move, str):
#         cols_to_move = [cols_to_move]
    
#     # Ensure all specified columns exist in the DataFrame
#     non_existent = set(cols_to_move) - set(df.columns)
#     if non_existent:
#         raise ValueError(f"Columns {non_existent} do not exist in the DataFrame")
    
#     # Get the index of the reference column
#     if isinstance(col_ref, str):
#         if col_ref not in df.columns:
#             raise ValueError(f"Reference column '{col_ref}' does not exist in the DataFrame")
#         ref_index = df.columns.get_loc(col_ref)
#     elif isinstance(col_ref, int):
#         if col_ref < 0 or col_ref >= len(df.columns):
#             raise ValueError(f"Reference column index {col_ref} is out of bounds")
#         ref_index = col_ref
#     else:
#         raise TypeError("col_ref must be either a string (column name) or an integer (column index)")

#     # Create the new column order
#     current_order = df.columns.tolist()
#     for col in reversed(cols_to_move):
#         current_order.remove(col)
#         current_order.insert(ref_index, col)

#     if inplace:
#         # Reorder the columns in-place
#         df.sort_index(axis=1, key=lambda x: pd.Index([current_order.index(c) for c in x]), inplace=True)
#         return None
#     else:
#         # Create a new DataFrame with the new order
#         return df.reindex(columns=current_order)
    

def to_front_of(df: pd.DataFrame, col_ref: Union[str, int], cols_to_move: Union[str, List[str]], inplace: bool = True) -> Union[pd.DataFrame, None]:
    # not done 

    # still doesn't work when 

    # From ChatGPT 4o as of July 6, 24
    # hard for 


    """
    Move specified columns in front of a reference column in a dataframe while preserving dtypes.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to reorder.
    col_ref : str or int
        The reference column name or index in front of which the columns will be moved.
    cols_to_move : str or list of str
        The column name or names to move.
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
    >>> to_front_of(df, 'B', 'C')
    >>> df
       A  C  B
    0  1  7  4
    1  2  8  5
    2  3  9  6
    >>> result = to_front_of(df, 0, ['B', 'C'], inplace=False)
    >>> result
       B  C  A
    0  4  7  1
    1  5  8  2
    2  6  9  3
    """
    
    # Convert cols_to_move to a list if it is a string
    if isinstance(cols_to_move, str):
        cols_to_move = [cols_to_move]

    # Ensure all specified columns exist in the DataFrame
    non_existent = set(cols_to_move) - set(df.columns)
    if non_existent:
        raise ValueError(f"Columns {non_existent} do not exist in the DataFrame")

    # Determine the index of the reference column
    if isinstance(col_ref, int):
        if col_ref < 0 or col_ref >= len(df.columns):
            raise ValueError("col_ref index is out of range")
        col_ref_index = col_ref
    elif isinstance(col_ref, str):
        if col_ref not in df.columns:
            raise ValueError(f"Column '{col_ref}' does not exist in the DataFrame")
        col_ref_index = df.columns.get_loc(col_ref)
    else:
        raise ValueError("col_ref must be a string or an integer")

    # Create a list of the remaining columns
    cols_remain = [x for x in df.columns if x not in cols_to_move]

    # Create the new column order
    new_order = cols_remain[:col_ref_index] + cols_to_move + cols_remain[col_ref_index:]

    if inplace:
        # Reorder the columns in-place
        df.sort_index(axis=1, key=lambda x: pd.Index([new_order.index(c) if c in new_order else len(df.columns) for c in x]), inplace=True)
        return None
    else:
        # Create a new DataFrame with the new order
        return df.reindex(columns=new_order)

