import os
from datetime import datetime


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formatted_date


def display_cwd():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")


def display_entries_in_directory(directory):
    # os.list
    entries = os.scandir(directory)
    for entry in entries:
        print(entry.name)

