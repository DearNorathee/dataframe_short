import dataframe_short.move_column as mc
import pandas as pd
import dataframe_short.utils_ds as ds 
import inspect_py as inp
from dataframe_short.sandbox1_ds import *
from pandas.testing import assert_frame_equal


def test_add_prefix_num():
    # ds._get_test_data_path doesn't work for some reasons
    df_path01 = ds._get_test_data_path("04 Credit Risk Customer.csv")
    df_path01 = r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame\dataframe_short\tests\test_input\csv\04 Credit Risk Customer.csv"
    df01 = pd.read_csv(str(df_path01))
    series01 = add_prefix_num(df01,'credit_history')
    actual01 = series01.iloc[0]

    series02 = add_prefix_num(df01,'credit_history',start_index=0)
    actual02 = series02.iloc[0]

    expect01 = "0001_critical/other existing credit"
    expect02 = "0000_critical/other existing credit"

    assert expect01 == actual01, inp.assert_message(actual01,expect01)
    assert expect02 == actual02, inp.assert_message(actual02,expect02)

    print()

def test_check_levels():
    df1_left = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    df1_right = pd.DataFrame({'X': [2, 3, 4], 'Y': ['b', 'c', 'd']})
    cols_map = {'A': 'X', 'B': 'Y'}
    actual01 = ds.check_levels(df1_left, df1_right, cols_map)
    
    expect01 = pd.DataFrame({
    'left_col': ['A', 'B'],
    'right_col': ['X', 'Y'],
    'left_only': [[1], ['a']],
    'right_only': [[4], ['d']],
    'both': [[2, 3], ['b', 'c']]
    })
    
    expect02 = pd.DataFrame({
    'left_col': ['A', 'B'],
    'right_col': ['X', 'Y'],
    'left_only': [[1.0], ['a']],
    'right_only': [[4.0], ['d']],
    'both': [[2.0, 3.0], ['b', 'c']]
    })
    
    
    df2_left = pd.DataFrame({'A': [1, '2', 3], 'B': ['a', 'b', 'c']})
    df2_right = pd.DataFrame({'X': [2.0, 3, 4], 'Y': ['b', 'c', 'd']})
    
    # Define the column mapping
    cols_map = {'A': 'X', 'B': 'Y'}
    
    # Run the level check with ignore_dtype=True
    actual02 = ds.check_levels(df2_left, df2_right, cols_map, ignore_dtype=True)
    assert_frame_equal(actual01,expect01)
    assert_frame_equal(actual02,expect02)


def main():
    test_add_prefix_num()

if __name__ == "__main__":
    main()