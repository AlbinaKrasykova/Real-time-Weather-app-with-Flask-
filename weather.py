import requests 
from datetime import datetime 

# API key
id_stored = '**************'

def get_weather(location):
    # Construct the complete API link with location and API key
    complete_api_link = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={id_stored}'

    # Get weather data from the API
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    
    # Check if the API response contains the expected keys
    if 'main' in api_data and 'weather' in api_data and 'wind' in api_data:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        icon =  api_data['weather'][0]['icon']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        data_time = datetime.now().strftime("%d %b %Y | %I :%M: %S %p")
        # add temp_city,hmdt, wind_spd, data_time
        return weather_desc, int(temp_city), icon
    else:
        return None

'''
def print_weather(temp_city, weather_desc, hmdt, wind_spd, data_time, location):
    print("---------------------------------------------------------------------")
    print(weather_desc)
    print('Weather stats for - {} || {}'.format(location.upper(), data_time))
    print("---------------------------------------------------------------------")
    print("Current temperature is {:.2f} deg C".format(temp_city))
    print("Humidity ", hmdt, '%')
    print("Wind speed {:.2f} deg C".format(wind_spd))


    location = input("Enter the city name: ")
print_weather(*get_weather(location), location)

'''




