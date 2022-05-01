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
    //    dispatch(doorControlSlice.actions.triggerDoorRequested())
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
