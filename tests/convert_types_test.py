
from typing import List, Dict, Literal, Union, Any
import pandas as pd
from dataframe_short.convert_types import *

def _get_test_data_path() -> Dict[int,str]:
    # becareful when you move this function around the file because your reference may have changed and throw an error

    from pathlib import Path
    """
    Get the absolute path to a test data file.
    For edit path manually
    
    Args:
    filename (str): Name of the test data file.
    
    Returns:
    pathlib.Path: Absolute path to the test data file.
    """
    # Get the current folder of the current file
    # current_dir = Path(__file__).resolve().parent
    
    # Construct the path to the test_data directory
    # test_data_dir = current_dir / test_folder
    
    # Return the full path to the specified file
    out_dict = {}
    out_dict[1] = r"Python MyLib 01\02 DataFrame\dataframe_short\tests\test_input\csv\01 Credit Risk Customer.csv"
    return out_dict

def test_to_str():
    df_path01 = _get_test_data_path()[1]
    df01 = pd.read_csv(df_path01) 

    to_str(df01,cols = ['duration','purpose'])
    assert df01['duration'].dtype == 'object'
    assert df01['purpose'].dtype == 'object'
    
    actual01 = to_str(df01,cols = ['num_dependents','age'],inplace=False)
    assert df01['num_dependents'].dtype == 'float'
    assert df01['age'].dtype == 'float'
    
    assert actual01['num_dependents'].dtype == 'object'
    assert actual01['age'].dtype == 'object'

def main():
    test_to_str()


if __name__ == "__main__":
    main()