import logging
from typing import List

logging.basicConfig(level=logging.INFO)


class WeatherReading:
    """
    Initializes a WeatherReading object with the given data.

    Args:
        data (List[str])
            data[0] is the date of the reading.
            data[1] is the maximum temperature.
            data[3] is the minimum temperature.
            data[7] is the humidity.
    """

    def __init__(self, data: List[str]):
        self.date = data[0] if data[0] else None
        self.max_temp = int(data[1]) if data[1] else None
        self.min_temp = int(data[3]) if data[3] else None
        self.humidity = int(data[7]) if data[7] else None



