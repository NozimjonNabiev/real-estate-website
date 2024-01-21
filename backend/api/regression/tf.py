class Model:
    def __init__(self, *args, **kwargs):
        super().__init__()

    def predict(self, **kwargs):
        DISTRICTS_SCORE = {
            "Bektemir": 1.1,
            "Mirobod": 1.2,
            "Mirzo Ulug'bek": 1.4,
            "Sergeli": 1.0,
            "Olmazor": 1.2,
            "Uchtepa": 1.3,
            "Shaxyontohur": 1.5,
            "Yashnobod": 1.2,
            "Chilonzor": 1.6,
            "Yunusobod": 1.7
        }
        BEDROOM_COUNT_MULTIPLIER = [0, 1.0, 1.8, 2.75, 3.7]
        AVERAGE_AREA_PER_BEDROOM = 30
        BASE_PRICE = 20000
        AVERAGE_PRICE = 36000
        district = kwargs.get("district", "Chilonzor")
        bedroom_count = kwargs.get("bedroom_count", 1)
        area = kwargs.get("area", 32)
        base_price = BASE_PRICE * BEDROOM_COUNT_MULTIPLIER[bedroom_count]
        district_score = DISTRICTS_SCORE[district]
        price = base_price * district_score * (area / bedroom_count / AVERAGE_AREA_PER_BEDROOM) + 275
        price = int(100 * (price // 100))
        return price