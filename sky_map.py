from skyfield.api import load, Topos
from datetime import datetime
from PIL import Image, ImageDraw

def generate_star_map(lat, lon);
ts = load.timescale()
t = ts.now()

eph = load('de421.bsp')
observer = Topos(latittude_degrees=lat, longigtude_degrees=lon)
earth = eph['earth']
location = earth + observer

#loading bright stars from HIpparcos catalog 

with load.open('star_data/bright_stars.csv') as f:
    lines = f.readlines()

image = Image.new("RGB", (800,800), "black")
draw = ImageDraw.draw(image)