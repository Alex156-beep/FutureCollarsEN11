import requests
from datetime import datetime, timedelta
import os


class WeatherForecast:
    def __init__(self, filename, latitude, longitude):
        self.filename = filename
        self.latitude = latitude
        self.longitude = longitude
        self.data = {}
        self._load()

    # ---------------- FILE HANDLING ----------------

    def _load(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                date, value = line.strip().split(",")
                self.data[date] = float(value)

    def _save(self):
        with open(self.filename, "w") as file:
            for date, value in self.data.items():
                file.write(f"{date},{value}\n")

    # ---------------- DICT-LIKE METHODS ----------------

    def __setitem__(self, date, value):
        self.data[date] = value
        self._save()

    def __getitem__(self, date):
        if date in self.data:
            return self.data[date]

        value = self._fetch_from_api(date)
        if value is not None:
            self[date] = value
        return value

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for item in self.data.items():
            yield item

    # ---------------- API ----------------

    def _fetch_from_api(self, date):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            "&daily=precipitation_sum"
            "&timezone=Europe%2FLondon"
            f"&start_date={date}"
            f"&end_date={date}"
        )

        try:
            response = requests.get(url)
            data = response.json()
            return data["daily"]["precipitation_sum"][0]
        except Exception:
            return None


# ---------------- HELPER FUNCTIONS ----------------

def get_date_from_user():
    user_input = input("Enter date (YYYY-mm-dd) or press Enter for tomorrow: ")

    if user_input == "":
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%Y-%m-%d")

    try:
        datetime.strptime(user_input, "%Y-%m-%d")
        return user_input
    except ValueError:
        print("Invalid date format.")
        return None


def print_result(value):
    if value is None or value < 0:
        print("I don't know")
    elif value == 0.0:
        print("It will not rain")
    else:
        print(f"It will rain ({value} mm)")


# ---------------- MAIN PROGRAM ----------------

def main():
    weather = WeatherForecast(
        filename="weather.txt",
        latitude=51.5072,     # London
        longitude=-0.1276
    )

    date = get_date_from_user()
    if date is None:
        return

    result = weather[date]
    print_result(result)

    print("\nSaved forecasts:")
    for d, v in weather.items():
        print(d, "→", v)


main()