import requests
API_KEY=""
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"


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
while True:
      city=input("Enter city or 'quit' to exit:")
      if city!='quit':
           data=weather(city)
           display_weather(data)
      else:
            break

