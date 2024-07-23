from collections import defaultdict
from datetime import datetime
from typing import Dict, List

from reading import WeatherReading


class YearlyComputations:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    """
    Computes the highest temperature, lowest temperature, and  humidity for a given year.

       initializes variables to track the highest and lowest temperatures and humidity, along with their corresponding dates.
       Uses `float("-inf")` and `float("inf")` for initial comparisons.
       Updates the highest temperature, lowest temperature, and highest humidity.

       Converts the dates of the highest temperature, lowest temperature, and highest humidity from `'%Y-%m-%d'` format to `'%B %d'` format.
       Uses `datetime.strptime` and `strftime` for date formatting, ensuring `None` is handled if no date is available.

       Creates a dictionary with formatted strings for the highest temperature, lowest temperature, and highest humidity.
       Prints each value in the result dictionary.

    Returns:
        Dict[str, str]: A dictionary with formatted strings for the highest temperature, lowest temperature, and highest humidity.
    """

    def compute_yearly(self, year: str) -> Dict[str, str]:
        highest_temp = float("-inf")
        lowest_temp = float("inf")
        highest_humidity = float("-inf")
        highest_temp_date = None
        lowest_temp_date = None
        highest_humidity_date = None

        for reading in self.readings:
            if reading.date.startswith(year):
                if reading.max_temp is not None and reading.max_temp > highest_temp:
                    highest_temp = reading.max_temp
                    highest_temp_date = reading.date
                if reading.min_temp is not None and reading.min_temp < lowest_temp:
                    lowest_temp = reading.min_temp
                    lowest_temp_date = reading.date
                if reading.humidity is not None and reading.humidity > highest_humidity:
                    highest_humidity = reading.humidity
                    highest_humidity_date = reading.date

        highest_temp_date_str = (
            datetime.strptime(highest_temp_date, "%Y-%m-%d").strftime("%B %d")
            if highest_temp_date
            else None
        )
        lowest_temp_date_str = (
            datetime.strptime(lowest_temp_date, "%Y-%m-%d").strftime("%B %d")
            if lowest_temp_date
            else None
        )
        highest_humidity_date_str = (
            datetime.strptime(highest_humidity_date, "%Y-%m-%d").strftime("%B %d")
            if highest_humidity_date
            else None
        )

        result = {
            "highest_temp": f"Highest: {highest_temp}C on {highest_temp_date_str}",
            "lowest_temp": f"Lowest: {lowest_temp}C on {lowest_temp_date_str}",
            "highest_humidity": f"Humidity: {highest_humidity}% on {highest_humidity_date_str}",
        }

        [print(value) for value in result.values()]

        return result


class MonthlyComputations:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    """
    Computes the average maximum temperature, average minimum temperature, and average humidity for a specified month.

        Splits the input `month` string into year and month.
        Constructs a year-month combination string for filtering readings.
        Accumulates the total maximum temperature, total minimum temperature, and total humidity, and increments the count for each reading.

        Checks if there are any valid readings (`count > 0`). If not, sets default values of 0 for the averages.
        Computes the average maximum temperature, average minimum temperature, and average humidity.

        Creates a dictionary with formatted strings for the average maximum temperature, average minimum temperature, and average humidity.

    Returns:
        Dict[str, str]: A dictionary with formatted strings for the average maximum temperature, average minimum temperature, and average humidity.
    """

    def compute_monthly(self, month: str) -> Dict[str, str]:
        total_max_temp = 0
        total_min_temp = 0
        total_humidity = 0
        count = 0

        year, m = month.split("/")
        year_month_combination = f"{year}-{m}"

        for reading in self.readings:
            if reading.date.startswith(year_month_combination):
                if reading.max_temp:
                    total_max_temp += reading.max_temp
                if reading.min_temp:
                    total_min_temp += reading.min_temp
                if reading.humidity:
                    total_humidity += reading.humidity
                count += 1

        if count <= 0:
            result = {
                "avg_max_temp": 0,
                "avg_min_temp": 0,
                "avg_humidity": 0
            }
        else:
            result = {
                "avg_max_temp": f"Highest Average {total_max_temp // count}C",
                "avg_min_temp": f"Lowest AVerage {total_min_temp // count}C",
                "avg_humidity": f"Average Humidity {total_humidity // count}%",
            }

        [print(value) for value in result.values()]
        return result


class ChartDataGeneration:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    """
    Generates a dictionary of  data for a specified month.

    Splits the input `month` string into year and month.
    Constructs a year-month combination string for filtering readings.
    Extracts the day from the date and appends the maximum and minimum temperatures to the list for that day in the dictionary.

    Prints the month and year in the format "MM YYYY".
    Calls `print_non_none_days` to print the days with valid temperature data.

    Returns:
        Dict[str, List[int]]: A dictionary where the keys are days of the month and the values are lists containing the maximum and minimum temperatures recorded on that day.
    """

    def generate_chart_data(self, month: str) -> Dict[str, List[int]]:
        chart_data = defaultdict(list)

        year, month_ = month.split("/")
        year_month_combination = f"{year}-{month_}"

        for reading in self.readings:
            if reading.date.startswith(year_month_combination):
                day = reading.date.split("-")[-1]
                chart_data[day].append(reading.max_temp)
                chart_data[day].append(reading.min_temp)
        self.print_non_none_days(chart_data)
        return chart_data

    """
    Prints the days of the month with recorded temperature data.

    Prints each day along with its maximum and minimum 
    temperatures.
    The number of '+' characters corresponds to the maximum and minimum temperatures recorded for that day.
    Days with `None` values for temperatures are excluded from the output.

    Args:
        chart_data (Dict[str, List[int]])

    Returns:
        None
    """

    def print_non_none_days(self, chart_data: Dict[str, List[int]]):
        for day, temps in chart_data.items():
            max_temp, min_temp = temps
            if max_temp is not None and min_temp is not None:
                print(f"{day} {'+'*int(max_temp)} {max_temp}C")
                print(f"{day} {'+'*int(min_temp)} {min_temp}C")
