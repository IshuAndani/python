import requests
import pandas
import matplotlib.pyplot as plt
import os

lat = 23.259933
lon = 77.412613
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
response = requests.get(url)
data = response.json()
print(data)

daily_data = data["daily"]

df = pandas.DataFrame(
    {
        "date": pandas.to_datetime(daily_data["time"]),
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)
print(df)

plt.figure(figsize=(10, 5))

plt.plot(df["date"], df["max_temp"], label="Max Temperature")
plt.plot(df["date"], df["min_temp"], label="Min Temperature")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Forecast for Lat: {lat}, Lon: {lon}")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_forecast.png")  # Save the plot as an image file
plt.show()

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/bhopal_weather.csv")
