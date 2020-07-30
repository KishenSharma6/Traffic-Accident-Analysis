import pandas as pd
import numpy as np

def missing_counts(dataframe):
    """
    Takes pandas dataframe and returns missing counts,%, and datatype of each column
    """
    missing = pd.DataFrame(dataframe.isna().sum(), columns=['missing_count'])
    missing['missing_%'] = missing.missing_count/len(dataframe) * 100
    missing['data_type'] = list(dataframe.dtypes.values)
    missing = missing.loc[missing['missing_count'] > 0].sort_values(by='missing_count', ascending=False)
    return(missing)
