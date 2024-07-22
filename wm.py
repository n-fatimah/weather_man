import logging
import os
import sys

import pandas as pd


def parse_command_line_args():
    if len(sys.argv) != 3:
        logging.error("Invalid")
        sys.exit(1)

    directory = sys.argv[1]
    command = sys.argv[2]
    if not command.startswith("-e "):
        print("Invalid command")
        sys.exit(1)

    year = command.split()[1]
    return directory, year


def read_and_parse_files(directory: str, year: int):
    data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt") and year in filename:
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, parse_dates=["PKT"], dayfirst=True)
            data.append(df)

    return pd.concat(data, ignore_index=True)


def generate_yearly_report(df, year):
    df["Year"] = pd.DatetimeIndex(df["PKT"]).year
    # year_data = df[df['Year'] == int(year)]
    year_data = df

    if year_data.empty:
        print(f"No data found for year {year}")
        return


    highest_temp_row = year_data.loc[year_data["Max TemperatureC"].idxmax()]
    lowest_temp_row = year_data.loc[year_data["Min TemperatureC"].idxmin()]
    highest_humidity_row = year_data.loc[year_data["Max Humidity"].idxmax()]

    highest_temp = highest_temp_row["Max TemperatureC"]
    highest_temp_date = highest_temp_row["PKT"].strftime("%B %d")

    lowest_temp = lowest_temp_row["Min TemperatureC"]
    lowest_temp_date = lowest_temp_row["PKT"].strftime("%B %d")

    highest_humidity = highest_humidity_row["Max Humidity"]
    highest_humidity_date = highest_humidity_row["PKT"].strftime("%B %d")

    print(f"Highest: {highest_temp}C on {highest_temp_date}")
    print(f"Lowest: {lowest_temp}C on {lowest_temp_date}")
    print(f"Humidity: {highest_humidity}% on {highest_humidity_date}")


def main():
    directory, year = parse_command_line_args()
    df = read_and_parse_files(directory, year)
    generate_yearly_report(df, year)


if __name__ == "__main__":
    main()
