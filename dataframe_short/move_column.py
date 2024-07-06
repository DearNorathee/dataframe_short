
def move_col_front(df, cols, inplace=True):
    """
    old code
    # based on pd version == 2.1.3
    
    Reorder the columns of a dataframe by moving some columns to the front.

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

    >>> pd_move_col_front(df, 'C')
    >>> df
       C  A  B
    0  7  1  4
    1  8  2  5
    2  9  3  6

    >>> pd_move_col_front(df, ['B', 'C'], inplace=False)
       B  C  A
    0  4  7  1
    1  5  8  2
    """
    
    # Convert cols to a list if it is a string
    if isinstance(cols, str):
        cols = [cols]

    # Create a list of the remaining columns
    cols_remain = [x for x in df.columns if x not in cols]

    # Reorder the columns by concatenating the two lists
    df_new = df[cols + cols_remain]

    # Modify the original dataframe or return a new one depending on inplace parameter
    if inplace:
        df.columns = df_new.columns
        df[:] = df_new
        # return None
    else:
        return df_new

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