import logging
logging.basicConfig(level=logging.INFO)

'''
class report generator will generate  the yearly, monthly  reports
And can generate charts based on the command.
Called from main.py from conditional statement.
'''
class ReportGenerator:
    def generate_yearly_report(self, result):
        print(f"Highest: {result.highest_temp}C on {result.highest_temp_date}")
        print(f"Lowest: {result.lowest_temp}C on {result.lowest_temp_date}")
        print(f"Humidity: {result.highest_humidity}% on {result.highest_humidity_date}")

    def generate_monthly_report(self, result):
        print(f"Highest Average: {result.avg_highest_temp}C")
        print(f"Lowest Average: {result.avg_lowest_temp}C")
        print(f"Average Mean Humidity: {result.avg_humidity}%")

    def generate_chart(self, chart_data):
        for day, temps in sorted(chart_data.data.items()):
            print(day,"+"*int(temps[0]), temps[0])
            print(day,"+"*int(temps[1]), temps[1])

