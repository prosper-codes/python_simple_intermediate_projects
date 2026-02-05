
import requests



API_KEY = "your api key"



def get_data(place, forecast_days=None, kind=None ):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data [:nr_values]
    return filtered_data




# def get_data(place, forecast_days=1):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
#     response = requests.get(url)
#     data = response.json()
#
#     # Check if API returned forecast
#     if "list" not in data:
#         raise ValueError(f"Could not fetch data for {place}. Response: {data}")
#
#     nr_values = 8 * forecast_days  # 8 entries per day (3-hour forecast)
#     filtered_data = data["list"][:nr_values]  # slice first n values
#     return filtered_data





if __name__ == "__main__":
    print(get_data(place="warsaw", forecast_days=3, kind="Temperature"))
