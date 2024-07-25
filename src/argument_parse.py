import logging
import sys


def validate_month_year(month_year_str: str) -> tuple:
    """
    Description: This function is used for monthly report and generate chart commands to validate the year and month

    Args:
        month_year_str

    Returns:
        tuple
    """
    try:
        year, month = map(int, month_year_str.split("/"))
        if month < 1 or month > 12:
            logging.info("The month in the command is not valid.")
            sys.exit(1)
        logging.info(f"The month for this query is {month} and year is {year}")
        return year, month
    except ValueError as e:
        logging.info("Invalid input for month/year. Ensure the format is YYYY/MM")
        sys.exit(1)
