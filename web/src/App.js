import React from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import { SessionManager } from './features/sessionManager/sessionManager';
import { SessionManagerComponent } from './features/sessionManager/sessionManagerComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <SessionManager/>
        
        
        
      </header>
    </div>
  );
}

export default App;
