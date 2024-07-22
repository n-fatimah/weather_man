
    # print('hello world')

import os
import argparse
import pandas as pd
from collections import namedtuple


def parse_weather_file(file_path):
    data = pd.read_csv(file_path, delimiter=',', usecols=['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Mean TemperatureC', 'Max Humidity'])
    data = data.rename(columns={'PKT': 'date', 'Max TemperatureC': 'max_temp', 'Min TemperatureC': 'min_temp', 'Mean TemperatureC': 'mean_temp', 'Max Humidity': 'humidity'})
    weather_readings = []
    for _, row in data.iterrows():
        date = row.date
        max_temp = row.max_temp
        min_temp = row.min_temp
        mean_temp = row.mean_temp
        humidity = row.humidity

        weather_reading = WeatherReading(date, max_temp, min_temp, mean_temp, humidity)

        weather_readings.append(weather_reading)

    return weather_readings

def load_weather_data(files_dir):
    readings = []
    for filename in os.listdir(files_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(files_dir, filename)
            readings.extend(parse_weather_file(file_path))
    return readings

def main():
    parser = argparse.ArgumentParser(description="Weather data report generator")
    parser.add_argument("files_dir")
    parser.add_argument("-e", type=int,dest='year' )
    parser.add_argument("-a", type=str, dest='average')
    parser.add_argument("-c", type=str,dest='chart')
    args = parser.parse_args()

    readings = load_weather_data(args.files_dir)

    if args.year:
        generate_year_report(readings, args.year)


if __name__ == "__main__":
    main()

