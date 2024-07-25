import argparse
import logging
import os
import sys
from pathlib import Path

import argument_parse
from calculate import ChartDataGeneration, MonthlyComputations, YearlyComputations
from extract import Extractor
from parser_reader import ParserReader

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """
    Main function to process weather data based on user input from command line arguments.

    Argument Parsing:
        path: The path to the weather data files.
        -e or --year: Year for computing yearly report.
        -c or --month: Month for computing monthly report.
        -a or --chart: Month for generating chart data.
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Weather Man")
    parser.add_argument("path", type=str)
    parser.add_argument("-e", "--year")
    parser.add_argument("-c", "--month")
    parser.add_argument("-a", "--chart")

    args = parser.parse_args()
    logging.info(type(args.year))
    logging.info(type(args.month))
    logging.info(type(args.chart))

    if not args.year and not args.month and not args.chart:
        logging.error("Command does not include year month or chart instructions")
        sys.exit(1)

    if args.year:
        year = int(args.year)
        logging.info(f"The year for this query is {year}")

    if args.month:
        year, month = argument_parse.validate_month_year(args.month)
        print(year, month)

    if args.chart:
        year, month = argument_parse.validate_month_year(args.chart)

    file_root = str(Path(__file__).resolve().parent.parent)
    full_path = os.path.join(file_root, args.path)

    extractor = Extractor(full_path, year)
    extractor.extract_files()

    weather_parser = ParserReader(extractor.destination)
    readings = weather_parser.parse_files()

    if args.month:
        computations = MonthlyComputations(readings)
        result = computations.compute_monthly(args.month)
        computations.print_monthly_report(result)

    if args.chart:
        chart_gen = ChartDataGeneration(readings)
        chart_data = chart_gen.generate_chart_data(args.chart)
        chart_gen.print_non_none_days(chart_data)

    if args.year:
        yearly_computations = YearlyComputations(readings)
        result = yearly_computations.compute_yearly(args.year)
        yearly_computations.print_yearly_report(result)


if __name__ == "__main__":
    main()
