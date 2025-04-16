from PIL import Image
import os
import platform

def show_image(image):
    path = "output/star_map.png"
    image.save(path)

    if platform.system() == "Linux" and "raspberrypi" in platform.uname().node:
        # Display on Pi LCD using fbi
        os.system(f"sudo fbi -T 1 -d /dev/fb0 -noverbose -a {path}")
    else:
        print("Running on non-Pi system — opening image preview.")
        image.show()
