#this program will grap data from open weather api using rest api
# and summarize the info for your city


import requests, json



def getcurrentweatherinfo(item):
    if "main" in item:
        if "temp" in item["main"]:
            print("Temperature: ", item.get("main").get("temp"))
            print("Feels Like: ", item.get("main").get("feels_like"))
            print("Temperatur High: ", item.get("main").get("temp_max"))
            print("Temperature Low: ", item.get("main").get("temp_min"))
            print("Humidity: ", item.get("main").get("humidity"))

        if "sys" in item:
            print("Country: ", item.get("sys").get("country"))

    print("City:",item.get("name"))
                

zip_code ="55343" #input("Please enter your zip code: ")
country_code= "US"

api_key="13c596151801eae996897b2c1800c4a3"

url="http://api.openweathermap.org/data/2.5/weather?zip="+ zip_code + "," + country_code + "&appid=" + api_key + "&units=imperial"
print(url)

#url= "http://api.openweathermap.org/data/2.5/weather?q=Hopkins,US-MN&appid=13c596151801eae996897b2c1800c4a3&units=imperial"

# Make a get request to get the latest position of the current weather statio.
response = requests.get(url)
wjson = response.json()
getcurrentweatherinfo(wjson)

