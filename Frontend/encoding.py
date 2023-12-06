from typing import List
from pydantic import BaseModel
import bentoml


class InputSchema(BaseModel):
    year: int
    month: int
    category: str
    type: str


class OutputSchema(BaseModel):
    prediction: float


def encode_categories(category: str, lst: list[int]) -> list[int]:
    category_mapping = {
        "alcohol accidents": [1, 0, 0],
        "escape accidents": [0, 1, 0],
        "traffic accidents": [0, 0, 1],
    }

    category_values = category_mapping.get(category.lower(), [0])
    lst.extend(category_values)

    return lst


def encode_types(types: str, lst: List[int]) -> List[int]:
    type_mapping = {
        "injured and killed": [1, 0, 0],
        "total": [0, 1, 0],
        "with personal injury": [0, 0, 1],
    }
    type_values = type_mapping.get(types.lower(), [0])
    lst.extend(type_values)

    del lst[2]
    del lst[2]
    return [lst]

