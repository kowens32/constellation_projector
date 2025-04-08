from sky_map import gnerate_star_map
from display import show_image
from config import LATITUDE, LONGITUDE

def main():
    image = generate_star_map(LATTITUDE, LONGITUDE)
    show_image(image)

if __name__ == "__main__":
    main()
