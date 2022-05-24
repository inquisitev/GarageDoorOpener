import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import DoorControlsComponent from './doorControlsComponent';
import { selectCurrentDoorState, triggerDoor, updateDoorState } from './doorControlSlice';

export const DoorControls = () => {
    const dispatch = useDispatch()
    const doorState = useSelector(selectCurrentDoorState)

     return <DoorControlsComponent doorState={doorState} getDoorState={()=>{dispatch(updateDoorState())}} doorTrigger={()=>{dispatch(triggerDoor())}}/>
  }
