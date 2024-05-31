from updateSvg import updateSvg
from weatherprovider import getWeather

def main():
    print(f"main called")
    output_dict = {
        'WEATHER_ICON': getWeather()
    }
    # todo: use relative path
    template_svg_filename = "/home/daniel/development/eink/EInkWeatherstation/pic/screen-template.svg"
    output_svg_filename = 'screen-output-weather.svg'
    updateSvg(template_svg_filename,output_dict, output_svg_filename)

print(f"call main")

if __name__ == "__main__":
    main()