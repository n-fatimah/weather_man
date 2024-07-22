import os
import logging
from reading import WeatherReading
logging.basicConfig(level=logging.INFO)


class ParserReader:
    def __init__(self, path):
        self.path = path
        """
        path: destination path of extracted files 
        """
    def parse_files(self):
        readings = []
        for file_name in os.listdir(self.path):
            logging.info('filename', file_name)
            full_file_name = os.path.join(self.path, file_name)
            logging.info("full file name",full_file_name)
            if os.path.isfile(full_file_name):
                with open(full_file_name, "r") as file:
                    next(file)
                    for line in file:
                        data = line.strip().split(",")
                        readings.append(WeatherReading(data))

        logging.info("Files parsed successfully")

        return readings
