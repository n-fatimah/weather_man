import argparse
import logging
import os
import sys
from pathlib import Path
from typing import List

from calculate import ChartDataGeneration, MonthlyComputations, YearlyComputations
from extract import Extractor
from parser_reader import ParserReader

"""
Main function to process weather data based on user input from command line arguments.

Argument Parsing:** Uses argparse to parse the command line arguments:
    path: The path to the weather data files.
    -e or --year: Year for computing yearly report.
    -c or --month: Month for computing monthly report.
    -a or --chart: Month for generating chart data.

    If month is provided, computes monthly statistics.
    If chart is provided, generates chart data.
    If year is provided, computes yearly statistics.

Returns:
    None
"""
logging.basicConfig(level=logging.INFO)


def main() -> None:
    parser = argparse.ArgumentParser(description="Weather Man")
    parser.add_argument("path", type=str)
    parser.add_argument("-e", "--year")
    parser.add_argument("-c", "--month")
    parser.add_argument("-a", "--chart")

    args = parser.parse_args()
    logging.info(type(args.year))
    logging.info(type(args.month))
    logging.info(type(args.chart))

    if args.year is None and args.month is None and args.chart is None:
        logging.error(f"Command does not include year month or chart instructions")
        sys.exit(1)

    if args.year:
        year = int(args.year)
        logging.info(f"The year for this query is {year}")

    if args.month:
        year, month_ = map(int, args.month.split("/"))
        if month_ < 0 or month_ > 12:
            logging.info(f"The month in the command is not valid.")
            sys.exit(1)
        logging.info(f"The month for this query is {month_} and year is {year}")

    if args.chart:
        year, month_ = map(int, args.chart.split("/"))
        if month_ < 0 or month_ > 12:
            logging.info(f"The month in the command is not valid.")
            sys.exit(1)
        logging.info(f"The month for this query is {month_} and year is {year}")

    file_root = str(Path(__file__).resolve().parent.parent)
    full_path = os.path.join(file_root, args.path)

    extractor = Extractor(full_path, year)
    extractor.extract_files()

    weather_parser = ParserReader(extractor.destination)
    readings = weather_parser.parse_files()

    if args.month:
        computations = MonthlyComputations(readings)
        computations.compute_monthly(args.month)

    if args.chart:
        chart_gen = ChartDataGeneration(readings)
        chart_gen.generate_chart_data(args.chart)

    if args.year:
        yearly_computations = YearlyComputations(readings)
        yearly_computations.compute_yearly(args.year)


if __name__ == "__main__":
    main()
