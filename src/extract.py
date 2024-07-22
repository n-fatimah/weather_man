
import logging
import os
import shutil


class Extractor:
    def __init__(self, path, year):
        self.path = path
        self.year = year
        self.destination = "extracted_files"

    def extract_files(self):

        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)
            print("removed")
        os.makedirs(self.destination)
        print("created")


        for file_name in os.listdir(self.path):
            # print("in for ",self.path)
            if file_name.startswith(f"Murree_weather_{self.year}"):
                full_file_name = os.path.join(self.path, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, self.destination)
                    logging.info(f"Copied: {full_file_name} to {self.destination}")

        logging.info(f"Files extracted to {self.destination}")


