import os
from reading import WeatherReading


class ParserReader:
    def __init__(self, path):
        self.path = path

    def parse_files(self):
        readings = []
        for file_name in os.listdir(self.path):
            print('filename', file_name)
            full_file_name = os.path.join(self.path, file_name)
            print("full file name",full_file_name)
            if os.path.isfile(full_file_name):
                with open(full_file_name, "r") as file:
                    next(file)
                    for line in file:
                        data = line.strip().split(",")
                        readings.append(WeatherReading(data))
                    # for line in file:
                    #     data = line.strip().split(",")
                    #     reading = WeatherReading(data)
                    #     print(reading)
                    #     readings.append(reading)

        print("Files parsed successfully")

        return readings
