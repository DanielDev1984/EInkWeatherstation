import dataProvider as dP

def getTemperature():
    return getWeatherInfoForKey("temperature")

def getPrecipitation():
    return getWeatherInfoForKey("precipitation")

def getPrecipitationProbability():
    return getWeatherInfoForKey("precipitation_probability")
    
def getWeatherInfoForKey(keyName):
    responseJson = dP.getWeatherJson()
    weatherInfo = []    
    for key in responseJson["weather"]:
        print(key["timestamp"] + " " + str(key[keyName]))
        weatherInfo.append(key[keyName])
    return weatherInfo


