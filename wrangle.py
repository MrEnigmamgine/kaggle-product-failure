# Core DS libraries
import numpy as np
import pandas as pd

# Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

#####################################################
#               CONFIG VARIABLES                    #
#####################################################

SEED = 8
FEATURES = []
TARGETS = ['failure']
ENVFILE = './env.py'
CSV='./data/train.csv'
DB= ''
SQLQUERY ="""

"""
#####################################################
#               END CONFIG VARIABLES                #
#####################################################


## Generic split data function
def train_test_validate_split(df, seed=SEED, stratify=None):
    """Splits data 60%/20%/20%"""
    from sklearn.model_selection import train_test_split
    # First split off our testing data.
    train, test_validate = train_test_split(
        df, 
        train_size=3/5, 
        random_state=seed, 
        stratify=( df[stratify] if stratify else None)
    )
    # Then split the remaining into train/validate data.
    test, validate = train_test_split(
        test_validate,
        train_size=1/2,
        random_state=seed,
        stratify= (test_validate[stratify] if stratify else None)
    )
    return train, test, validate

def get_potatoes():
    df = pd.read_csv(CSV, index_col=0)
    train, test, validate = train_test_validate_split(df)


    return train, test, validate

def impute_potatoes(train, test, validate):
    imputeCols = train.select_dtypes(include=np.number).columns.tolist()
    from sklearn.impute import SimpleImputer
    imputer =  SimpleImputer()
    imputer.fit(train[imputeCols])
    train[imputeCols] = imputer.transform(train[imputeCols])
    test[imputeCols] = imputer.transform(test[imputeCols])
    validate[imputeCols] = imputer.transform(validate[imputeCols])

    return train, test, validate

def wrangle_potatoes():
    return impute_potatoes(*get_potatoes())