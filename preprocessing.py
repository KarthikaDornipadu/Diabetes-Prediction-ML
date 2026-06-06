import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encode gender
    le_gender = LabelEncoder()
    df['gender'] = le_gender.fit_transform(df['gender'])

    # Encode smoking history
    le_smoking = LabelEncoder()
    df['smoking_history'] = le_smoking.fit_transform(df['smoking_history'])

    return df