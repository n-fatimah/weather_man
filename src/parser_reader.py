import logging
import os
from typing import List

from reading import WeatherReading


class ParserReader:
    def __init__(self, path: str):
        self.path = path

    def parse_files(self) -> List[WeatherReading]:
        """
        Description: Parses weather data files.

        Returns:
            List[WeatherReading]: A list of `WeatherReading` objects created from the parsed files.

        """
        readings = []
        for file_name in os.listdir(self.path):
            full_file_name = os.path.join(self.path, file_name)
            if os.path.isfile(full_file_name):
                with open(full_file_name, "r") as file:
                    next(file)
                    readings = [
                        WeatherReading(line.strip().split(",")) for line in file
                    ]

        logging.info("Files parsed successfully")
        return readings

    def format_weather_reading(reading: WeatherReading) -> str:
        """
        The function to format the Weather reading Object to verify output
        """
        return (
            f"Date: {reading.date}, Max Temp: {reading.max_temp}C, "
            f"Min Temp: {reading.min_temp}C, Humidity: {reading.humidity}%"
        )
