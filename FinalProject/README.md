# Smart Cap
## Description

The Smart Cap project represents an innovative convergence of wearable technology and assistive devices. At its core, the Smart Cap is designed to enhance spatial awareness for individuals with visual impairments, utilizing a synergy of advanced sensors and smart feedback systems. With the integration of an OpenMV camera, a NeoPixel LED strip, and a microcontroller, this cap can detect the presence and proximity of people in crowded environments and provide intuitive visual and tactile feedback to the wearer.

## Inspiration

The idea for the Smart Cap was born from a personal experience in Times Square, NYC. During my first week in the city, I witnessed a visually impaired person navigating the chaotic and crowded streets with the aid of a traditional white cane. The challenges they faced — from avoiding obstacles to detecting the flow of people — sparked a realization in me about the potential for technology to aid in these daily tasks.

The bustling energy of Times Square, with its overwhelming sights and sounds, exemplified the complex environments that can pose significant challenges to those with visual impairments. This encounter became the catalyst for the Smart Cap, driving me to develop a solution that could provide a sense of confidence and independence for visually impaired individuals in similar situations.

## Project Features

- **OpenMV Camera**: Captures real-time video feeds for processing and person detection.
- **NeoPixel LED Strip**: Provides visual feedback via color changes and patterns.
- **Microcontroller (Arduino Nano 33 IoT)**: Serves as the central processing unit, interpreting sensor data and controlling feedback mechanisms.
- **Battery Pack (1300mAh)**: Powers the entire system, ensuring portability and ease of use.

## How It Works

The Smart Cap operates on a simple yet effective principle: the OpenMV camera continuously scans the immediate surroundings, the processed data is then used to control the NeoPixel LEDs, which change colors and patterns to indicate the presence and proximity of other individuals. This visual feedback allows users to understand their environment better and make informed decisions about navigation and movement.

## Finished Project Pictures:

<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/fbda4653-8519-4d27-bb5e-1091dee38ee1" height="800" width="600" alt="IMG_8219"/>
<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/2b1b40da-f364-4163-946f-b228dddfcb4b" height="800" width="600" alt="IMG_8220"/>
<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/46533c5a-617b-49e2-8797-a75cc2f8533a" height="800" width="600" alt="IMG_8221"/>
<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/3ca88988-b787-42a3-b096-dda7be71926d" height="800" width="600" alt="IMG_8222"/>
<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/ff3319f6-c1ea-4849-8281-4b8efa012235" height="800" width="600" alt="IMG_8223"/>
<img src="https://github.com/basil-ahmed/Wearables/assets/90772853/13841db0-9904-497b-9f3b-6d25fd37b969" height="800" width="600" alt="IMG_8224"/>


---

# Final Project Updates

## Week 1 Updates:

#### Description of the Circuit:

![DALL·E 2023-11-06 17 00 37 - Create a simplified schematic diagram for a Smart Cap project  Include basic symbols for an OpenMV camera, buttons, and a Nano 33 IoT microcontroller](https://github.com/basil-ahmed/Wearables/assets/90772853/68336f97-a3d1-4c93-9705-d8b39a140b21)


Here's a description of how the components might be connected:

1. **Arduino Nano 33 IoT**:
   - Vcc to Breadboard positive rail (for power)
   - GND to Breadboard ground rail (for ground)
   - Digital pins will be used to control the LEDs and to send signals to the speaker
   - The UART or I2C pins if needed for communication with the OpenMV camera

2. **OpenMV Camera**:
   - Vcc to 3.3V or 5V (depending on camera requirements)
   - GND to Ground
   - I2C/SPI/UART pins to corresponding pins on the Nano 33 IoT (for data communication)

3. **LEDs**:
   - Anode (+) to digital pins on Arduino (through a resistor, typically 220 ohms to limit current)
   - Cathode (-) to Ground

4. **Speaker**:
   - One wire to a PWM-capable pin on the Nano 33 IoT (through an amplifier circuit if needed)
   - Other wire to Ground

5. **Power Supply**:
   - Powering the entire circuit can be done through the USB port on the Nano 33 IoT, which can be connected to a portable battery pack or any 5V USB power source.

6. **Additional Components**:
   - Buttons or switches can be connected to digital pins with pull-up or pull-down resistors to control modes or turn on/off features.
   - Potentiometers can be connected to analog pins if need be to adjust volumes or settings.

7. **Connectivity**:
   - If to send notifications to a phone, the Nano 33 IoT will use its onboard Bluetooth or WiFi for communication.

Please note that this description is quite general. Each component's datasheet should be consulted to ensure correct wiring and compatibility, especially in terms of voltage and current requirements.

## Week 1 Questions:

1. How do I connect OpenMV with Arduino Nano 33 IoT?

---

## Week 2 Updates:

#### Navigating Challenges with the OpenMV Camera

#### Introduction

This week, my journey with the OpenMV camera brought some unexpected challenges. My goal was to implement person detection using TensorFlow models, but I encountered a significant roadblock related to the camera's hardware limitations and development environment constraints.

#### The Challenge with the OpenMV Camera

**Hardware Limitations:**
The model of the OpenMV camera I'm using lacks SDRAM, which is crucial for running larger TensorFlow models, like those required for person detection. This limitation became apparent when I attempted to run the person detection code, only to be met with errors.

<img width="1440" alt="Screenshot 2023-11-13 at 4 48 38 PM" src="https://github.com/basil-ahmed/Wearables/assets/90772853/0cbb13b9-3df3-4584-9202-822ac43c509d">


**Firmware and TensorFlow Model Compatibility**
Further investigation led me to the OpenMV documentation, which clarified that adding TensorFlow models to this specific camera requires building the firmware. However, there's a catch: the firmware build process isn't compatible with macOS, which is my current operating system.

<img width="682" alt="Screenshot 2023-11-13 at 4 48 55 PM" src="https://github.com/basil-ahmed/Wearables/assets/90772853/55d7daac-3dee-48e2-87c2-b5f47476c1ff">


**The Error and Documentation**
Upon running the person detection code, the OpenMV IDE displayed an error message directly related to the absence of the necessary TensorFlow model. The OpenMV documentation explicitly stated that to add this model to the camera's firmware, one needs to use a Linux machine or set up a virtual Linux environment. Unfortunately, this isn't a straightforward process on a MacBook.

<img width="1091" alt="Screenshot 2023-11-13 at 4 49 32 PM" src="https://github.com/basil-ahmed/Wearables/assets/90772853/10f107f8-b801-483c-a13d-046d9bc63ef8">


#### Navigating the Solution

To resolve this, I’m currently exploring two primary options:

1. **Setting Up a Virtual Linux Environment**: This involves running a virtual machine on my MacBook. It's a viable solution but requires significant setup and resources.

2. **Accessing a Linux Machine**: Alternatively, I could use a dedicated Linux machine for this task. This might be a more efficient route, but accessibility is a concern.

#### Consultation with Orpheas Kofinakos: Exploring Arduino Nano and OpenMV Camera Integration

This week, I also had the opportunity to book office hours with Orpheas Kofinakos from the Coding Lab in the ITP department. This consultation was pivotal, as advised by my professor, to explore the potential integration of the Arduino Nano with the OpenMV camera for my project. 

During our discussion, we delved into the technicalities and feasibility of connecting the Arduino Nano 33 IoT with the OpenMV camera. This exploration was crucial, given that both devices are integral to my project's success. We examined various aspects, including hardware interfaces, communication protocols, and the processing capabilities of both devices.

The conclusion, however, was not as encouraging as I had hoped. We found that integrating these two devices might be either extremely tricky or potentially impossible, given their current configurations and limitations. The primary challenges identified were related to the communication protocols and the processing power required for handling complex tasks like person detection in real-time.

Orpheas suggested that while a direct connection might be challenging, there could be alternative approaches to explore, such as using intermediate hardware or modifying the project scope to fit the capabilities of the available hardware. This insight was invaluable and has given me a clearer direction on how to proceed with the project.

The consultation was an eye-opener, emphasizing the importance of thorough compatibility assessment in project planning, especially when dealing with sophisticated electronics like the Arduino Nano and the OpenMV camera. 

Moving forward, I'll be revisiting the project design, considering Orpheas's insights, and exploring alternative pathways to achieve the project goals. This might involve adjusting the scope or finding creative solutions to the hardware integration challenges.

---

#### Moving Forward

Despite these challenges, I’m optimistic about finding a solution. My next steps involve either setting up a virtual environment or finding access to a Linux machine. Once this is done, I'll attempt to rebuild the firmware with the required TensorFlow model.

#### Reflective Questions and Next Steps

As I navigate these challenges, a few questions come to mind:

1. **Are there alternative methods or tools for person detection that might be more compatible with my current OpenMV camera model?**
   
2. **Could leveraging external processing power (like a connected Raspberry Pi) bypass the need for SDRAM on the camera itself?**

3. **Is there a community or forum where I could seek advice or solutions from others who have faced similar issues?**

I am eager to tackle these issues head-on and will keep updating on the progress. In the meantime, I welcome any suggestions or insights from fellow developers who have navigated similar challenges.

---

## Week 3 Updates: 

### Progress with OpenMV Camera and Arduino Nano Integration

#### Introduction

This week brought significant advancements in my project, despite encountering hurdles with the OpenMV IDE and its compatibility with TensorFlow models. A meeting with my professor led to a breakthrough in an alternative approach for person detection, and I made substantial progress in establishing communication between the OpenMV camera and the Arduino Nano 33 IoT.

#### Attempt with an Older Version of OpenMV IDE

As per my professor's suggestion, I attempted to download and run an older version of the OpenMV IDE, hoping it would support the TensorFlow model for person detection. Unfortunately, this approach did not yield the desired results, leading me to explore other avenues. The 2.9.0 version that I downloaded had a lot of bugs in detecting the OpenMV camera and after a lot of tries I moved on to find a different solution.

#### Breakthrough with Haar Cascade

Finally, Instead of relying on TensorFlow, I pivoted to using Haar Cascade for face detection through the OpenMV camera. Haar Cascade is a machine learning object detection algorithm used to identify objects in an image or video, based on the concept of features proposed by Paul Viola and Michael Jones. It is particularly effective for face detection due to its speed and accuracy, making it a suitable alternative for this project.

Utilizing Haar Cascade, I was able to successfully detect faces with the OpenMV camera. The following line of code was crucial in determining the number of faces detected in the camera frame:

```python
print("Number of Faces: ", len(objects))
```

This breakthrough is a significant step towards achieving the project’s goals.

#### Images of the Model in Action:

- **Detected Face:**

  ![1](https://github.com/basil-ahmed/Wearables/assets/90772853/4483036b-dcb6-49a4-95e6-829219f4488d)

- **When No Faces are detected:**

  <img width="1440" alt="Screenshot 2023-11-19 at 10 28 55 PM" src="https://github.com/basil-ahmed/Wearables/assets/90772853/157c6606-a4a5-424c-92b2-063207d423f1">
  
   ![IMG_7376](https://github.com/basil-ahmed/Wearables/assets/90772853/f735e4f7-674d-4c54-bf26-0c798631ff93)

- **When Faces are detected:**

  <img width="1440" alt="Screenshot 2023-11-19 at 10 29 57 PM" src="https://github.com/basil-ahmed/Wearables/assets/90772853/e0f16ff7-f55c-4150-ac0c-2a0bf5284585">

  ![IMG_7375](https://github.com/basil-ahmed/Wearables/assets/90772853/d52c8b20-ef7f-4ee2-a9eb-64d9b918b49c)


#### Establishing UART Communication

Another major development was figuring out how to establish communication between the OpenMV and the Arduino Nano. I first tried using UART (Universal Asynchronous Receiver/Transmitter) communication, a method that allows for serial communication between devices.

##### How UART Communication Works

- **Wiring**: The process involves connecting the two microprocessors with wires. This is done by connecting the TX (transmit) pin of one device to the RX (receive) pin of the other, and vice versa.

- **Data Transmission**: Data is transmitted serially, meaning one bit at a time, over these connections. This method is effective for short-distance communication between microcontrollers and peripheral devices.

- **Synchronization**: The devices are synchronized to a common baud rate to ensure proper data transmission and reception.

This UART setup will enable the OpenMV camera to send data to the Arduino Nano, such as the count of detected faces.

#### Switching from UART to I2C Communication

- **Initial Attempts with UART Communication:** In my previous update, I discussed the process of establishing UART communication between the OpenMV camera and the Arduino Nano. This involved connecting the TX and RX pins of the devices for serial data transmission and synchronizing them to a common baud rate. While UART is effective for short-distance communication, I encountered challenges in implementing this setup effectively.
- **Transitioning to I2C Communication:** Due to difficulties with the UART setup, I decided to switch to I2C (Inter-Integrated Circuit) communication. This method offers several advantages for microcontroller communication, including simpler wiring and potentially more reliable data transfer.
- **How I2C Communication Works:**
   - **Wiring Setup**: The I2C communication requires fewer connections. The OpenMV Cam's I2C Data (P5) and I2C Clock (P4) are connected to the Arduino Uno's Data (A4) and Clock (A5) pins, respectively. Both devices share a common ground connection.
     ![IMG_7401](https://github.com/basil-ahmed/Wearables/assets/90772853/90e1be4b-6264-4128-ab80-d0a9b7ebfd6b)


   - **Data Transmission**: In I2C, two lines (SDA for data, SCL for clock) are used. Data is transmitted in packets, with each packet containing information about the sender, receiver, and the data itself. This protocol allows for more flexibility and control over data transmission compared to UART.
   
   - **Error Handling and Synchronization**: Unlike UART, I2C includes built-in mechanisms for error checking and requires synchronization only for the clock line, simplifying the setup.

- **Implementation and Code Example:** The updated code for the OpenMV and Arduino is focused on establishing the OpenMV Cam as an I2C slave and the Arduino as the master. The Python script for the OpenMV Cam uses the `pyb.I2C` library to set up the I2C communication, handle data packing, and manage potential transmission errors. Meanwhile, the Arduino code employs the `Wire` library to initiate requests for data from the OpenMV Cam, process incoming data packets, and handle any discrepancies in the received data.

This I2C setup is intended to enhance the reliability of communication between the OpenMV camera and the Arduino Nano, ensuring more stable data transfer for applications like facial detection and count.

---

#### Next Steps and Considerations

Moving forward, the next steps involve:

1. **Determining the Output**: I am considering different output options like using Bluetooth for smartphone communication, LEDs, or sound alerts through a speaker.

2. **Sewing the Boards on a Cap**: Both the OpenMV camera and Arduino Nano, along with the chosen output device, will be sewn onto a cap. This requires careful planning to ensure stability and functionality.

3. **Powering the Boards**: A key question arises – how will both these boards be powered effectively when mounted on the cap? This is crucial for the portability and usability of the project.

#### Questions and Reflections

As I delve deeper into this project, several questions come to mind:

1. **What is the most efficient way to power both the OpenMV camera and the Arduino Nano when they are sewn onto a cap?**

2. **Are there any potential issues I should anticipate with UART communication in this setup?**

3. **What would be the most user-friendly and practical output method for this project – Bluetooth communication, LEDs, or a speaker system?**

4. **How can I ensure that the sewing of the boards onto the cap is secure and does not interfere with their functionality?**

This project is proving to be an exciting challenge, blending hardware interfacing, coding, and creative problem-solving. I am eager to continue this journey and look forward to any feedback or suggestions from the community.

---

## Week 4 Updates: 

**Title: Navigating NeoPixels and OpenMV Cam: My Weekly Project Update**

**Introduction:**
Welcome back to my blog where I chronicle my journey through the dynamic world of wearable technology. This week's update is especially exciting as it marks a significant pivot in my final project. Initially, I planned to use mobile phone notifications as an output for the number of people detected by the OpenMV Cam. However, after considering the time constraints and potential anxiety-inducing effects of increasing LED blink rates, a discussion with my professor led to a strategic shift. We decided to employ NeoPixels as a more visually appealing and less stress-inducing output method. Here's how this week unfolded with this new direction.

**The Shift to NeoPixels**

Adapting to the new plan, I dove into controlling NeoPixels using the OpenMV Cam. This involved researching and figuring out NeoPixel compatibility and then running a sample code that showcased a mini light show, a testament to the versatility and visual appeal of NeoPixels. The idea is for the lights to change in color and pattern in response to the number of people detected, offering a more subtle and engaging feedback mechanism.

Reference: https://docs.micropython.org/en/v1.8.2/esp8266/esp8266/tutorial/neopixel.html

https://github.com/basil-ahmed/Wearables/assets/90772853/2d26be05-80ab-43e8-a403-2befd0929833


**Overcoming Lab Challenges**

Despite the excitement of the NeoPixels, I encountered a minor setback. I intended to glue the wires to the NeoPixels for a tidier setup, but all the glue guns in the lab were unavailable. This hiccup, though a small one, was a reminder of the need for flexibility and problem-solving in any project.

I also tried using the black NeoPixel strip as that would've looked better with the black cap, however, because of already existing resistors and a 3.3V OpenMV Output, I had to work with the White NeoPixel Strip.

**Creating a Home for the OpenMV Cam**

Another key development this week was finding the perfect box for the OpenMV Cam. The box will not only protect the board but will also be mounted on the top of the cap, forming the core of my project. I've chosen Velcro for its attachment, balancing the need for secure placement with the flexibility of easy removal.

![IMG_7866 Medium](https://github.com/basil-ahmed/Wearables/assets/90772853/5a316a58-c819-4d29-8ba6-5b2319a62f4c)


**Conclusion:**

This week has been a mix of progress and learning. The switch to NeoPixels has opened up new creative avenues, while the challenges faced in the lab have taught me the importance of adaptability. Each step, whether it's programming a light show or selecting the right box for the camera, is bringing me closer to the completion of this innovative project.

**Looking Ahead**

I'm eager to further explore the capabilities of the NeoPixels and to finalize the mounting of the OpenMV Cam!

---

## Week 5 Updates: 

**Title: Nearing Completion: In-Depth Week 5 Update on My Wearable Tech Project**

![DALL·E 2023-12-04 17 09 08 - A sequence of images depicting the process of a final project in technology and wearables  Image 1_ A person soldering red, white, and orange wires (P](https://github.com/basil-ahmed/Wearables/assets/90772853/250297c3-a594-47de-9d35-c622aec39963)

**Introduction:**
Hello readers! As I near the completion of my wearable technology project, I'm here to share a comprehensive Week 5 update. This week was pivotal, full of intricate tasks and critical decision-making. From precise soldering to integrating the wearables component, each step was taken with specific goals in mind. Let me walk you through the detailed process of this week's advancements.

**Soldering and Stabilizing the Wires**

The week commenced with soldering the power (PWR, Red), ground (GND, White), and data input (DI, Orange) wires to the NeoPixels. The choice of these specific colors was to ensure easy identification and minimize errors during connection. Soldering provided a strong electrical connection necessary for the consistent operation of the NeoPixels. To further stabilize these connections and prevent any potential short-circuits, I applied hot glue over the soldered areas. This not only secured the wires physically but also insulated them, reducing the risk of electrical faults.

![IMG_7877](https://github.com/basil-ahmed/Wearables/assets/90772853/e8ee3a3d-fc4c-4164-9189-ee619e37be0f)

![IMG_7879](https://github.com/basil-ahmed/Wearables/assets/90772853/e72ea015-a7da-4a04-9901-6933d8c05266)

![IMG_7880](https://github.com/basil-ahmed/Wearables/assets/90772853/ed8d42fe-159e-4c0e-8bea-927c06c6d3e9)

**Meticulous Multimeter Testing**

After soldering, I tested each connection with a multimeter, using its audio continuity function. This step was crucial to confirm that there were no loose connections or shorts. This thorough testing ensured the reliability of my soldering work and the overall integrity of the electronic circuit.

![IMG_7878](https://github.com/basil-ahmed/Wearables/assets/90772853/93a77a42-e5d0-4e75-b921-a9206d7b5c50)


**Independent Operation with Battery Power**

*Image: The project powered by a 1200 mAh battery.*
![IMG_7883](https://github.com/basil-ahmed/Wearables/assets/90772853/1fc0b826-eb45-4d63-b8ea-c138fe5993f2)

A significant milestone was testing the OpenMV uploaded code with a 1200 mAh battery. This battery choice was influenced by its capacity to provide adequate power for extended periods, making the device more practical for real-world use. Running the code on battery power demonstrated the project's functionality independent of a computer, a key aspect of wearable technology.


https://github.com/basil-ahmed/Wearables/assets/90772853/de86fab5-b9fe-4c4c-b877-6a353fd2eb68


**Integrating the Technology into Wearables**

The integration of the technology into a wearable form involved choosing a cap as the base. The cap was selected for its universal fit and ease of wear. I attached the NeoPixel strip with super glue, a robust adhesive that ensured a firm hold while being discreet. The placement of the strip was strategically done to ensure visibility of the lights when worn, enhancing the user's experience.

![IMG_7922](https://github.com/basil-ahmed/Wearables/assets/90772853/484f4963-3b77-458b-ac91-643e8ae30791)

![IMG_7923](https://github.com/basil-ahmed/Wearables/assets/90772853/211d2fb8-69d0-4e34-a047-97f860ccf2f6)

**Selecting and Preparing the Electronics Housing**

Choosing a new box to house the camera, microprocessor, wires, and battery was a decision based on size and convenience. The box needed to be large enough to accommodate all components while being compact enough to fit comfortably on the cap. I customized the box by making a hole for the camera and providing an opening for the USB cable, which allowed for easy access during testing and troubleshooting.

![IMG_7924](https://github.com/basil-ahmed/Wearables/assets/90772853/b95a59d5-2140-41ef-8cd5-7262f639602d)

**Attaching the Box to the Cap**

Mounting the box onto the cap involved using Velcro. This choice was driven by the need for a secure yet removable attachment method. Velcro provides the flexibility to detach the box for adjustments or maintenance while ensuring it stays in place during use.

![IMG_7926](https://github.com/basil-ahmed/Wearables/assets/90772853/8cda1ba9-6c09-4898-87d1-0ecd78a30203)

**Aesthetic Enhancement**

Painting the box black was an aesthetic decision to harmonize it with the cap's color. This touch was crucial for the visual appeal of the project, making the technology appear seamless with the wearable component.

![IMG_7927](https://github.com/basil-ahmed/Wearables/assets/90772853/061f11f2-00a6-4d4f-bf4b-32955e2f1f0b)

**Real-World Testing and Code Development**

Developing a code to correlate the number of people detected with the lighting pattern was the next step. This functionality was tested in a real-world scenario with friends to verify its accuracy and responsiveness. This test was essential to ensure that the project worked as intended in actual use.

**Upcoming Task: Camera Orientation**

The final task for the upcoming week is to adjust the camera's orientation by 90 degrees. This adjustment is necessary for both aesthetic reasons and to optimize the camera's field of view. The corresponding code modification will involve rotating the frame within the software to maintain detection accuracy.

**Conclusion:**

Week 5 has been a journey of precision, practical decision-making, and creative problem-solving. With the project now 95% complete, I am excited to share the final touches in the upcoming update. Stay tuned for the culmination of this innovative wearable technology project!

---

## Week 6 Updates:

**Title:** Breakthrough in Smart Cap: Camera Feed Rotation and Successful Testing

**Introduction:**

Hello everyone! Welcome back to my weekly update on the Smart Cap project. This week has been particularly exciting as I achieved a significant milestone in enhancing the OpenMV camera’s functionality and successfully tested the Smart Cap with multiple people. Let’s dive into the details of this week’s progress.

**Rotating the Camera Feed:**

One of the technical challenges I faced was the orientation of the OpenMV camera feed. Given the positioning of the camera on the cap, the feed needed to be rotated to accurately capture the environment in front of the wearer. This week, I managed to rotate the camera feed using MicroPython, a huge step towards making the Smart Cap more practical and user-friendly.

The process involved delving into the OpenMV documentation and tweaking the camera settings using MicroPython code. This adjustment now allows the camera to capture images in the correct orientation, irrespective of how it’s mounted on the cap.

**Successful Testing with People Detection:**

The real triumph of the week was the successful testing of the Smart Cap with up to three people. Using the Haar Cascade algorithm, the cap could effectively detect and distinguish individuals in its vicinity. This testing was crucial in validating the cap's ability to function accurately in real-world scenarios.

The tests were conducted in various settings to simulate different levels of crowd density. The Smart Cap performed remarkably well, providing accurate visual feedback through the NeoPixels based on the number of people detected. This success marks a significant leap forward in the project, bringing the Smart Cap closer to its intended functionality.

**Reflections and Learnings:**

This week’s achievements have been incredibly rewarding. Overcoming the challenge with the camera orientation has not only improved the functionality but also deepened my understanding of camera systems and MicroPython programming. The successful people detection test has boosted my confidence in the project's potential and applicability in real-life situations.

**Conclusion:**

The sixth week of development has been a blend of technical triumphs and reaffirming the practicality of the Smart Cap. Each step, whether it's tweaking code or real-world testing, brings this project closer to its goal – enhancing spatial awareness for visually impaired individuals in crowded environments. Stay tuned for more updates as the Smart Cap continues to evolve!

> **_Next Steps:_** The Final Project for the course has been completed! I will keep working on the prototype to make it go out in the world.

---

_Thank you for following along on this journey. Your support and feedback have been invaluable. If you have any suggestions or insights, feel free to share them in the comments below!_


## The Code:

``` 
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
```
