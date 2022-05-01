import React from 'react';
import {Button, Card, Descriptions, Divider} from 'antd';
import LogInForm from './LogInForm';
import { selectServerAddress } from './sessionManagerSlice';

 
export const SessionManagerComponent = (props) => {

    let content = <div></div>;

    if(!props.loggedIn){
        content = <LogInForm logInFailed={props.logInFailed} onSubmit={(formValue)=>{
            props.logIn( formValue )
        }}/>
    }
    else{
        content = /*<div>
            <p>Username: {props.username}</p>
            <p>serverAddress: {props.serverAddress}</p>
            <Divider/>
            <Button onClick={props.logOut}>Log Out</Button>
        </div>*/
        <div>
        <Descriptions column={1}>
        <Descriptions.Item label="User Name">{props.username}</Descriptions.Item>
        <Descriptions.Item label="Server Address">{props.serverAddress}</Descriptions.Item>
      </Descriptions>

      <Button onClick={props.logOut}>Log Out</Button>
      </div>
        
    }

    return (
        <Card 
        title="Session Manager"
        style={{width: 400}}
        >
            {content}
        </Card>
    );
}
