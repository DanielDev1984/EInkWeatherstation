
. env.sh

function log {
    echo "---------------------------------------"
    echo ${1^^}
    echo "---------------------------------------"
}

log "start program"

python3 provideIcon.py

cairosvg -o ../pic/svgToPngTest.png -f png --dpi 300 --output-width 800 --output-height 480 screen-output-weather.svg

python3 HelloDisplay.py