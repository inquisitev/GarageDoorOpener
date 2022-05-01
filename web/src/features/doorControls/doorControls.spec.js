import doorControlReducer, { triggerDoor, updateDoorState, makeInitialState } from "./doorControlSlice";


describe('Door Controls reducer', () => {
    
    it('should handle initial state',async () =>  {
      const initialState = makeInitialState()

      expect(doorControlReducer(initialState, { type: 'unknown' })).toEqual(
        initialState
      );
    });

    it('should show failed on rejected trigger',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorTriggerState.triggerPending = true
      initialState.doorTriggerState.triggerFailed = false
      initialState.doorTriggerState.triggerSuccess = false

      expectedState.doorTriggerState.triggerFailed = true
      expectedState .doorTriggerState.triggerPending = false
      expectedState.doorTriggerState.triggerSuccess = false


      expect(doorControlReducer(initialState, {type: triggerDoor.rejected})).toEqual(
          expectedState
      );
    });

    it('should show pending while awaiting response trigger',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorTriggerState.triggerPending = false
      initialState.doorTriggerState.triggerFailed = false
      initialState.doorTriggerState.triggerSuccess = true

      expectedState.doorTriggerState.triggerFailed = false
      expectedState.doorTriggerState.triggerPending = true
      expectedState.doorTriggerState.triggerSuccess = false

      expect(doorControlReducer(initialState, {type: triggerDoor.pending})).toEqual(
          expectedState
      );
    });

    it('should show pending successful when fulfilled trigger',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorTriggerState.triggerPending = true
      initialState.doorTriggerState.triggerFailed = false
      initialState.doorTriggerState.triggerSuccess = false

      expectedState.doorTriggerState.triggerFailed = false
      expectedState.doorTriggerState.triggerPending = false
      expectedState.doorTriggerState.triggerSuccess = true

      expect(doorControlReducer(initialState, {type: triggerDoor.fulfilled})).toEqual(
          expectedState
      );
    });

    it('should show failed on rejected update',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorState.updatePending = false
      initialState.doorState.updateFailed = false

      expectedState.doorState.updateFailed = true
      expectedState .doorState.updatePending = false

      expect(doorControlReducer(initialState, {type: updateDoorState.rejected})).toEqual(
          expectedState
      );
    });

    it('should show pending while awaiting response update',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorState.updatePending = false
      initialState.doorState.updateFailed = false

      expectedState.doorState.updateFailed = false
      expectedState.doorState.updatePending = true

      expect(doorControlReducer(initialState, {type: updateDoorState.pending})).toEqual(
          expectedState
      );
    });

    it('should show pending successful when fulfilled update',async () =>  {
      const initialState = makeInitialState()
      const expectedState = makeInitialState()

      initialState.doorState.updatePending = true
      initialState.doorState.updateFailed = false

      expectedState.doorState.updateFailed = false
      expectedState.doorState.updatePending = false
      expectedState.doorState.currentState = "DOOR_CLOSED"

      const response = {
        "data": {
            "state": "DOOR_CLOSED"
        },
        "status": 200,
        "statusText": "OK",
    }


    expect(doorControlReducer(initialState, {type: updateDoorState.fulfilled, payload: response})).toEqual(expectedState);

    });

});