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

for line in lines[1:]: # Skip header
    ra, dec = map(float, line.strip().split(','))
    star = eph['earth'].at(t).observe(load.star(ra_hours=ra, dec_degress=dec))
    alt, az, _ = star.apparent().altaz()
    if alt.degress > 0:
        x = int((az.degress / 360 ) * 800)
        y = int((1 - (alt.degrees / 90)) * 800)
        draw.ellipse((x-1, y-1, x+1, y +1), fill="white")
return image