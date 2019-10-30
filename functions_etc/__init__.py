"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

# sample code

# sample datasets
"""
Here are
"""
ONES = pd.DataFrame(np.ones(5))
ZEROS = pd.DataFrame(np.zeros(20))

# sample functions
"""

"""


def decriment(x):
    return (x - 1)


"""
Class

"""

class Dataframes:
    """
    a class of dataframe inspection functions
    """

    def __init__(self, df):
        self.df = df
        self.nulz = nul_values
        self.val_norm = normalized_value_count


    """
    2 helper functions/methods
    """


    def nulz(self):
         """
         first helper function to look for nul values
         """
         return self.df.isna().sum()


    def val_norm(self):
        """
        2nd helper function to look for value countes
        """
        return self.df.value_counts(normalize=True)


#DF1 = Dataframes()

#print(DF1.nul_values)
#print(DF1.normalized_value_count)





# #first helper function
# def nulz(DF):
#     return(print(DF.isna().sum()))
#
#
# #2nd helper functions
# def val_norm(DF):
#     return(print(DF.value_counts(normalize=True)))
