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
