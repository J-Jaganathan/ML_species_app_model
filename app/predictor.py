import os
import joblib
import pandas as pd

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "encoder.pkl"
)
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)


def preprocess(input_data: dict):
    df = pd.DataFrame([input_data])
    return df

def predict(input_data: dict):
    # Step 1: convert dict → DataFrame
    df = preprocess(input_data)

    # Step 2: split features
    categorical_cols = ["island", "sex"]
    numerical_cols = ["bill_length_mm", "bill_depth_mm",
                      "flipper_length_mm", "body_mass_g"]

    # Step 3: encode categorical features
    encoded_cat = encoder.transform(df[categorical_cols])

    encoded_df = pd.DataFrame(
        encoded_cat,
        columns=encoder.get_feature_names_out(),
        index=df.index
    )

    # Step 4: combine numerical + encoded categorical
    final_input = pd.concat(
        [df[numerical_cols].reset_index(drop=True),
         encoded_df.reset_index(drop=True)],
        axis=1
    )

    # Step 5: prediction
    prediction = model.predict(final_input)

    return prediction[0]

