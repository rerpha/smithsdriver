# smithsdriver
Small microcontroller based device to convert a 2-wire temperature sensor, drive a relay, and output to a classic car smiths gauge

It uses a [waveshare rp2040-zero](https://www.waveshare.com/wiki/RP2040-Zero) board (todo: say everything else it uses)

other parts: 
- enclosure: https://thepihut.com/products/general-purpose-project-enclosure-75x50x27mm ?
- MOSFETs: 2x AO3400A
- 12V to 5V DC-DC buck converter


## KiCAD

to open the schematic you will need to go to preferences -> manage symbol libraries

then add `RP2040-Zero-Kicad/` as a library

