import sensor
import time
import image
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin('P3'), 18)

def smart_cap(np, num_faces):
    n = np.n

    if num_faces == 0:
        for j in range(n):
            np[j] = (0, 0, 0)
        np.write()
    elif num_faces < 2:
        # cycle
        for i in range(n):
            for j in range(n):
                np[j] = (0, 100, 0)
            np[i % n] = (255, 255, 255)
            np.write()
            time.sleep_ms(25)
    elif num_faces < 3:
        # cycle
        for i in range(n):
            for j in range(n):
                np[j] = (0, 0, 100)
            np[i % n] = (255, 255, 255)
            np.write()
            time.sleep_ms(25)
    else:
        # cycle
        for i in range(n):
            for j in range(n):
                np[j] = (100, 0, 0)
            np[i % n] = (255, 255, 255)
            np.write()
            time.sleep_ms(25)

# Reset sensor
sensor.reset()

# Sensor settings
sensor.set_contrast(3)
sensor.set_gainceiling(16)
# HQVGA and GRAYSCALE are the best for face tracking.
sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# FPS clock
clock = time.clock()

while True:
    clock.tick()

    # Capture snapshot
    img = sensor.snapshot()
    # Rotate the image by 90 degrees to correct for the camera's physical rotation
    img.rotation_corr(z_rotation=90)

    # Find objects.
    # Note: Lower scale factor scales-down the image more and detects smaller objects.
    # Higher threshold results in a higher detection rate, with more false positives.
    objects = img.find_features(face_cascade, threshold=0.90, scale_factor=1.20)

    # Draw objects
    for r in objects:
        img.draw_rectangle(r)

    num_faces = len(objects)

    smart_cap(np, num_faces)

    # Print FPS.
    # Note: Actual FPS is higher, streaming the FB makes it slower.
    print(clock.fps())
