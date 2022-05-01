import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import DoorControlsComponent from './doorControlsComponent';

export const SessionManager = () => {


    //const username = useSelector(selectUsername)
    //const serverAddress = useSelector(selectServerAddress)

    const dispatch = useDispatch()

     return <DoorControlsComponent/>
  }