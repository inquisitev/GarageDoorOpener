from pickle import FALSE
from server.Tests.GarageDoorOpener.StubbedOpener import StubbedOpener

def test_opener():
    opener = StubbedOpener([0,1,2], [3,4,5])
    opener.pin_set(0,1)
    opener.pin_set(1,1)
    opener.pin_set(2,1)
    assert opener.garage_door_state() == "DOOR_OPEN"

    opener.pin_set(0,0)
    opener.pin_set(1,0)
    opener.pin_set(2,0)
    assert opener.garage_door_state() == "DOOR_INBETWEEN"

    opener.pin_set(3,1)
    opener.pin_set(4,1)
    opener.pin_set(5,1)
    assert opener.garage_door_state() == "DOOR_CLOSED"

    states = opener.garage_door_sensor_states()
    assert states["DOOR_UP_0"] == False
    assert states["DOOR_UP_1"] == False
    assert states["DOOR_UP_2"] == False
    assert states["DOOR_DOWN_0"] == True
    assert states["DOOR_DOWN_1"] == True
    assert states["DOOR_DOWN_2"] == True

