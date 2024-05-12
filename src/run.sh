
. env.sh

cairosvg -o ../pic/svgToPngTest.png -f png --dpi 300 --output-width 800 --output-height 480 ../pic/testImage.svg

python3 HelloDisplay.py