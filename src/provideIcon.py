import requests
from updateSvg import updateSvg
from weatherprovider import getWeather

def main():
    print(f"main called")
    
url = "https://api.brightsky.dev/weather?date=2024-06-09&lat=47.56&lon=7.79"

#querystring = {"date":"2024-06-01","last_date":"2023-08-08","lat":"52.52","lon":"13.4"}
querystring = {""}

headers = {"Accept": "application/json"}

response = requests.get(url)

for key in response.json()["weather"]:
    print(key["timestamp"] + " " + str(key["temperature"]))

'''output_dict = {
        'WEATHER_ICON': getWeather()
    }
    # todo: use relative path
template_svg_filename = "/home/daniel/development/eink/EInkWeatherstation/pic/screen-template.svg"
output_svg_filename = 'screen-output-weather.svg'
updateSvg(template_svg_filename,output_dict, output_svg_filename)'''

print(f"call main")

if __name__ == "__main__":
    main()