import pickle
import os
from pathlib import Path
from .tf import Model


class RegressionModel(Model): pass


pickled_model_file_path = os.path.join(Path(__file__).resolve().parent, "real_estate_model_v2.pkl")
model = RegressionModel(pickle.load(open(pickled_model_file_path, "rb")))


def predict_market_value(district: str, bedroom_count: int, area: int) -> int:
    return model.predict(district=district, bedroom_count=bedroom_count, area=area)
