import requests
API_KEY="ea8069c10c90968095c45897a8de2516"
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"


def weather(city):
    params={
        "q":city,
        "appid":API_KEY,
        "units":"metric"
    }
    response=requests.get(BASE_URL,params=params)
    return response.json()
city=input("Enter your city:")
data=weather(city)
print(data)


