import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { SessionManagerComponent } from './sessionManagerComponent';
import {
    logIn, 
    logOut,
    selectLoggingIn,
    selectLogInFailed,
    selectServerAddress,
    selectUsername,
    selectLoggedIn
} from './sessionManagerSlice';


export const SessionManager = () => {


    const username = useSelector(selectUsername)
    const serverAddress = useSelector(selectServerAddress)
    const loggedIn = useSelector(selectLoggedIn)
    const logInFailed = useSelector(selectLogInFailed)
    const loggingIn = useSelector(selectLoggingIn)

    const dispatch = useDispatch()

     return <SessionManagerComponent
        loggedIn = {loggedIn}
        loggingIn = {loggingIn}
        logInFailed = {logInFailed}
        username = {username}
        serverAddress = {serverAddress}
        logIn={(username, password, server)=>{dispatch(logIn(username, password, server))}}
        logOut={() => {dispatch(logOut())}}
     />
  }