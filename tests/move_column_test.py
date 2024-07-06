import dataframe_short.move_column as mc
import pandas as pd
import dataframe_short.utils_ds as ds 
import inspect_py as inp
def _get_test_data_path(filename:str,test_folder:str = 'test_data/csv' ):
    from pathlib import Path
    """
    Get the absolute path to a test data file.
    
    Args:
    filename (str): Name of the test data file.
    
    Returns:
    pathlib.Path: Absolute path to the test data file.
    """
    # Get the directory of the current file
    current_dir = Path(__file__).resolve().parent
    
    # Construct the path to the test_data directory
    test_data_dir = current_dir / test_folder
    
    # Return the full path to the specified file
    return test_data_dir / filename

def test_to_first_col():
    
    df_path01 = _get_test_data_path("04 Credit Risk Customer.csv")
    df01 = pd.read_csv(df_path01) 
    
    df01_type_01 = ds.dtype(df01,True)
    
    mc.to_first_col(df01,'residence_since')
    
    df01_type_02 = ds.dtype(df01,True)
    
    assert df01_type_01 == df01_type_02, inp.assert_message(df01_type_02, df01_type_01)
    
    df01_first_column_name = df01.columns[0]
    
    assert df01_first_column_name == 'residence_since', inp.assert_message(df01_first_column_name, 'residence_since')
    
    mc.to_first_col(df01,["job","class"])
    
    df01_first_2_name = df01.columns[:2].tolist()
    df01_type_03 = ds.dtype(df01,True)
    
    assert df01_first_2_name == ["job","class"]
    
    df01_ori_order = list(df01.columns)
    actual01 = mc.to_first_col(df01,['housing','num_dependents','installment_commitment'],False)
    
    actual01_first_3_cols = actual01.columns[:3].tolist()
    # the original df shouldn't be modify, and I tried to test the order of original df
    assert list(df01.columns) == df01_ori_order
    
    # test if the first 3 columns of actual01 is ['housing','num_dependents','installment_commitment']
    assert actual01_first_3_cols == ['housing','num_dependents','installment_commitment']
    
    
    # try to move the columns that aren't in df01
    # this should throw ValueError
    try:
        mc.to_first_col(df01,['housing','num dependents','installment commitment'])
    except Exception  as e:
        assert isinstance(e, ValueError)
    
    
    print("")

def test_to_last_col():

    df_path01 = _get_test_data_path("04 Credit Risk Customer.csv")
    df01 = pd.read_csv(df_path01) 
    
    df01_type_01 = ds.dtype(df01,True)
    
    mc.to_last_col(df01,'residence_since')
    
    df01_type_02 = ds.dtype(df01,True)
    
    assert df01_type_01 == df01_type_02, inp.assert_message(df01_type_02, df01_type_01)
    
    df01_first_column_name = df01.columns[-1]
    
    assert df01_first_column_name == 'residence_since', inp.assert_message(df01_first_column_name, 'residence_since')
    
    mc.to_last_col(df01,["job","class"])
    
    df01_first_2_name = df01.columns[-2:].tolist()
    df01_type_03 = ds.dtype(df01,True)
    
    assert df01_first_2_name == ["job","class"]
    
    df01_ori_order = list(df01.columns)
    actual01 = mc.to_last_col(df01,['housing','num_dependents','installment_commitment'],False)
    
    actual01_first_3_cols = actual01.columns[-3:].tolist()
    # the original df shouldn't be modify, and I tried to test the order of original df
    assert list(df01.columns) == df01_ori_order
    
    # test if the first 3 columns of actual01 is ['housing','num_dependents','installment_commitment']
    assert actual01_first_3_cols == ['housing','num_dependents','installment_commitment']
    
    
    # try to move the columns that aren't in df01
    # this should throw ValueError
    try:
        mc.to_last_col(df01,['housing','num dependents','installment commitment'])
    except Exception  as e:
        assert isinstance(e, ValueError)
    
    
    print("")


def main():
    test_to_last_col()
    test_to_first_col()

if __name__ == "__main__":
    main()
