import pickle
from .tf import Model


class RegressionModel(Model): pass


model = RegressionModel(pickle.load(open("real_estate_model_v2.pkl", "rb")))


def predict_market_value(district: str, bedroom_count: int, area: int) -> int:
    return model.predict(district=district, bedroom_count=bedroom_count, area=area)
