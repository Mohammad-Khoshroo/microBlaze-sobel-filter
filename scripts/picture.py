from PIL import Image

try:
    img = Image.open('input.png') 
except FileNotFoundError:
    print("Error: Could not find 'input.png'. Please check the file name and path.")
    exit()

WIDTH = 160
HEIGHT = 120
TOTAL_PIXELS = WIDTH * HEIGHT

img = img.convert('L').resize((WIDTH,HEIGHT))

pixels = list(img.getdata())

with open("image_data.h", "w") as f:
    f.write("#ifndef IMAGE_DATA_H\n#define IMAGE_DATA_H\n\n")
    f.write("#include <stdint.h>\n\n")
    f.write(f"// Grayscale image data ({WIDTH}x{HEIGHT} = {TOTAL_PIXELS} pixels)\n")
    f.write(f"static const uint8_t real_img_gray[{TOTAL_PIXELS}] = {{\n")
    f.write(", ".join(map(str, pixels)))
    
    f.write("\n};\n\n#endif\n")

print(f"Success! image_data.h created with {WIDTH}x{HEIGHT} resolution.")