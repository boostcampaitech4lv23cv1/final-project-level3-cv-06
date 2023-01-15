from pydantic import BaseModel, validator
import numpy as np


class PredIn(BaseModel):
    category: str

    # @validator(category)
    # def category_validation(cls, v):
    #     if v not in ["animal", "landmark"]:
    #         raise ("This category is not validate")
    #     return v


# class PredOut(BaseModel):
#     image: np.ndarray


class GameIn(BaseModel):
    category: str
    mode: str
