from PIL import Image
import os

def show_image(image):
    path = "/tmp/star_map.png"
    image.save(path)

    if platform.system() == "Linux" and "raspberrypi" in platform.uname().node:
        os.system(f"sudo fbi -T 1 -d /dev/fb0 -noverbose -a {path}")
    else:
        print(f"[DEBUG] Skipping image display, not running on Pi.")