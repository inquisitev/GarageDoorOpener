import { configureStore } from '@reduxjs/toolkit';
import { reducer as formReducer } from 'redux-form'
import sessionManagerReducer from '../features/sessionManager/sessionManagerSlice';

export const store = configureStore({
  reducer: {
    sessionManager: sessionManagerReducer,
    form: formReducer
  },
});
