import logging
from datetime import datetime


def format_date(temp_date):
    """
    Formats the date string to 'Month Day' format.
    And if the date_str is None, return string Unknown date for now,

    Args:
        date_str

    The formatted date string or None if date_str is None.
    """
    if temp_date:
        try:
            date_str= datetime.strptime(temp_date, "%Y-%m-%d").strftime("%B %d")
            if date_str is None:
                return "Unknown Date"
            else:
                return date_str
        except:
            logging.error("Error in fetching date.")
    return None
