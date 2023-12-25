import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "f19eb99514714016b27123437232512"

sehir = input("şehir: ")

response = requests.get(url, params= {
    "key": access_key,
    "q": sehir,
    "lang": "tr"
})

sonuc = response.json()

sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havadurumu} derece ve {text}.")