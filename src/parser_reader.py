
import os
import logging
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
                    next(file)  # Skip header
                    for line in file:
                        data = line.strip().split(",")
                        reading = WeatherReading(data)
                        readings.append(reading)
                        

        logging.info(f"Files parsed successfully")
        return readings
