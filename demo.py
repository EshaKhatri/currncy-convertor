import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = "INR"
currency_2 = "USD"
amount="1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "33ec956489mshe3576a6601ce4b4p189d5fjsn86e032ac4476",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data=json.loads(response.text)
converted_Amount = data['result']['convertedAmount']
formatted = "{:,.2f}".format(converted_Amount)

print(converted_Amount,formatted)