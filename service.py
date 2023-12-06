import pandas as pd
import bentoml
from bentoml.io import JSON
from encoding import InputSchema, OutputSchema, encode_categories, encode_types

runner = bentoml.xgboost.get("my_xgboost_model:latest").to_runner()
svc = bentoml.Service("accidents-regressor", runners=[runner])


@svc.api(input=JSON(pydantic_model=InputSchema), output=JSON(pydantic_model=OutputSchema))
async def accidents_regression(input_data: InputSchema) -> OutputSchema:
    input_df = pd.DataFrame([input_data.model_dump()])
    input_array = list(input_df.values)[0].tolist()
    input_array = encode_categories(input_data.category, input_array)
    input_array = encode_types(input_data.type, input_array)
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
        return OutputSchema(prediction=0)

    prediction = await runner.predict.async_run(input_array)
    return OutputSchema(prediction=prediction)
