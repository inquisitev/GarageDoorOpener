import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { SessionManagerComponent } from './sessionManagerComponent';
import {
    logIn, 
    logOut,
    signUp,
    selectServerAddress,
    selectUsername,
    selectLoggedIn
} from './sessionManagerSlice';


export const SessionManager = () => {


    const username = useSelector(selectUsername)
    const serverAddress = useSelector(selectServerAddress)
    const loggedIn = useSelector(selectLoggedIn)

    const dispatch = useDispatch()

     return <SessionManagerComponent
        loggedIn = {loggedIn}
        username = {username}
        serverAddress = {serverAddress}
        logIn={(username, password, server)=>{dispatch(logIn(username, password, server))}}
     />
  }