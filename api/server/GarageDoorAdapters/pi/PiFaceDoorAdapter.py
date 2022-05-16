#from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter
import json,time
import pifacedigitalio as piface

pifacedigital = piface.PiFaceDigital()
pifacedigital.leds[2].turn_on()

piface.digital_write(1, 1)
time.sleep(100)
piface.digital_write(1, 0)


#class PiFaceDoorAdapter(GenericGarageDoorAdapter):
#    def _init_controller(self):
#        piface.init()        
#
#        self.door_up = []
#        self.door_down = []
#        with open('./config.json', 'r') as config_file:
#            config = json.loads(config_file.read())
#            self.door_up = config['door_open_sensors']
#            self.door_down = config['door_closed_sensors']
#
#    def _digital_read(self, pin: int) -> bool:
#        return bool(piface.digital_read(pin))
#
#    def _digital_write(self, pin: int, val: bool) -> None:
#        return piface.digital_write(pin, int(val))