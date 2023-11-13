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

### Week 2 Updates:
