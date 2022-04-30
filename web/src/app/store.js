import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import { reducer as formReducer } from 'redux-form'
import sessionManagerReducer from '../features/sessionManager/sessionManagerSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    sessionManager: sessionManagerReducer,
    form: formReducer
  },
});
