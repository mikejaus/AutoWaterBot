# AutoWaterBot
> Automatic plant watering system using a relay and raspberry pi 3

In its current state, the script checks the sensor if moisture is detected and lets the pump shoot water onto the plant until water is detected. In upcoming updates i hope to make the software more aware of how much water the plant is being given to avoid drowning the plant. I also have plans to implement a humidity sensor and link a humidifier that would be used for any plant needing moisture regulation. I also hope to implement a HTML interface so that i can access the system wherever i am and make it easier for others to monitor it aswell. A cool idea would be to add a web monitoring system with a webcam that i have spare but that might come in the late future for this project

## References / Learning Material
- Original inspiration from [The Cyber Omlette](http://www.cyber-omelette.com/2017/09/automated-plant-watering.html).

- Learning the [Moisture Sensors](https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/).
    - This reference didnt actually help me that much as the sensor i purchased was alot different, instead i learnt the basics of  connecting things to the raspberry pi from multiple videos and tutorials and managed to wrap my head around how the GPIO pins worked on a raspberry pi. After figuring out GPIO pins i learnt how to implement them into python code so that i could read and write values from the sensor.

## Purchased Materials:
- [Small Water Pump](https://www.ebay.com.au/itm/273310251939).
- [8 Channel Relay Module](https://www.ebay.com.au/itm/223212920415).
- [Hydroponic Light](https://www.ebay.com.au/itm/132567970379).
    - Not needed if you aren't growing the plant indoors
- [Raspberry Pi 3](https://www.jaycar.com.au/raspberry-pi-3b-single-board-computer/p/XC9000).
- [Soil Moisture Sensor](https://www.jaycar.com.au/arduino-compatible-soil-moisture-sensor-module/p/XC4604).
- Packet of GPIO Wires (Came with the raspberry pi kit)

## Wiring:

Start by cutting the wire that connects the pump and the power input, seperate the white and red wires and put two of the same wire going into the relay and the other two soldered back together, shown [here](https://imgur.com/a/IFV9cdd). 

Connect the ground (GND) pin on the relay to the ground pin on the raspberry pi, i found [this](https://imgur.com/a/VaiOy99) resource great for finding which pins are correct. Connect VCC to the 5V Pin on your raspberry pi. Finally connect the IN1 or whichever GPIO pin corresponds to the relay you will be using, to a GPIO slot in your raspberry pi, for me i used pin 7 (or GPIO slot 4). This will enable us to tell the raspberry pi to open the relay slot on the specified GPIO pin and enable the pump to turn on.

Connecting the moisture sensor is simple, connect the pin with the "+" sign above it to a 5V pin on the raspberry pi. Then connect the pin with the "-" symbol to a ground pin on the raspberry pi. The final pin is the GPIO pin, so choose whatever pin you would like but personally i chose pin 3 (GPIO 2).

Once all connected, download the script.py from this repository and run it on the raspberry pi. Get creative with the piping you use for the watering system, i just went for some conventional plastic tubing and poked a few holes with a heated up screwdriver, make sure you get a wide spread of water with the holes so that the whole plant is watered equally.

