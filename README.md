# Technovation Software Challenege
### Problem Statement:
Approximately 1.3 million people die in road traffic related accidents every year. This is an alarming figure and we, as proactive engineers must come up with an effective solution to bring these figures down.

In order to ensure pedestrian safety and vehicle speed limits in areas with high pedestrian density/residential areas, design a system to detect the traffic density in school areas/ residential areas and accordingly warn the driver about the speed limit for vehicles. The system needs to provide a warning to the driver, if the speed limits are breached.

### Solution:
- We will use the Vision Based systems which sense the speed limit signs using sign boards for schools/hospitals/accident prone areas etc. and will decide upon the safe speed value with which the vehicle need to operate. 

- The system will provide a warning to the driver, if the speed limits are breached. 

- The warning will be provided using LCD or Seven Segment Simple Display and a Buzzer. The sign boards for the purpose of safe speed will be made according to IRC standards and the same can be used by the system for calculating safe speed.

### Roadmap For Solution:
1. Road Activity monitoring
2. Vehicle Data Monitoring
3. Alert System

## 1. Road Activity monitoring:
- Camera Sensor is used to detect and recognize the traffic sign boards and traffic density.

- Similar colors and shape of the sign boards can be used for the detection of safe speed. We can also detect the traffic density. We can use Machine Learning Technology using Python OpenCV for this purpose.

## 2. Vehicle Data Monitoring:
- We need to use ELM-327 Bluetooth adapter to measure the real time ECU’s value (speed, engine rpm, temperature, fuel rate, and oxygen) of vehicle using OBD II (On Board Diagnostics Protocol) 

- We will gather and process the data for speed detection and many more features such as temperature, fuel rate and measuring oxygen in the vehicle.

## 3. Alert System:
- The alert and processed output will be display on LCD and buzzer will be buzzed.

- A speaker is also used to give appropriate instructions to the driver in speech format.

### Why our solution is useful:
1. It requires a low cost.
2. It gives not only speed detecting features but also senses temperature , determines fuel rate, oxygen level, engine rpm, fuel system status, torque in the vehicle.
3. It gives an alert on the LCD screen and speaker. 
4. Read diagnostic trouble codes, both generic and manufacture specific.
