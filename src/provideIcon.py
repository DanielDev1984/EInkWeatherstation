import requests
from updateSvg import updateSvg
from weatherprovider import getWeather
import drawsvg as draw
import datetime
import dataProvider as dP
import dataMapper as dM

def main():
    createTemperatureGraph()
    #createPrecipitationGraph()
    print(f"main called provideIcon")

def createTemperatureGraph():
    temperatures = dM.getTemperature()

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
    # graph provider
    d = draw.Drawing(500, 800,origin='center')
    for i in range(0,23):
        d.append(draw.Lines(i*10,-temperatures[i],i*10+10,-temperatures[i+1],close=False, stroke_width=4,fill='none',stroke='black'))
    
    d.append(draw.Lines(minTempIndex*10, -temperatures[minTempIndex], minTempIndex*10, -temperatures[minTempIndex]-10,close=False, fill='white', stroke='black'))
    d.append(draw.Text(str(temperatures[minTempIndex]/tempScaleFactor), 14, minTempIndex*10, -temperatures[minTempIndex]-20,text_anchor='middle',font_family='DejaVu'))
    d.append(draw.Lines(maxTempIndex*10, -temperatures[maxTempIndex], maxTempIndex*10, -temperatures[maxTempIndex]-10,close=False, fill='white', stroke='black'))
    d.append(draw.Text(str(temperatures[maxTempIndex]/tempScaleFactor), 14, maxTempIndex*10, -temperatures[maxTempIndex]-20,text_anchor='middle',font_family='DejaVu'))

    d.append(draw.Lines(0,-temperatures[0],0,-temperatures[minTempIndex],close=False, fill='white', stroke='black'))
    d.append(draw.Lines(120,-temperatures[11],120,-temperatures[minTempIndex],close=False, fill='white', stroke='black'))
    d.append(draw.Text("00:00", 20, 0,-temperatures[minTempIndex]+20, text_anchor='middle',font_family='DejaVu'))
    d.append(draw.Text("12:00", 20, 120,-temperatures[minTempIndex]+20, text_anchor='middle',font_family='DejaVu'))

    currentHour = datetime.datetime.now().hour
    d.append(draw.Circle( currentHour*10, -temperatures[currentHour], 10, fill='grey', stroke='black'))

    # todo: provide interface for date as well
    #d.append(draw.Text(date, 28, 0,0,font_family='DejaVu'))

    d.save_svg('/home/daniel/development/eink/EInkWeatherstation/pic/icons/temperature_graph_hour.svg')

    output_dict = {
            'WEATHER_ICON': getWeather()
        }
        # todo: use relative path
    template_svg_filename = "/home/daniel/development/eink/EInkWeatherstation/pic/screen-template.svg"
    output_svg_filename = 'screen-output-weather.svg'
    updateSvg(template_svg_filename,output_dict, output_svg_filename)
    print(f"create temperature graph called")

def createPrecipitationGraph():
    precipitation = dM.getPrecipitation()
    print(f"precipitation in array: {precipitation}")
    probability = dM.getPrecipitationProbability()
    print(f"precipitationProbability in array: {probability}")


if __name__ == "__main__":
    main()