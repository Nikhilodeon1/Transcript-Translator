
import requests
url3 = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload3 = "q=Hello%2C%20world!&target=es&source=en"
headers3 = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "b2a20d965cmsha261263e4ee25b6p15523ajsn10d1a691befb",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response3 = requests.request("POST", url3, data=payload3, headers=headers3)

print(response3.text)