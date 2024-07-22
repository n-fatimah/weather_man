class WeatherReading:
    def __init__(self, data):
        self.date = data[0]
        self.max_temp = int(data[1]) if data[1] else None
        self.min_temp = int(data[3]) if data[3] else None
        self.humidity = int(data[7]) if data[7] else None


