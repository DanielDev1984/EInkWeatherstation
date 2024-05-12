#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
import logging
import epd7in5_V2
import time
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # draw image
    logging.info("read image file")
    Himage = Image.open(os.path.join(picdir, 'svgToPngTest.png'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(20)

    """ Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)

    # partial update
    logging.info("show date")
    epd.init_part()
    num = 0
    while (True):
        draw.rectangle((10, 120, 130, 170), fill = 127)
        draw.text((10, 120), time.strftime('%D'), font = font24, fill = 0)
        epd.display_Partial(epd.getbuffer(Himage),0, 0, epd.width, epd.height)
        num = num + 1
        time.sleep(2)
        if(num == 4):
            break """


    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit(cleanup=True)
    exit()