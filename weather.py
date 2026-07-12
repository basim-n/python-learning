import requests
API_KEY="bd9fe17c7cfdcd1fa85dd5d32a4ab112"
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL="http://api.openweathermap.org/data/2.5/forecast"


def weather(city):
    params={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
    response=requests.get(BASE_URL,params=params)
    return response.json()
def display_weather(data):
        if int(data['cod']) !=200:
              print(f"ERROR:{data['message']}")
        else:
              print("-"*12)
              print(f"CITY:{data['name']},{data['sys']['country']}")
              print(f"TEMPERATURE:{data['main']['temp']} oC")
              print(f"Feels Like:{data['main']['feels_like']}")
              print(f"HUMIDITY: {data['main']['humidity']}")
              print(f"CONDITION:{data['weather'][0]['description']}")
              print("-"*12)
def get_forecast(city):
      params={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
      response=requests.get(FORECAST_URL,params=params)
      return response.json()
def display_forecast(data):
      if str(data['cod'])!='200':
            print(f"ERROR:{data['message']}")
            return
      
      print(f"\n5-Day Forecast for {data['city']['name']}, {data['city']['country']}")
      print("-" * 40)
      for entry in data['list']:
            if '12:00:00' in entry['dt_txt']:
                        print(f"{entry['dt_txt']} | {entry['main']['temp']}oC | {entry['weather'][0]['description']}")

while True:
      print(f"=== WEATHER APP===")
      print("1.Current Weather")
      print("2.5 day forecast")
      print("3.Quit")
      ch=input("Enter a choice:")
      if ch=='1':
             city=input("Enter city or 'quit' to exit:")
             data=weather(city)
             display_weather(data)
      elif ch=='2':
            city=input("Enter city name:")

            data=get_forecast(city)
            display_forecast(data)
      elif ch =='3':
            print("GOODBYE!")
            break

