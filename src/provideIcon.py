import requests
from updateSvg import updateSvg
from weatherprovider import getWeather
import drawsvg as draw
import datetime

def main():
    print(f"main called")

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
temperatures = []

for key in response.json()["weather"]:
    print(key["timestamp"] + " " + str(key["temperature"]))
    temperatures.append(key["temperature"])


minTemp = min(temperatures)
minTempIndex = 0
maxTemp = max(temperatures)
maxTempIndex = 0
tempScaleFactor = 5.0
for i in range(len(temperatures)):
    if minTemp == temperatures[i]:
        minTempIndex = i
    if maxTemp == temperatures[i]:
        maxTempIndex = i
    temperatures[i]  = temperatures[i]*tempScaleFactor

print(f"temps in array: {temperatures}")

d = draw.Drawing(500, 800,origin='center')
d.append(draw.Lines(0,-temperatures[0],10,-temperatures[1],
                    10,-temperatures[1],20,-temperatures[2],
                    20,-temperatures[2],30,-temperatures[3],
                    30,-temperatures[3],40,-temperatures[4],
                    40,-temperatures[4],50,-temperatures[5],
                    50,-temperatures[5],60,-temperatures[6],
                    60,-temperatures[6],70,-temperatures[7],
                    70,-temperatures[7],80,-temperatures[8],
                    80,-temperatures[8],90,-temperatures[9],
                    90,-temperatures[9],100,-temperatures[10],
                    100,-temperatures[10],110,-temperatures[11],
                    110,-temperatures[11],120,-temperatures[12],
                    120,-temperatures[12],130,-temperatures[13],
                    130,-temperatures[13],140,-temperatures[14],
                    140,-temperatures[14],150,-temperatures[15],
                    150,-temperatures[15],160,-temperatures[16],
                    160,-temperatures[16],170,-temperatures[17],
                    170,-temperatures[17],180,-temperatures[18],
                    180,-temperatures[18],190,-temperatures[19],
                    190,-temperatures[19],200,-temperatures[20],
                    200,-temperatures[20],210,-temperatures[21],
                    210,-temperatures[21],220,-temperatures[22],
                    220,-temperatures[22],230,-temperatures[23],
                    230,-temperatures[23],240,-temperatures[24],
                    close=False, fill='white', stroke='black'))

d.append(draw.Lines(minTempIndex*10, -temperatures[minTempIndex], minTempIndex*10, -temperatures[minTempIndex]-10,close=False, fill='white', stroke='black'))
d.append(draw.Text(str(temperatures[minTempIndex]/tempScaleFactor), 14, minTempIndex*10, -temperatures[minTempIndex]-20,text_anchor='middle'))
d.append(draw.Lines(maxTempIndex*10, -temperatures[maxTempIndex], maxTempIndex*10, -temperatures[maxTempIndex]-10,close=False, fill='white', stroke='black'))
d.append(draw.Text(str(temperatures[maxTempIndex]/tempScaleFactor), 14, maxTempIndex*10, -temperatures[maxTempIndex]-20,text_anchor='middle'))

d.append(draw.Lines(0,-temperatures[0],0,-temperatures[minTempIndex],close=False, fill='white', stroke='black'))
d.append(draw.Lines(120,-temperatures[11],120,-temperatures[minTempIndex],close=False, fill='white', stroke='black'))
d.append(draw.Text("00:00", 20, 0,-temperatures[minTempIndex]+20, text_anchor='middle'))
d.append(draw.Text("12:00", 20, 120,-temperatures[minTempIndex]+20, text_anchor='middle'))

currentHour = datetime.datetime.now().hour
d.append(draw.Circle( currentHour*10, -temperatures[currentHour], 10, fill='grey', stroke='black'))

d.append(draw.Text(date, 28, 0,0))

d.save_svg('temperature_graph_hour.svg')

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