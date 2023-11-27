# Final Project Updates
## Smart Cap

### Week 1 Updates:

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
