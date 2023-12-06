import bentoml
from xgboost import XGBRegressor as xgb
model = xgb()
model.load_model("/Users/DELL/PycharmProjects/Traffic-Accidents-Model/models/model_file_name.json")
bento_model = bentoml.xgboost.save_model("my_xgboost_model", model)
loaded_model = bentoml.xgboost.load_model("my_xgboost_model")
