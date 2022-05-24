import time

"""
Garage door interface kept simple.
"""
class GenericGarageDoorAdapter:

    def __init__(self):
        self.door_down = [3,4]
        self.door_up = [0,1,2]

    def garage_door_button(self):
        '''
        Short the garage door wires for half a second and return to the open state.
        '''
        self._digital_write(0,1)
        time.sleep(.5)
        self._digital_write(0,0)

    def garage_door_state(self):
        door_is_down = all([self._digital_read(x) for x in self.door_down])
        door_is_up = all([self._digital_read(x) for x in self.door_up])

        if door_is_down:
            return 'DOOR_CLOSED'
        elif door_is_up: 
            return 'DOOR_OPEN'
        else:
            return "DOOR_INBETWEEN"

    def garage_door_sensor_states(self):
        states = {}

        for i, x in enumerate(self.door_down):
            states[f'DOOR_DOWN_{i}'] = self._digital_read(x)
        
        for i, x in enumerate(self.door_up):
            states[f'DOOR_UP_{i}'] = self._digital_read(x)

        return states

    def _digital_read(self, pin: int) -> bool:
        return True

    def _digital_write(self, pin: int, val: bool) -> None:
        pass

    def _init_controller(self):
        pass
