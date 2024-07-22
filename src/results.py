class YearlyResult:
    def __init__(
        self,
        highest_temp,
        highest_temp_date,
        lowest_temp,
        lowest_temp_date,
        highest_humidity,
        highest_humidity_date,
    ):
        self.highest_temp = highest_temp
        self.highest_temp_date = highest_temp_date
        self.lowest_temp = lowest_temp
        self.lowest_temp_date = lowest_temp_date
        self.highest_humidity = highest_humidity
        self.highest_humidity_date = highest_humidity_date


class MonthlyResult:
    def __init__(self, avg_highest_temp, avg_lowest_temp, avg_humidity):
        self.avg_highest_temp = avg_highest_temp
        self.avg_lowest_temp = avg_lowest_temp
        self.avg_humidity = avg_humidity


class ChartData:
    def __init__(self, data):
        self.data = data
