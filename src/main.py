import argparse
import logging
import os
import sys
from pathlib import Path

from calculate import Computations
from extract import Extractor
from parser_reader import ParserReader
from report import ReportGenerator

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.error)


"""
argument parsing based on commands
"""


def main():
    parser = argparse.ArgumentParser(description="Weather Man")
    parser.add_argument("path")
    parser.add_argument("-e", "--year")
    parser.add_argument("-c", "--month")
    parser.add_argument("-a", "--chart")

    args = parser.parse_args()
    logging.info(args.year)
    logging.info(args.month)
    logging.info(args.chart)

    if args.year is None and args.month is None and args.chart is None:
        logging.error("Command does not include year month or chart instructions")
        sys.exit(1)

    if args.year:
        year = int(args.year)

    if args.month:
        year=int(args.month.split("/")[0])
        month=int(args.month.split("/")[1])
        logging.info(month,year)

    if args.chart:
        year=int(args.chart.split("/")[0])
        month=int(args.chart.split("/")[1])
        logging.info(month,year)




    file_root = str(Path(__file__).resolve().parent.parent)

    full_path = os.path.join(file_root, args.path)
    logging.info(f"full path path {full_path}")

    extractor = Extractor(full_path, year)
    extractor.extract_files()

    weather_parser = ParserReader(extractor.destination)
    readings = weather_parser.parse_files()

    computations = Computations(readings)
    report_generator = ReportGenerator()

    if args.year:
        result = computations.compute_yearly(args.year)
        report_generator.generate_yearly_report(result)
    if args.month:
        result = computations.compute_monthly(args.month)
        report_generator.generate_monthly_report(result)
    if args.chart:
        chart_data = computations.generate_chart_data(args.chart)
        report_generator.generate_chart(chart_data)


if __name__ == "__main__":
    logging.info("Program is starting")
    main()
