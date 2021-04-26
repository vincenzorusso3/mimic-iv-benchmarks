from __future__ import absolute_import
from __future__ import print_function

import pandas as pd


def dataframe_from_csv(path, header=0, index_col=False):
    df=pd.read_csv(path, header=header, index_col=index_col)
    df.columns = df.columns.str.upper()
    
    ## devo trasformare STAY_ID in ICUSTAY_ID
    df.rename(columns = {"STAY_ID": "ICUSTAY_ID",
                          "ICD_CODE":"ICD9_CODE"}, 
          inplace = True)
    #print(df.columns)
    #print(df.columns)
    #return pd.read_csv(path, header=header, index_col=index_col)
    return df
