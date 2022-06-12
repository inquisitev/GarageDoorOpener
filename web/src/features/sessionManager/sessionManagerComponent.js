import React from 'react';
import {Button, Card, Col, Descriptions, Row, Typography} from 'antd';
import LogInForm from './LogInForm';
import Avatar from 'antd/lib/avatar/avatar';
import { UserOutlined } from '@ant-design/icons';

const {Text} = Typography

 
export const SessionManagerComponent = (props) => {

    let content = <div></div>;

    if(!props.loggedIn){
        content = <LogInForm logInFailed={props.logInFailed} onSubmit={(formValue)=>{
            props.logIn( formValue )
        }}/>
    }
    else{
        content = (<div>
            <Row>
                <Col span={8}>
                    <Avatar icon={<UserOutlined />} />
                </Col>
                <Col span={32}>
                    <Text>{props.username} </Text>
                </Col>
            </Row>
            <Button onClick={props.logOut}>Log Out</Button>
      </div>)
        
    }

    return (
        <Card 
        style={{width: 400}}
        >
            {content}
        </Card>
    );
}
