import requests
import json

class Tiempo(object):

    def obtener(self, capital):
        aux = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=b270c8fc015a2cf595e48696fa1d5b35".format(capital)).content)
        if "main" in aux:
            d={
                "Temperatura": aux["main"]["temp"],
                "sensacion": aux["main"]["feels_like"],
                "humedad": aux["main"]["humidity"]
                }
        else:
            d = aux
        return d
