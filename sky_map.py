from skyfield.api import load, Topos
from skyfield.starlib import Star
from PIL import Image, ImageDraw

def generate_star_map(lat, lon):
    ts = load.timescale()
    t = ts.now()

    eph = load('de421.bsp')
    observer = Topos(latitude_degrees=lat, longitude_degrees=lon)
    earth = eph['earth']
    location = earth + observer

    image = Image.new("RGB", (800, 800), "black")
    draw = ImageDraw.Draw(image)

    # Load star data
    with open('star_data/hipparcos_visible.csv', 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:
        try:
            ra, dec, mag = map(float, line.strip().split(','))
            if mag > 6.5:
                continue
            star = Star(ra_hours=ra, dec_degrees=dec)
            astrometric = location.at(t).observe(star)
            alt, az, _ = astrometric.apparent().altaz()
            if alt.degrees > 0:
                x = int((az.degrees / 360) * 800)
                y = int((1 - (alt.degrees / 90)) * 800)
                size = max(1, int(3 - mag / 2))
                draw.ellipse((x-size, y-size, x+size, y+size), fill="white")
        except Exception as e:
            print(f"Skipping star due to error: {e}")

    # Draw planets
    for name in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']:
        try:
            planet = eph[name]
            astrometric = location.at(t).observe(planet)
            alt, az, _ = astrometric.apparent().altaz()
            if alt.degrees > 0:
                x = int((az.degrees / 360) * 800)
                y = int((1 - (alt.degrees / 90)) * 800)
                draw.ellipse((x-3, y-3, x+3, y+3), fill="cyan")
        except Exception as e:
            print(f"Skipping planet {name} due to error: {e}")

    return image
