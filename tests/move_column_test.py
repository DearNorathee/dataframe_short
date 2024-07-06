import dataframe_short.move_column as mc
import pandas as pd
import dataframe_short.utils_ds as ds 

def test_to_first_col():
    df_path01 = r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame\dataframe_short\tests\test_data\csv\04 Credit Risk Customer.csv"
    df = pd.read_csv(df_path01) 
    mc.to_first_col(df,'residence_since')

    mc.to_first_col(df,'residence_since',["job","class"])


def main():
    test_to_first_col()

if __name__ == "__main__":
    main()
