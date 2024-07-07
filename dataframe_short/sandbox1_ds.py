from typing import *
import pandas as pd
import dataframe_short.utils_ds as ds 

def add_prefix_num(df:Union[pd.DataFrame],
                   col:str,
                   start_index:int = 1,
                   increment:int = 1, # not implemented
                   ) -> pd.Series:
    n_rows = df.shape[0]
    
    digit_rows = len(str(n_rows))
   
    df_copy = ds.by_col(df,col)
    
    df_copy.reset_index(drop=True, inplace=True)
    df_copy.index += start_index

    out_series = df_copy.index.map(lambda x: f"{str(x).zfill(digit_rows)}") + "_" + df_copy[col]

    return out_series