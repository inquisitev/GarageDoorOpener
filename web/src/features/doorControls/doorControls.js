import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import DoorControlsComponent from './doorControlsComponent';
import { triggerDoor } from './doorControlSlice';

export const DoorControls = () => {


    const dispatch = useDispatch()

     return <DoorControlsComponent doorTrigger={()=>{dispatch(triggerDoor())}}/>
  }