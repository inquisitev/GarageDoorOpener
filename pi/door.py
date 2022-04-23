import pifacedigitalio as p
import time, json

"""
Garage door interface kept simple.
"""

p.init()

door_down = []
door_up = []

with open('./config.json', 'r') as config_file:
    config = json.loads(config_file.read())
    door_up = config['door_open_sensors']
    door_down = config['door_closed_sensors']


def garage_door_button():
    '''
    Short the garage door wires for half a second and return to the open state.
    '''
    p.digital_write(0,1)
    time.sleep(.5)
    p.digital_write(0,0)

def garage_door_state():
    '''
    Read all of the digital pin assigned to both door down and door up.
    '''
    door_is_down = all([p.digital_read(x) for x in door_down])
    door_is_up = all([p.digital_read(x) for x in door_up])

    if door_is_down:
        return 'DOOR_CLOSED'
    elif door_is_up: 
        return 'DOOR_OPEN'
    else:
        return "DOOR_INBETWEEN"

def garage_door_sensor_states():
    '''
    Get the state of all garage door sensors.
    '''
    states = {}

    for x, i in enumerate(door_down):
        states[f'DOOR_DOWN_{i}'] = bool(p.digital_read(x))
    
    for x, i in enumerate(door_up):
        states[f'DOOR_UP_{i}'] = bool(p.digital_read(x))
    
    return states