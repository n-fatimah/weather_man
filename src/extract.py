import logging
import os
import shutil

from enums import FileDestination, FilePrefix


class Extractor:
    """
    Arguments: path and year
    """

    def __init__(self, path, year):
        self.path = path
        self.year = year
        self.destination = FileDestination.EXTRACTED_FILES.value

    def extract_files(self):
        """
        Description: Extracts and copies weather data files from the source directory to the destination directory.

        Returns:
            None
        """

        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)
        os.makedirs(self.destination)

        prefix = FilePrefix.MURREE_WEATHER.value
        for file_name in os.listdir(self.path):
            if file_name.startswith(f"{prefix}{self.year}"):
                full_file_name = os.path.join(self.path, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, self.destination)

        logging.info(f"Files extracted to {self.destination}")
