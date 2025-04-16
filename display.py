from PIL import Image
import os

def show_image(image):
    path = "/tmp/star_map.png"
    image.save(path)
    os.system(f"sud fbi -T 1 -d /dev/fb0 -noverbose -a {path}")