import 'modules/materialize-css/dist/css/materialize.min.css'
import 'modules/font-awesome/css/font-awesome.min.css'
import './app.css'

import React from 'react'

import TopBar from '../template/topBar/topBar'
import Routes from './routes'


export default props => {
    return (
        <div>
            <div className='container'>
                <TopBar />
                <Routes />
            </div>
        </div>
    )
}
