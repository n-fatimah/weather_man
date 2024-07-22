# weather_man

Virtual Environment

sudo apt update
sudo apt install python3-venv
rm -rf .env
python3 -m venv .env
ls -l .env/bin
source .env/bin/activate

import os
import shutil
import logging

class Extractor:
    def __init__(self, path, year):
        self.path = path
        self.year = year
        self.destination = "extracted_files"

    def extract_files(self):
        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)
            print(f"Removed existing directory: {self.destination}")
        os.makedirs(self.destination)
        print(f"Created directory: {self.destination}")

        for file_name in os.listdir(self.path):
            if file_name.startswith(f"Murree_weather_{self.year}"):
                full_file_name = os.path.join(self.path, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, self.destination)
                    print(f"Copied: {full_file_name} to {self.destination}")

        print(f"Files extracted to {self.destination}")




import os
import argparse
import pandas as pd
from collections import namedtuple

WeatherReading = namedtuple('WeatherReading', ['date', 'max_temp', 'min_temp', 'mean_temp', 'humidity'])

def parse_weather_file(file_path):
    data = pd.read_csv(file_path, delimiter=',', usecols=['PKT', 'Max TemperatureC', 'Min TemperatureC', 'Mean TemperatureC', 'Max Humidity'])
    data = data.rename(columns={'PKT': 'date', 'Max TemperatureC': 'max_temp', 'Min TemperatureC': 'min_temp', 'Mean TemperatureC': 'mean_temp', 'Max Humidity': 'humidity'})
    return [WeatherReading(row.date, row.max_temp, row.min_temp, row.mean_temp, row.humidity) for _, row in data.iterrows()]

def load_weather_data(files_dir):
    readings = []
    for filename in os.listdir(files_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(files_dir, filename)
            readings.extend(parse_weather_file(file_path))
    return readings

def generate_year_report(readings, year):
    yearly_readings = [r for r in readings if r.date.startswith(str(year))]
    if not yearly_readings:
        print(f"No data found for year {year}")
        return
    highest = max(yearly_readings, key=lambda r: r.max_temp if r.max_temp is not None else float('-inf'))
    lowest = min(yearly_readings, key=lambda r: r.min_temp if r.min_temp is not None else float('inf'))
    humidity = max(yearly_readings, key=lambda r: r.humidity if r.humidity is not None else float('-inf'))
    print(f"Highest: {highest.max_temp}C on {highest.date}")
    print(f"Lowest: {lowest.min_temp}C on {lowest.date}")
    print(f"Humidity: {humidity.humidity}% on {humidity.date}")

def generate_month_report(readings, year, month):
    monthly_readings = [r for r in readings if r.date.startswith(f"{year}-{month:02d}")]
    if not monthly_readings:
        print(f"No data found for {year}/{month:02d}")
        return
    avg_high_temp = sum(r.max_temp for r in monthly_readings if r.max_temp is not None) / len(monthly_readings)
    avg_low_temp = sum(r.min_temp for r in monthly_readings if r.min_temp is not None) / len(monthly_readings)
    avg_mean_humidity = sum(r.humidity for r in monthly_readings if r.humidity is not None) / len(monthly_readings)
    print(f"Highest Average: {avg_high_temp:.2f}C")
    print(f"Lowest Average: {avg_low_temp:.2f}C")
    print(f"Average Mean Humidity: {avg_mean_humidity:.2f}%")

def generate_chart(readings, year, month):
    monthly_readings = [r for r in readings if r.date.startswith(f"{year}-{month:02d}")]
    if not monthly_readings:
        print(f"No data found for {year}/{month:02d}")
        return
    print(f"{year}/{month:02d}")
    for reading in monthly_readings:
        if reading.max_temp is not None:
            print(f"{reading.date[-2:]} {'+' * int(reading.max_temp)} {reading.max_temp}C")
        if reading.min_temp is not None:
            print(f"{' ' * 3}{'+' * int(reading.min_temp)} {reading.min_temp}C")

def main():
    parser = argparse.ArgumentParser(description="Weather data report generator")
    parser.add_argument("files_dir", help="Directory containing weather data files")
    parser.add_argument("-e", "--year", type=int, help="Generate report for a given year")
    parser.add_argument("-a", "--average", type=str, help="Generate average report for a given month (format: YYYY/MM)")
    parser.add_argument("-c", "--chart", type=str, help="Generate bar chart for a given month (format: YYYY/MM)")
    args = parser.parse_args()

    readings = load_weather_data(args.files_dir)

    if args.year:
        generate_year_report(readings, args.year)
    if args.average:
        year, month = map(int, args.average.split('/'))
        generate_month_report(readings, year, month)
    if args.chart:
        year, month = map(int, args.chart.split('/'))
        generate_chart(readings, year, month)

if __name__ == "__main__":
    main()






###
import os
import sys
import pandas as pd

def parse_command_line_args():
    if len(sys.argv) != 3:
        print("invalid")
        sys.exit(1)

    directory = sys.argv[1]
    command = sys.argv[2]
    if not command.startswith("-e "):
        print("Invalid command")
        sys.exit(1)

    year = command.split()[1]
    return directory, year

def read_and_parse_files(directory, year):
    data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt") and year in filename:
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, parse_dates=['PKT'], dayfirst=True)
            data.append(df)

    return pd.concat(data, ignore_index=True)

def generate_yearly_report(df, year):
    df['Year'] = pd.DatetimeIndex(df['PKT']).year
    year_data = df[df['Year'] == int(year)]

    if year_data.empty:
        print(f"No data found for year {year}")
        return

    highest_temp_row = year_data.loc[year_data['Max TemperatureC'].idxmax()]
    lowest_temp_row = year_data.loc[year_data['Min TemperatureC'].idxmin()]
    highest_humidity_row = year_data.loc[year_data['Max Humidity'].idxmax()]

    highest_temp = highest_temp_row['Max TemperatureC']
    highest_temp_date = highest_temp_row['PKT'].strftime('%B %d')

    lowest_temp = lowest_temp_row['Min TemperatureC']
    lowest_temp_date = lowest_temp_row['PKT'].strftime('%B %d')

    highest_humidity = highest_humidity_row['Max Humidity']
    highest_humidity_date = highest_humidity_row['PKT'].strftime('%B %d')

    print(f"Highest: {highest_temp}C on {highest_temp_date}")
    print(f"Lowest: {lowest_temp}C on {lowest_temp_date}")
    print(f"Humidity: {highest_humidity}% on {highest_humidity_date}")

def main():
    directory, year = parse_command_line_args()
    df = read_and_parse_files(directory, year)
    generate_yearly_report(df, year)

if __name__ == "__main__":
    main()





