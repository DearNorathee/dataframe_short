import dataframe_short.move_column as mc
import pandas as pd
import dataframe_short.utils_ds as ds 
import inspect_py as inp
from dataframe_short.sandbox1_ds import *

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


def main():
    test_add_prefix_num()

if __name__ == "__main__":
    main()