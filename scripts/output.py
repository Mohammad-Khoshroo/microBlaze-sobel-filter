import serial
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

COM_PORT = 'COM12' 
BAUD_RATE = 115200

WIDTH = 160        
HEIGHT = 120
TOTAL_PIXELS = WIDTH * HEIGHT

def receive_image():
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=10)
        print(f"Connected to {COM_PORT}. Waiting for 'START_IMAGE'...")

        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line == "START_IMAGE":
                print("START_IMAGE received! Capturing pixels...")
                break

        pixels = []
        while len(pixels) < TOTAL_PIXELS:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.isdigit():
                pixels.append(int(line))

        print("All pixels received successfully!")
        ser.close()

        img_array = np.array(pixels, dtype=np.uint8).reshape((HEIGHT, WIDTH))

        plt.figure(figsize=(6, 5))
        plt.imshow(img_array, cmap='gray')
        plt.title('Sobel Output (160x120)')
        plt.axis('off')
        plt.show()

        output_img = Image.fromarray(img_array)
        output_img.save("sobel_output.png")
        print("Image saved as 'sobel_output.png'!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    receive_image()