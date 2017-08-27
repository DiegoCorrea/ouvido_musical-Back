import React, { Component} from 'react'
import ReactDOM from 'react-dom';
import { Router, Route, Redirect, hashHistory } from 'react-router'

import Users from '../user/users'
import UserPage from '../user/userPage'

import Songs from '../song/songs'
import SongPage from '../song/songPage'

import Recommendations from '../recommendation/recommendations'

import LoginPage from '../login/loginPage'

export default props => (
    <Router history={hashHistory}>
        <Route path='/' component={LoginPage} />
    
        <Route path='/users' component={Users} />
        <Route path='/users/:uuid' component={UserPage} />
        <Route path='/users/:uuid/recommendations' component={Recommendations} />

        <Route path='/songs' component={Songs} />
        <Route path='/songs/:uuid' component={SongPage}/>
        <Route path='/songs/:uuid/recommendations' component={Recommendations} />

        <Redirect from='*' to='/' />
    </Router>
)
