# Fish Feeding Tracker

My daughter got a fish tank for her 5th birthday and I wanted an easy way for her to keep track of how many times she fed the fish each day. I also had an Adafruit Magtag lying around not being used and thought, why not?

## Hardware

* [Adafruit Magtag](https://www.adafruit.com/product/4800)

## Software

* [CircuitPython](https://circuitpython.org/board/adafruit_magtag_2.9_grayscale/)

**Note:** This project was built using CircuitPython 6.2.0-beta.2. It may not work with other versions.

## Setup

1. Copy `secrets.py.example` to `secrets.py` and update the values with your own. This uses Adafruit IO to store the data. You can create an account [here](https://io.adafruit.com/). **NOTE** your Magtag will need to connect to the internet to get an accurate time to reset correctly every day.
2. Copy this entire repo to the Magtag when it boots.  

## Usage

By default, the Magtag will display two fish food icons. Pressing the button will change one of them to a thumbs up, and doing it again will change the second to a thumbs up. Once more will cycle back to two fish food icons. The Magtag should reset automatically every day at 12:00 AM.