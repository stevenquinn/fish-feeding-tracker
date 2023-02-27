from adafruit_magtag.magtag import MagTag
import time
import rtc
import board
from secrets import secrets



class FishFeeder:

    def __init__(self):
        self.magtag = MagTag()
        self.display = board.DISPLAY
        self.should_refresh_display = True
        self.time_synced = False
        self.fed_morning = False
        self.fed_evening = False
        self.magtag.network.connect()
        print("Connected to WiFi.")
        time.sleep(2)
        self.check_time()

        # Run in a loop.
        while True:
            self.run()
            time.sleep(self.display.time_to_refresh)


    def run(self):

        # If it's between 12am and 1am, reset the has_been_fed_today flag to False.
        if self.should_reset_feeder():
            self.reset_feeder()

        if self.button_pressed():
            self.fish_was_fed()

        self.update_display()

        

    def check_time(self):

        self.magtag.get_local_time()
        self.time_synced = True
    
     
    def should_reset_feeder(self):

        now = rtc.RTC().datetime
        return now.tm_hour == 0 and (self.fed_morning or self.fed_evening)


    def reset_feeder(self):
            
        # Reset the has_been_fed_today flag to False.
        self.fed_morning = False
        self.fed_evening = None

    
    def button_pressed(self):

        return self.magtag.peripherals.button_a_pressed or self.magtag.peripherals.button_b_pressed or self.magtag.peripherals.button_c_pressed or self.magtag.peripherals.button_d_pressed 


    def fish_was_fed(self):

        if self.fed_morning is True and self.fed_evening is True:
            self.fed_morning = False
            self.fed_evening = False
        elif self.fed_morning is True:
            self.fed_evening = True
        else:
            self.fed_morning = True

        self.should_refresh_display = True

    
    def update_display(self):

        backgroundImage = "not-fed"

        if self.fed_morning is True:
            backgroundImage = "fed-morning"

        if self.fed_morning is True and self.fed_evening is True:
            backgroundImage = "fed-evening"

        self.magtag.graphics.set_background("/images/" + backgroundImage + ".bmp")

        if self.should_refresh_display:
            self.magtag.display.refresh()
            self.should_refresh_display = False




feeder = FishFeeder()
