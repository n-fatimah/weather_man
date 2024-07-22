import logging
from collections import defaultdict
from results import YearlyResult, MonthlyResult, ChartData

logging.basicConfig(level=logging.INFO)
class Computations:
    def __init__(self, readings):
        self.readings = readings

    """

    Args: year from main.py
    returns :
                highest_temp,
                highest_temp_date,
                lowest_temp,
                lowest_temp_date,
                highest_humidity,
                highest_humidity_date,
    """

    def compute_yearly(self, year):
        highest_temp = float("-inf")
        lowest_temp = float("inf")
        highest_humidity = float("-inf")
        highest_temp_date = ""
        lowest_temp_date = ""
        highest_humidity_date = ""

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

        return YearlyResult(
            highest_temp,
            highest_temp_date,
            lowest_temp,
            lowest_temp_date,
            highest_humidity,
            highest_humidity_date,
        )

    def compute_monthly(self, month):
        """_summary_

        Args:
            month (): _description_

        Returns:
            int:averages of temperatures and humidity
            month YYYY/MM
        """
        total_max_temp = 0
        total_min_temp = 0
        total_humidity = 0
        count = 0

        if month:
            year=month.split("/")[0]
            m=month.split("/")[1]

            year_month_combination=year+'-'+m


        for reading in self.readings:
            if reading.date.startswith(year_month_combination):
                if reading.max_temp:
                    total_max_temp += reading.max_temp
                if reading.min_temp:
                    total_min_temp += reading.min_temp
                if reading.humidity:

                    total_humidity += reading.humidity
                count += 1


        return MonthlyResult(
            total_max_temp // count, total_min_temp // count, total_humidity // count
        )

    """
    Generates  chart
    """
    def generate_chart_data(self, month):

        chart_data = defaultdict(list)


        if month:
            year=month.split("/")[0]
            m=month.split("/")[1]
            year_month_combination=year+'-'+m


        for reading in self.readings:
            if reading.date.startswith(year_month_combination):
                day = reading.date.split("-")[-1]
                chart_data[day].append(reading.max_temp)
                chart_data[day].append(reading.min_temp)
        logging.info("done with chart data")
        return ChartData(chart_data)
