from collections import defaultdict
from datetime import datetime
from typing import Dict, List


from reading import WeatherReading
import formatDate

class YearlyComputations:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    def compute_yearly(self, year: str) -> Dict[str, str]:
        """
        Description: Computes the highest temperature, lowest temperature, and  humidity for a given year.

        Argument: year

        Returns:
            Dict[str, str]: A dictionary with formatted strings for the highest temperature, lowest temperature, and highest humidity.
        """

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

        highest_temp_date_str = formatDate.format_date(highest_temp_date)
        lowest_temp_date_str = formatDate.format_date(lowest_temp_date)
        highest_humidity_date_str = formatDate.format_date(highest_humidity_date)

        result = {
            "highest_temp": f"Highest: {highest_temp}C on {highest_temp_date_str}",
            "lowest_temp": f"Lowest: {lowest_temp}C on {lowest_temp_date_str}",
            "highest_humidity": f"Humidity: {highest_humidity}% on {highest_humidity_date_str}",
        }

        return result

    def print_yearly_report(self, result : Dict[str, str]):
        """
        Description: To print the yearly report
        Argument: result

        """
        [print(value) for value in result.values()]



class MonthlyComputations:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    def compute_monthly(self, month: str) -> Dict[str, str]:
        """
        Description: Computes the average maximum temperature, average minimum temperature, and average humidity for a specified month.

        Argument: month

        Returns:
            Dict[str, str]: A dictionary with formatted strings for the average maximum temperature, average minimum temperature, and average humidity.
        """
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

        if count == 0:
            result = {"avg_max_temp": 0, "avg_min_temp": 0, "avg_humidity": 0}
        else:
            result = {
                "avg_max_temp": f"Highest Average {total_max_temp // count}C",
                "avg_min_temp": f"Lowest AVerage {total_min_temp // count}C",
                "avg_humidity": f"Average Humidity {total_humidity // count}%",
            }

        return result

    def print_monthly_report(self, result : Dict[str, str]):
        """
        Description: print the dict returned from compute_monthly

        Args:
            result
        """
        [print(value) for value in result.values()]


class ChartDataGeneration:
    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    """
    Description: Generates a dictionary of  data for a specified month.

    Argument: month

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
        return self.print_non_none_days(chart_data)

    """
    Description: Prints the days of the month with recorded temperature data.

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

