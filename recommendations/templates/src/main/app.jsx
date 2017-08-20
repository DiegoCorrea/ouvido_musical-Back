import 'modules/materialize-css/dist/css/materialize.min.css'
import 'modules/font-awesome/css/font-awesome.min.css'
import './app.css'

import React from 'react'
import FacebookLogin from 'react-facebook-login'

import TopBar from '../template/topBar/topBar'
import Routes from './routes'


export default props => {
    const responseFacebook = (response) => {
        if (response.accessToke != 'undefined')
            console.log(response);
        else
            console.log("sem login")
    };

    const checkLoginState = (response) => {
        if (response.status == 'connected')
            responseFacebook
        else
            console.log("sem login")
    }
    return (
        <div>
            <div className='container'>
                {/*
                <FacebookLogin
                appId="1420911897974648"
                autoLoad
                callback={responseFacebook}
                icon="fa-facebook"
                />*/}
                <TopBar />
                <Routes />
            </div>
        </div>
    )
}