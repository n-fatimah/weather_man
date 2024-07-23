import logging
import os
from typing import List

from reading import WeatherReading


class ParserReader:
    def __init__(self, path: str):
        self.path = path

    """
    Parses weather data files.
    The method iterates through each file in the directory specified by `self.path`. 
    For each file, it reads the content line by line. 
    Each line is split by commas to extract weather data,

    Prints a confirmation message "Files parsed successfully" once all files are processed.
    Returns:
        List[WeatherReading]: A list of `WeatherReading` objects created from the parsed files.

    """

    def parse_files(self) -> List[WeatherReading]:
        readings = []
        for file_name in os.listdir(self.path):
            full_file_name = os.path.join(self.path, file_name)
            if os.path.isfile(full_file_name):
                with open(full_file_name, "r") as file:
                    next(file)
                    readings = [WeatherReading(line.strip().split(",")) for line in file]

        logging.info(f"Files parsed successfully")
        return readings


    """
    The function to format the Weatherreading Object to verify output 
    """
    def format_weather_reading(reading: WeatherReading) -> str:
        return (f"Date: {reading.date}, Max Temp: {reading.max_temp}C, "
                f"Min Temp: {reading.min_temp}C, Humidity: {reading.humidity}%")