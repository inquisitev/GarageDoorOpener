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
        
        <SessionManagerComponent
          loggedIn = {true}
          username={'username'}
          serverAddress={'127.0.0.1:800'}
        />
        <SessionManagerComponent
          loggedIn = {false}
          logInFailed = {false}
        />
        <SessionManagerComponent
          loggedIn = {false}
          logInFailed = {true}
      />
        
      </header>
    </div>
  );
}

export default App;
