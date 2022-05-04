import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import {selectServerAddress, selectToken} from '../sessionManager/sessionManagerSlice.js'
import axios from 'axios';

export const makeInitialState = () => {
    return {
        doorState:{
            updatePending: false,
            updateFailed: false,
            currentState: ""
        },
        doorTriggerState:{
            triggerPending: false,
            triggerFailed: false,
            triggerSuccess:false
        }
    }
  }

const initialState = makeInitialState()

export const triggerDoor = createAsyncThunk(
    "doorControls/triggerDoor",
    async (args, {dispatch, getState}) => {
        const state = getState()
        const serverAddress = selectServerAddress(state) + '/door_button'
        const token = selectToken(state)
        return await axios({
            method: 'post',
            url: serverAddress,
            data: {
                token: token
            }
          });
    }
)

export const updateDoorState = createAsyncThunk(
    "doorControls/updateDoorState",
    async (args, {dispatch, getState}) => {
        const state = getState()
        const serverAddress = selectServerAddress(state) + '/door_state'
        const token = selectToken(state)
        return await axios({
            method: 'post',
            url: serverAddress,
            data: {
                token: token
            }
          });
    }
)


export const doorControlSlice = createSlice({
    name: 'doorControls',
    initialState,
    reducers: {
        
    },
    extraReducers: (builder) => {
        builder
        .addCase(triggerDoor.pending, (state) => {
            state.doorTriggerState.triggerPending = true
            state.doorTriggerState.triggerFailed = false
            state.doorTriggerState.triggerSuccess = false
        })
        .addCase(triggerDoor.fulfilled, (state, action) => {
            state.doorTriggerState.triggerPending = false
            state.doorTriggerState.triggerFailed = false
            state.doorTriggerState.triggerSuccess = true
        })
        .addCase(triggerDoor.rejected, (state, action) => {
            state.doorTriggerState.triggerPending = false
            state.doorTriggerState.triggerFailed = true
            state.doorTriggerState.triggerSuccess = false
        })
        .addCase(updateDoorState.pending, (state) => {
            state.doorState.updatePending = true
            state.doorState.updateFailed = false
            state.doorState.currentState = ""
        })
        .addCase(updateDoorState.fulfilled, (state, action) => {
            state.doorState.updatePending = false
            state.doorState.updateFailed = false
            state.doorState.currentState = action.payload.data.state
        })
        .addCase(updateDoorState.rejected, (state, action) => {
            state.doorState.updatePending = false
            state.doorState.updateFailed = true
            state.doorState.currentState = ""
        });
      },
});

export const selectCurrentDoorState = (state) => state.doorControls.doorState.currentState
export const selectCurrentDoorStateUpdatePending = (state) => state.doorControls.doorState.updatePending
export const selectCurrentDoorStateUpdateFailed = (state) => state.doorControls.updateFailed
export const selectDoorTriggerPending = (state) => state.doorControls.doorTriggerState.triggerPending
export const selectDoorTriggerSuccess = (state) => state.doorControls.doorTriggerState.triggerSuccess
export const selectDoorTriggerFailure = (state) => state.doorControls.doorTriggerState.triggerFailed

export default doorControlSlice.reducer;
