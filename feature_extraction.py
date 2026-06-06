def create_features(df):

    # BMI Risk
    df['bmi_risk'] = df['bmi'].apply(
        lambda x: 2 if x >= 30 else 1 if x >= 25 else 0
    )

    # Glucose Risk
    df['glucose_risk'] = df['blood_glucose_level'].apply(
        lambda x: 2 if x >= 126 else 1 if x >= 100 else 0
    )

    # Interaction Features
    df['bmi_hypertension'] = (
        df['bmi'] * df['hypertension']
    )

    df['hba1c_glucose'] = (
        df['HbA1c_level'] *
        df['blood_glucose_level']
    )

    return df