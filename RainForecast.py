import requests
from datetime import datetime, timedelta
import os

LATITUDE = 51.5072
LONGITUDE = -0.1276
DATA_FILE = "weather.txt"


def get_date_from_user():
    date_input = input("Enter date (YYYY-mm-dd) or press Enter for tomorrow: ")

    if date_input == "":
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")

    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        print("Invalid date format.")
        return None


def load_saved_data():
    data = {}

    if not os.path.isfile(DATA_FILE):
        return data

    with open(DATA_FILE, "r") as file:
        for line in file:
            date, value = line.strip().split(",")
            data[date] = float(value)

    return data


def save_result(date, precipitation):
    with open(DATA_FILE, "a") as file:
        file.write(f"{date},{precipitation}\n")


def fetch_weather(date):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        "&daily=precipitation_sum"
        "&timezone=Europe%2FLondon"
        f"&start_date={date}"
        f"&end_date={date}"
    )

    response = requests.get(url)
    data = response.json()

    try:
        return data["daily"]["precipitation_sum"][0]
    except (KeyError, IndexError):
        return None


def print_result(value):
    if value is None or value < 0:
        print("I don't know")
    elif value == 0.0:
        print("It will not rain")
    else:
        print(f"It will rain ({value} mm)")


def main():
    date = get_date_from_user()
    if date is None:
        return

    saved_data = load_saved_data()

    if date in saved_data:
        print("Result loaded from file:")
        precipitation = saved_data[date]
    else:
        print("Fetching data from API...")
        precipitation = fetch_weather(date)

        if precipitation is not None:
            save_result(date, precipitation)

    print_result(precipitation)


main()