import React from 'react';
import './App.css';
import { DoorControls } from './features/doorControls/doorControls';
import { SessionManager } from './features/sessionManager/sessionManager';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <SessionManager/>
        <DoorControls/>
        
        
        
      </header>
    </div>
  );
}

export default App;
