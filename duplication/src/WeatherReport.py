class Forecast:
    def __init__(self, period, temperature, condition, wind_speed):
        self.period = period  # "morning", "afternoon", "evening", "night"
        self.temperature = temperature
        self.condition = condition
        self.wind_speed = wind_speed

    def get_period(self):
        return self.period

    def get_temperature(self):
        return self.temperature

    def get_condition(self):
        return self.condition

    def get_wind_speed(self):
        return self.wind_speed


class WeatherReport:
    def format_daily_report(self, forecasts, output):
        for forecast in forecasts:

            line = (
                forecast.get_period().capitalize() + ": "
                + str(forecast.get_temperature())
                + "°C, "
                + forecast.get_condition()
                + ", wind "
                + str(forecast.get_wind_speed())
                + "km/h"
            )
            output.append(line)
