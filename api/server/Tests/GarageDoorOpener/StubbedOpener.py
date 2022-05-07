from server.GarageDoorAdapters.GenericGarageDoorAdapter import GenericGarageDoorAdapter

class StubbedOpener(GenericGarageDoorAdapter):
    def _init_controller(self):
        pass

    def __init__(self, door_up, door_down):
        self.pin_states = [False for x in range(8)]
        self.door_up = door_up
        self.door_down = door_down

    def pin_set(self, pin, val):
        self.pin_states[pin] = val

    def _digital_read(self, pin: int) -> bool:
        return self.pin_states[pin]

    def _digital_write(self, pin: int, val: bool) -> None:
        self.pin_states[pin] = val