from dataframe_short.move_column import *
# import dataframe_short.move_column as mc
import pandas as pd
import dataframe_short.utils_ds as ds 
import inspect_py as inp
from typing import *

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


def test_to_front_of():

    df_path01 = _get_test_data_path()[1]
    df01 = pd.read_csv(df_path01) 
    
    df01_type_01 = ds.dtype(df01,True)
    
    mc.to_front_of(df01,'checking_status','residence_since')
    
    df01_type_02 = ds.dtype(df01,True)
    
    assert df01_type_01 == df01_type_02, inp.assert_message(df01_type_02, df01_type_01)
    
    df01_first_column_name = df01.columns[0]
    
    assert df01_first_column_name == 'residence_since', inp.assert_message(df01_first_column_name, 'residence_since')
    
    mc.to_front_of(df01,'residence_since',["job","class"])
    
    df01_first_2_name = df01.columns[:2].tolist()
    df01_type_03 = ds.dtype(df01,True)
    
    assert df01_first_2_name == ["job","class"]
    
    # ori order housing is after purpose
    actual03 = mc.to_front_of(df01,'purpose',['housing',],False)
    
    
    df01_ori_order = list(df01.columns)
    
    # ori order housing is before 'own_telephone'
    actual01 = mc.to_front_of(df01,'own_telephone',['housing',],False)
    actual01_last_cols = actual01.columns[-3:].tolist()
    # ori order housing is before 'foreign_worker'
    actual02 = mc.to_front_of(df01,'foreign_worker',['housing',],False)
    
    actual02_last_cols = actual02.columns[-2:].tolist()
    # the original df shouldn't be modify, and I tried to test the order of original df
    assert list(df01.columns) == df01_ori_order
    
    
    
    # test if the first 3 columns of actual01 is ['housing','num_dependents','installment_commitment']
    assert actual01_last_cols == ['housing','own_telephone','foreign_worker']
    
    
    # try to move the columns that aren't in df01
    # this should throw ValueError
    try:
        mc.to_front_of(df01,'own_telephone',['housing','num dependents','installment commitment'])
    except Exception as e:
        assert isinstance(e, ValueError), inp.assert_message(e,ValueError)
    
    
    print("")

def test_to_first_col():
    
    df_path01 = _get_test_data_path()[1]
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
    except Exception as e:
        assert isinstance(e, ValueError)
    
    
    print("")

def test_to_last_col():

    df_path01 = _get_test_data_path()[1]
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
    test_to_front_of()
    test_to_last_col()
    test_to_first_col()

if __name__ == "__main__":
    main()
