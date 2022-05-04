import { configureStore } from '@reduxjs/toolkit';
import { reducer as formReducer } from 'redux-form'
import sessionManagerReducer from '../features/sessionManager/sessionManagerSlice';
import doorControlsReducer from '../features/doorControls/doorControlSlice.js';

export const store = configureStore({
  reducer: {
    sessionManager: sessionManagerReducer,
    doorControls: doorControlsReducer,
    form: formReducer
  },
});
