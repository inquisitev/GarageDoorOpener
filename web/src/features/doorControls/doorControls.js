import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import DoorControlsComponent from './doorControlsComponent';
import { selectCurrentDoorState, triggerDoor } from './doorControlSlice';

export const DoorControls = () => {
    const dispatch = useDispatch()
    const doorState = useSelector(selectCurrentDoorState)

     return <DoorControlsComponent doorTrigger={()=>{dispatch(triggerDoor())}}/>
  }
