import React from 'react';
import '../../App.css';
import { Breadcrumb, Layout, Menu } from 'antd';
import { DoorControls } from '../doorControls/doorControls';
import { SessionManager } from '../sessionManager/sessionManager';
import { SessionManagerComponent } from '../sessionManager/sessionManagerComponent';
const { Header, Content, Sider } = Layout;
const navHeaders = [].map((key) => ({
  key,
  label: `${key}`,
}));
const menuItems = [
  {
    key: `sessionManager`,
    icon: React.createElement(icon),
    children: []
  }
]

const Home = () => (
  <Layout>
    <Header className="header">
      <div className="logo" />
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['Home']} items={navHeaders} />
    </Header>
    <Layout>
      <Sider width={200} className="site-layout-background">
        <Menu
          mode="inline"
          defaultSelectedKeys={['1']}
          defaultOpenKeys={['sub1']}
          style={{
            height: '100%',
            borderRight: 0,
          }}
          items={menuItems
        }
        />
      </Sider>
      <Layout
        style={{
          padding: '0 24px 24px',
        }}
      >
        <Content
          className="site-layout-background"
          style={{
            padding: 24,
            margin: 0,
            minHeight: 280,
          }}
        >
          <SessionManagerComponent loggedIn={true} username="username" serverAddress="123.456.0.78" />
          {/*<SessionManager/>
          <DoorControls/>*/}

        </Content>
      </Layout>
    </Layout>
  </Layout>
);

export default Home;