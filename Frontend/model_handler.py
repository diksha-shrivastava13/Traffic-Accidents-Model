import bentoml
from xgboost import XGBRegressor as xgb
from encoding import encode_categories, encode_types
import pandas as pd
model = xgb()
model.load_model("/Users/DELL/PycharmProjects/Traffic-Accidents-Model/models/model_file_name.json")
bento_model = bentoml.xgboost.save_model("my_xgboost_model", model)
loaded_model = bentoml.xgboost.load_model("my_xgboost_model")


def make_local_request(input_data):
    input_array = list(input_data.values())
    # input_array = list(input_df.values)[0].tolist()
    input_array = encode_categories(input_array[2], input_array)
    input_array = encode_types(input_array[3], input_array)
    print(input_array)

    def validate_data(input_array: list[int]) -> bool:
        year = input_array[0][0]
        month = input_array[0][1]
        binary_values = input_array[0][2:]
        if not (2000 <= year <= 2020):
            return False
        if not (1 <= month <= 12):
            return False
        if not all(val in {0, 1} for val in binary_values):
            return False
        return True

    if not validate_data(input_array):
        return -1

    prediction = loaded_model.predict(input_array)
    return prediction
