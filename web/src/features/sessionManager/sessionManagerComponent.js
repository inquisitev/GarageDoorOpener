import React from 'react';
import {Card} from 'antd';
import LogInForm from './LogInForm';

 
export const SessionManagerComponent = (props) => {

    let content = <div></div>;

    if(!props.loggedIn){
        content = <LogInForm onSubmit={(formValue)=>{
            props.logIn( formValue )
        }}/>
    }
    else{
        content = <div>
            <p>Username: {props.username}</p>
            <p>serverAddress: {props.serverAddress}</p>
            <button onClick={props.logOut}>Log Out</button>
        </div>
        
    }

    return (
        <Card>
            {content}
        </Card>
    );
}
