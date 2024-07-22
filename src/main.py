import argparse
from extract import Extractor
from parser_reader import ParserReader
from calculate import YearlyComputations, MonthlyComputations, ChartDataGeneration
from typing import List
import sys
from pathlib import Path
import logging
import os

"""
Main function to process weather data based on user input from command line arguments.

Argument Parsing:** Uses argparse to parse the command line arguments:
    path: The path to the weather data files.
    -e or --year: Year for computing yearly report.
    -c or --month: Month for computing monthly report.
    -a or --chart: Month for generating chart data.

    If `month` is provided, computes monthly statistics using the `MonthlyComputations` class.
    If `chart` is provided, generates chart data using the `ChartDataGeneration` class.
    If `year` is provided, computes yearly statistics using the `YearlyComputations` class.

Returns:
    None
"""
logging.basicConfig(level=logging.INFO)
def main() -> None:
    parser = argparse.ArgumentParser(description="Weather Man")
    parser.add_argument('path', type=str)
    parser.add_argument('-e', '--year')
    parser.add_argument('-c', '--month')
    parser.add_argument('-a', '--chart')

    args = parser.parse_args()
    logging.info(args.year)
    logging.info(args.month)
    logging.info(args.chart)


    if args.year is None and args.month is None and args.chart is None:
        logging.error(f"Command does not include year month or chart instructions")
        sys.exit(1)

    if args.year:
        year = int(args.year)


    if args.month:
        year,month= int(args.month.split("/"))
        if month<0 or month >12:
            logging.info(f"The month in the command is not valid.")

    if args.chart:
        year,month = int(args.chart.split("/"))
        logging.info(f"{month}")
        if month<0 or month >12:
            logging.info(f"The month in the command is not valid.")

    file_root = str(Path(__file__).resolve().parent.parent)
    full_path = os.path.join(file_root, args.path)

    extractor = Extractor(full_path, year)
    extractor.extract_files()

    weather_parser= ParserReader(extractor.destination)
    readings = weather_parser.parse_files()

    if args.month:
        computations = MonthlyComputations(readings)
        computations.compute_monthly(args.month)


    if args.chart:
        chart_gen = ChartDataGeneration(readings)
        chart_gen.generate_chart_data(args.chart)

    if args.year:
        yearly_computations = YearlyComputations(readings)
        yearly_computations.compute_yearly(str(args.year))

if __name__ == "__main__":
    main()
