
import logging
import os
import shutil

from enum import Enum

class File_Prefix(Enum):
    MURREE_WEATHER = "Murree_weather_"

class Extractor:
    """
    Args: path and year
    """
    def __init__(self, path, year):
        self.path = path
        self.year = year
        self.destination = "extracted_files"


    """
    Extracts and copies weather data files from the source directory to the destination directory.

     If the destination directory already exists, it is removed using shutil.rmtree.
     A new empty destination directory is created using os.makedirs.

    Iterates over the files in the source directory (`self.path`).
    Filters files based on a prefix (`File_Prefix.MURREE_WEATHER.value`) and the specified year (`self.year`).
    Copies the filtered files to the destination directory (`self.destination`) using `shutil.copy`.

    Returns:
        None
    """

    def extract_files(self):

        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)
        os.makedirs(self.destination)

        prefix = File_Prefix.MURREE_WEATHER.value
        for file_name in os.listdir(self.path):
            if file_name.startswith(f"{prefix}{self.year}"):
                full_file_name = os.path.join(self.path, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, self.destination)

        logging.info(f"Files extracted to {self.destination}")
        
        return


