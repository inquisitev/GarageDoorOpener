import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import {selectServerAddress} from './../sessionManager/sessionManagerSlice.js'
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
    async ({dispatch, getState}) => {
        const state = getState()
        const serverAddress = selectServerAddress(state)
        dispatch(sessionManagerSlice.actions.triggerDoorRequested())
        return await axios({
            method: 'post',
            url: formValues.serverAddress + '/door_button',
            data: {
              user: formValues.username,
              password_plain: formValues.password
            }
          });
    }
)

export const doorControlSlice = createSlice({
    name: 'doorControls',
    initialState,
    reducers: {
        doorTriggerRequest: (state, action) => {
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(triggerDoor.pending, (state) => {
                
            })
            .addCase(triggerDoor.fulfilled, (state, action) => {

            })
            .addCase(triggerDoor.rejected, (state, action) => {

            });
      },
});



export default doorControlSlice.reducer;
