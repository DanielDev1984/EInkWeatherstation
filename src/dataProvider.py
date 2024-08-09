import requests
from updateSvg import updateSvg
from weatherprovider import getWeather
import drawsvg as draw
import datetime
import json

def main():
    print(f"main called dataProvider")
    fetchLatestWeatherInfo()

def fetchLatestWeatherInfo():
    # data source
    hostname = "https://api.brightsky.dev/weather"

    dateHour = datetime.datetime.now().month
    if dateHour < 10:
        dateHour = "0" + str(dateHour)
    else:
        dateHour = str(dateHour)

    dateDay = datetime.datetime.now().day
    if dateDay < 10:
        dateDay = "0" + str(dateDay)
    else:
        dateDay = str(dateDay)
    date = "date="+ str(datetime.datetime.now().year) + "-" + dateHour + "-" + dateDay

    location = "lat=47.56&lon=7.79" 
        
    url = hostname+"?" + date + "&" + location


    headers = {"Accept": "apkeylication/json"}

    response = requests.get(url)
    # todo: dynamically generate filename
    outfilename = "test" + ".json"
    out_file = open(outfilename, "w")
    json.dump(response.json(), out_file)
    out_file.close()
    

def getWeatherJson():
    outfilename = "test" + ".json"
    with open(outfilename) as f:
        d = json.load(f)
    f.close()
    return d

if __name__ == "__main__":
    main()