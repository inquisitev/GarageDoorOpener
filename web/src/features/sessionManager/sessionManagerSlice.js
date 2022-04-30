import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

export const makeInitialState = () => {
    return {
        logInState:{
            loggedIn: false,
            loggingIn: false,
            logInFailed: false, 
            logInFailedReason: "",
        },
        createAccountState:{
            createAccountFailed:false, 
            createAccountSuccess:false,
            creatingAccount: false,
            createAccountFailedReason: "",
        },
        serverAddress: "",
        user: {
            username:"",
            token:""
        }
    }
  }

const initialState = makeInitialState()

export const logIn = createAsyncThunk(
    "sessionManager/login",
    async (formValues, {dispatch}) => {
        dispatch(sessionManagerSlice.actions.logInRequest(formValues))
        return await axios({
            method: 'post',
            url: formValues.serverAddress + '/login',
            data: {
              user: formValues.username,
              password_plain: formValues.password
            }
          });
    }
)

export const signUp = createAsyncThunk(
    "sessionManager/signup",
    async (username, password, email, serverAddress) => {

    }
)

export const sessionManagerSlice = createSlice({
    name: 'sessionManager',
    initialState,
    reducers: {
        logInRequest: (state, action) => {
            state.user.username = action.payload.username
            state.serverAddress = action.payload.serverAddress
        },
        logOut: (state) => {},
        signUp: (state) => {},
    },
    extraReducers: (builder) => {
        builder
          .addCase(logIn.pending, (state) => {
            state.user.loggingIn = true
          })
          .addCase(logIn.fulfilled, (state, action) => {
              if (action.payload.status == 200){
                state.logInState.loggedIn = true
                state.logInState.loggingIn = false
                state.user.token = action.payload.data.token
              }
              else{
                  state.logInState.logInFailed = true
                  state.logInState.loggingIn = false
              }
          })
          .addCase(signUp.pending, (state) => {
            state.createAccountState.creatingAccount = true
          })
          .addCase(signUp.fulfilled, (state, action) => {

          });
      },
});

export const selectToken = (state) => state.sessionManager.user.token
export const selectUsername = (state) => state.sessionManager.user.username
export const selectServerAddress = (state) => state.sessionManager.serverAddress
export const selectLoggedIn = (state) => state.sessionManager.logInState.loggedIn
export const selectLoggingIn = (state) => state.sessionManager.logInState.loggingIn
export const selectLogInFailed = (state) => state.sessionManager.logInState.logInFailed
export const selectCreatingAccount = (state) => state.sessionManager.createAccountState.creatingAccount
export const selectCreateAccountSuccess = (state) => state.sessionManager.createAccountState.createAccountSuccess
export const selectCreateAccountFailed = (state) => state.sessionManager.createAccountState.createAccountFailed

export const {logOut} = sessionManagerSlice.actions


export default sessionManagerSlice.reducer;
